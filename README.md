<h1 align="center">
  <a href="https://captf.io/"><img
    src="https://captf.io/assets/readme/mark.svg"
    width="72" height="72" alt="CAPTF"></a>
  <br>
  .github
</h1>

<p align="center">The org profile and community health files for CAPTF</p>

<p align="center">
  <a href="https://github.com/captf-io/.github/actions/workflows/checks.yml"><img
    src="https://img.shields.io/github/actions/workflow/status/captf-io/.github/checks.yml?branch=main&amp;label=build&amp;labelColor=161B3A&amp;style=flat-square"
    alt="build"></a>
  <a href="https://captf.io/docs/module-author/contract/index.html"><img
    src="https://img.shields.io/static/v1?label=contract&amp;message=v1alpha1&amp;color=A974FF&amp;labelColor=161B3A&amp;style=flat-square"
    alt="contract v1alpha1"></a>
  <a href="https://captf.io/docs/"><img
    src="https://img.shields.io/static/v1?label=docs&amp;message=captf.io&amp;color=5B8CFF&amp;labelColor=161B3A&amp;style=flat-square"
    alt="docs captf.io"></a>
  <a href="https://github.com/captf-io/.github/blob/main/LICENSE.md"><img
    src="https://img.shields.io/static/v1?label=license&amp;message=Apache-2.0&amp;color=FFD84D&amp;labelColor=161B3A&amp;style=flat-square"
    alt="license Apache-2.0"></a>
</p>

> [!NOTE]
> **Pre-release.** CAPTF is `v1alpha1`: its API and its
> [module contract](https://captf.io/docs/module-author/contract/index.html)
> may still change between releases.

The organization-wide files for [CAPTF](https://captf.io/), Cluster API
Provider Terraform: the profile shown at
[github.com/captf-io](https://github.com/captf-io) and the community health
files each `captf-io` repository carries a copy of.

| Path | Holds |
| --- | --- |
| [`profile/`](profile) | The org profile README, and its hero and how-it-works diagram in `assets/` |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to propose a change, and the commit message style |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | The Contributor Covenant, which every space of the project follows |
| [`SECURITY.md`](SECURITY.md) | How to report a vulnerability privately, and what is in scope |
| [`LICENSE.md`](LICENSE.md) | The Apache License 2.0 |
| [`CODEOWNERS`](CODEOWNERS) | Who reviews changes |
| [`.github/`](.github) | The issue forms (bug, feature, question) and the pull request template |

## Community health files

Every `captf-io` repository carries its own copy of `CONTRIBUTING.md`,
`CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE.md`, `CODEOWNERS` and
`.github/pull_request_template.md`. The copies here are the canonical ones:
change a file here first, then copy it into every other repository. GitHub
uses the issue forms and the pull request template here for every
repository that has none of its own.

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

## READMEs

Every README in the organization, this one included, is composed from the
same [README
components](https://captf.io/docs/developer-guide/readme-components/): a
header, a badge row, a status note and a footer. Their sources and images
live in the website repository. Nothing generates or syncs them: copy a
component from that page and fill in its placeholders.

<br>
<p align="center">
  <img
    src="https://captf.io/assets/readme/divider.svg"
    width="100%" height="4" alt="">
</p>
<p align="center">
  <a href="https://captf.io/"><img
    src="https://captf.io/assets/readme/mark.svg"
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
    <a href="https://github.com/captf-io/.github/blob/main/LICENSE.md"
    >Apache 2.0</a>.</sub>
</p>
