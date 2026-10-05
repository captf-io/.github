<!-- captf:header -->
<h1 align="center">
  <a href="https://github.com/captf-io"><img
    src="https://raw.githubusercontent.com/captf-io/.github/refs/heads/main/readme/banners/github.svg"
    width="100%"
    alt=".github: The org profile and community health files for CAPTF"></a>
</h1>
<p align="center">
  <a href="https://captf.io/docs/module-author/contract/index.html"><img
    src="https://img.shields.io/static/v1?label=contract&amp;message=v1alpha1&amp;color=A974FF&amp;labelColor=161B3A&amp;style=flat-square"
    alt="contract v1alpha1"></a>
  <a href="https://captf.io/docs/"><img
    src="https://img.shields.io/static/v1?label=docs&amp;message=captf.io&amp;color=5B8CFF&amp;labelColor=161B3A&amp;style=flat-square"
    alt="docs captf.io"></a>
</p>
<!-- /captf:header -->

<!-- captf:status -->
> [!NOTE]
> **Pre-release.** CAPTF is `v1alpha1`: its API and its
> [module contract](https://captf.io/docs/module-author/contract/index.html)
> may still change before the first release.
<!-- /captf:status -->

The organization-wide files for [CAPTF](https://captf.io/), Cluster API
Provider Terraform: the profile shown at
[github.com/captf-io](https://github.com/captf-io), the community health
files each `captf-io` repository carries a copy of, and the fragments that give
each repository's README the same header and footer.

| Path | Holds |
| --- | --- |
| [`profile/`](profile) | The org profile README, and its hero and how-it-works diagram in `assets/` |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to propose a change, and the commit message style |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | The Contributor Covenant, which every space of the project follows |
| [`SECURITY.md`](SECURITY.md) | How to report a vulnerability privately, and what is in scope |
| [`.github/`](.github) | The issue forms (bug, feature, question) and the pull request template |
| [`readme/`](readme) | The README fragments: banners, header, status note, footer and `sync.py` |

## Community health files

Every `captf-io` repository carries its own `CONTRIBUTING.md`,
`SECURITY.md` and `CODE_OF_CONDUCT.md` at its root. GitHub uses the
issue forms and the pull request template here for every repository that
has none of its own. Keep the copies of the three files in step with the
ones here.

Blank issues are off: an issue starts from a form, and the chooser points
vulnerability reports at `SECURITY.md` and questions at the
[docs](https://captf.io/docs/).

## The profile

[`profile/README.md`](profile/README.md) is the page at
[github.com/captf-io](https://github.com/captf-io). It loads its images
from `main` of this repository, so they change when a commit lands.

The landing page at [captf.io](https://captf.io/) shares its copy and its
diagram, [`profile/assets/how-it-works.svg`](profile/assets/how-it-works.svg),
with the profile. Change them in both repositories together.

## README fragments

Every README in the organization, this one included, opens with a banner
and badges and ends with the same footer. They live in
[`readme/`](readme), which documents the README layout and the rules for
the text between them.

```sh
make readme          # render the banners and sync the README blocks
make readme-check    # fail if a banner or a block is out of date
```

Both work on a directory holding the `captf-io` checkouts side by side,
by default the parent of this one; set `WORKSPACE=<dir>` otherwise.

<!-- captf:footer -->
<br>
<p align="center">
  <img
    src="https://raw.githubusercontent.com/captf-io/.github/refs/heads/main/readme/assets/divider.svg"
    width="100%" height="4" alt="">
</p>
<p align="center">
  <a href="https://captf.io/"><img
    src="https://raw.githubusercontent.com/captf-io/.github/refs/heads/main/readme/assets/mark.svg"
    width="40" height="40" alt="CAPTF"></a>
  <br>
  <a href="https://captf.io/docs/"
    ><b>Documentation</b></a> ·
  <a href="https://captf.io/docs/getting-started/quick-start.html"
    ><b>Quick start</b></a> ·
  <a href="https://github.com/captf-io/.github/blob/main/CONTRIBUTING.md"
    ><b>Contributing</b></a> ·
  <a href="https://github.com/captf-io/.github/blob/main/SECURITY.md"
    ><b>Security</b></a>
  <br>
  <sub>Built for
    <a href="https://cluster-api.sigs.k8s.io/">Cluster API</a>.
    Apache 2.0.</sub>
</p>
<!-- /captf:footer -->
