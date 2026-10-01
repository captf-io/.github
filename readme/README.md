# README fragments

The shared header, status note and footer that every captf-io README and
the org profile carry, so the repositories look like one project and like
<https://captf.io/>. They are drawn from the same sources as the site: the
colours of `assets/css/main.css` in captf-io.github.io, and the hero and
diagram in `profile/assets/`.

A README holds each fragment between two markers, and
[`sync.py`](sync.py) fills them in. Never edit inside the markers; edit
the template here and sync.

## The fragments

| Block | Holds | Goes |
| --- | --- | --- |
| `header` | The repository's banner, linked to the docs, and a badge row: build, contract, docs, licence | First line of the README. The banner is the `<h1>`, so the README has no `# title` |
| `status` | The pre-release note: `v1alpha1`, the contract may change | Right under the header. Remove the markers from every README at the first release |
| `footer` | A gradient divider, the CAPTF mark, the site footer's links, the licence | Last thing in the README. It replaces a `## License` section |

The banner is a 1200×260 card in the hero's style: the repository's name in
the purple-blue-yellow gradient, its tagline, an eyebrow with its kind, and
a glyph from the how-it-works diagram. Like the hero it is dark in both
GitHub themes, and its animations stop under `prefers-reduced-motion`.

| Glyph | Drawn as | For |
| --- | --- | --- |
| `job` | The Job wheel (diagram step 03) | The provider |
| `image` | Stacked layers (step 02) | Base images |
| `module` | `.tf` with a cursor (step 01) | Module repositories |
| `cluster` | Four nodes and a check (step 04) | Unused, kept for a cluster-shaped repository |
| `book` | An open book | The docs |
| `site` | A browser window round the mark | The website |
| `mark` | The CAPTF hexagon and dot | Anything else |

## The README skeleton

```markdown
<!-- captf:header -->
<!-- /captf:header -->

<!-- captf:status -->
<!-- /captf:status -->

One paragraph: what this repository is and where it sits in CAPTF.

## Using it

## Developing

## Releasing

<!-- captf:footer -->
<!-- /captf:footer -->
```

The middle is the repository's own. Keep to these rules so the pages read
the same:

- Name the sections with gerunds where they fit: `Using…`, `Building…`,
  `Developing`, `Releasing`.
- Style the body with plain Markdown only: tables, fenced code with a
  language, and GitHub alerts (`[!NOTE]`, `[!TIP]`, `[!WARNING]`). The
  fragments carry all of the brand's images, colour and HTML.
- No emoji, and no badges outside the header.
- Write prose in the docs' house style: plain, direct, present tense.
- Keep lines within 80 columns; the fragments do, so markdownlint's
  `MD013` and `MD041` pass where a repository runs it.

## Adding a repository

1. Add a `[[repo]]` entry to [`repos.toml`](repos.toml): its kind, glyph
   and a tagline of at most 60 characters. Add `ci` once the repository
   is public, since the build badge needs a public repository.
2. Run `make readme`, which writes `banners/<repo>.svg`. Commit it here
   and push it first: READMEs load the banners and assets from `main` of
   this repository.
3. Paste the skeleton's markers into the repository's README, run
   `make readme` again, and commit the README in that repository.

## Changing a fragment

Edit [`templates/`](templates) or [`assets/`](assets), then run
`make readme` from this checkout with the other checkouts beside it, or
point it at them with `WORKSPACE=<dir>`. Commit the banners and templates
here, then the README in each repository it changed.
`make readme-check` writes nothing and fails if a banner or a README
block is out of date.

## Layout

| Path | Holds |
| --- | --- |
| `repos.toml` | Every repository that carries the fragments, and its banner text |
| `sync.py` | Renders the banners and fills each README's blocks; Python 3.11+, standard library only |
| `templates/banner.svg` | The banner, with `${…}` placeholders |
| `templates/glyphs/` | The banner glyphs, drawn on a 120×120 tile centred on the origin |
| `templates/*.md` | The `header`, `status` and `footer` blocks |
| `assets/` | The footer's divider and mark |
| `banners/` | The rendered banners. Generated: run `make readme`, don't edit |
