#!/usr/bin/env python3
"""Render the CAPTF README fragments and sync them into each README.

Reads repos.toml, writes banners/<repo>.svg from templates/banner.svg, and
replaces the body of every marked block in each repository's README with
the rendered fragment:

    <!-- captf:header -->
    ...
    <!-- /captf:header -->

Repositories are found in the workspace, the directory holding their
checkouts (default: the one holding this .github checkout); the .github
repository is always this checkout. A README gets only the blocks it already
has markers for; a README that is not checked out is skipped. With --check nothing is written, and the exit
status is 1 if any banner or block is out of date.
"""

import argparse
import pathlib
import re
import string
import sys
import textwrap
import tomllib
from xml.sax.saxutils import escape

HERE = pathlib.Path(__file__).resolve().parent
CHECKOUT = HERE.parent
TEMPLATES = HERE / "templates"
BANNERS = HERE / "banners"

RAW = "https://raw.githubusercontent.com/captf-io/.github/refs/heads/main/readme"
SHIELDS = "https://img.shields.io"
# Badge colours: the label is the site's --surface, the values its accents.
LABEL = "161B3A"
PURPLE, BLUE, YELLOW = "A974FF", "5B8CFF", "FFD84D"

FRAGMENTS = ("header", "status", "footer")
BLOCK = re.compile(
    r"(?P<open><!-- captf:(?P<name>[a-z]+) -->\n)(?P<body>.*?)(?P<close><!-- /captf:(?P=name) -->)",
    re.S,
)

# Banner geometry, in the template's 1200x260 user units.
TAGLINE_MAX = 60  # characters
TITLE_MAX = 64  # font size
TITLE_WIDTH = 860  # from the left margin to clear of the glyph tile
TITLE_EM = 0.52  # average advance of a bold sans character, in em
PILL_CHAR = 10.2  # advance of an eyebrow character at 14px, letter-spaced
PILL_PAD = 60  # mark, gaps and the pill's rounded ends


def template(name):
    return string.Template((TEMPLATES / name).read_text())


def banner(repo):
    """Return the SVG banner for a repository."""
    name, tagline = repo["name"], repo["tagline"]
    if len(tagline) > TAGLINE_MAX:
        sys.exit(f"{name}: tagline is {len(tagline)} characters, over {TAGLINE_MAX}")
    eyebrow = f"CAPTF · {repo['kind'].upper()}"
    size = min(TITLE_MAX, int(TITLE_WIDTH / (TITLE_EM * len(name))))
    title_y = 118 + round(0.72 * size)
    glyph = (TEMPLATES / "glyphs" / f"{repo['glyph']}.svg").read_text()
    return template("banner.svg").substitute(
        name=escape(name),
        tagline=escape(tagline),
        eyebrow=escape(eyebrow),
        pill_width=round(PILL_PAD + PILL_CHAR * len(eyebrow)),
        title_size=size,
        title_y=title_y,
        tagline_y=title_y + 48,
        glyph=textwrap.indent(glyph.rstrip("\n"), " " * 6),
    )


def slug(repo):
    return repo["name"].lstrip(".")


def attr(name, value, indent=4):
    """An HTML attribute, wrapped to stay inside 80 columns."""
    pad = " " * indent
    return textwrap.fill(
        f'{name}="{escape(value, {chr(34): "&quot;"})}"',
        width=80,
        initial_indent=pad,
        subsequent_indent=pad,
    )


def badge(alt, src, href):
    return f'  <a href="{href}"><img\n    src="{src}"\n    alt="{alt}"></a>'


def static_badge(label, message, color):
    return (
        f"{SHIELDS}/static/v1?label={label}&amp;message={message}"
        f"&amp;color={color}&amp;labelColor={LABEL}&amp;style=flat-square"
    )


def badges(repo):
    """The badge row: build status, then contract, docs and licence."""
    row = []
    if ci := repo.get("ci"):
        name = repo["name"]
        row.append(
            badge(
                "build",
                f"{SHIELDS}/github/actions/workflow/status/captf-io/{name}/{ci}"
                f"?branch=main&amp;label=build&amp;labelColor={LABEL}&amp;style=flat-square",
                f"https://github.com/captf-io/{name}/actions/workflows/{ci}",
            )
        )
    row += [
        badge(
            "contract v1alpha1",
            static_badge("contract", "v1alpha1", PURPLE),
            "https://captf.io/docs/module-author/contract/index.html",
        ),
        badge("docs captf.io", static_badge("docs", "captf.io", BLUE), "https://captf.io/docs/"),
    ]
    if repo.get("license", True):
        row.append(badge("license Apache-2.0", static_badge("license", "Apache-2.0", YELLOW), "LICENSE.md"))
    return '<p align="center">\n' + "\n".join(row) + "\n</p>"


def fragments(repo):
    """The rendered body of each block, by name; no header without a banner."""
    license = '<a href="LICENSE.md">Apache 2.0</a>' if repo.get("license", True) else "Apache 2.0"
    bodies = {
        "status": template("status.md").substitute(),
        "footer": template("footer.md").substitute(raw=RAW, license=license),
    }
    if repo.get("banner", True):
        bodies["header"] = template("header.md").substitute(
            href=repo.get("href", "https://captf.io/docs/"),
            banner=f"{RAW}/banners/{slug(repo)}.svg",
            alt=attr("alt", f"{repo['name']}: {repo['tagline']}"),
            badges=badges(repo),
        )
    return bodies


def sync_readme(text, bodies):
    """Return text with every known block's body replaced, and unknown names."""
    unknown = []

    def replace(m):
        name = m["name"]
        if name not in bodies:
            unknown.append(name)
            return m[0]
        return m["open"] + bodies[name].rstrip("\n") + "\n" + m["close"]

    return BLOCK.sub(replace, text), unknown


def update(path, content, check, stale):
    old = path.read_text() if path.exists() else None
    if old == content:
        return
    stale.append(path)
    if not check:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if anything is stale")
    ap.add_argument(
        "--workspace",
        type=pathlib.Path,
        default=CHECKOUT.parent,
        help="directory holding the checkouts (default: %(default)s)",
    )
    ap.add_argument("repos", nargs="*", help="limit to these repositories")
    args = ap.parse_args()

    repos = tomllib.loads((HERE / "repos.toml").read_text())["repo"]
    if args.repos:
        missing = set(args.repos) - {r["name"] for r in repos}
        if missing:
            sys.exit(f"not in repos.toml: {', '.join(sorted(missing))}")
        repos = [r for r in repos if r["name"] in args.repos]

    stale, failed = [], False
    for repo in repos:
        if repo.get("banner", True):
            update(BANNERS / f"{slug(repo)}.svg", banner(repo), args.check, stale)

        checkout = CHECKOUT if repo["name"] == ".github" else args.workspace / repo.get("dir", repo["name"])
        readmes = repo.get("readme", "README.md")
        for rel in [readmes] if isinstance(readmes, str) else readmes:
            readme = (checkout / rel).resolve()
            if not readme.exists():
                print(f"skip {repo['name']}: no {readme}")
                continue
            text, unknown = sync_readme(readme.read_text(), fragments(repo))
            for name in unknown:
                print(f"{readme}: unknown block captf:{name} (have {', '.join(FRAGMENTS)})")
                failed = True
            update(readme, text, args.check, stale)

    for path in stale:
        print(("stale " if args.check else "wrote ") + str(path))
    sys.exit(1 if failed or (args.check and stale) else 0)


if __name__ == "__main__":
    main()
