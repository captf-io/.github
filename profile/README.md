# Cluster API Provider Terraform

CAPTF is a [Cluster API](https://cluster-api.sigs.k8s.io/) infrastructure
provider that runs your Terraform or OpenTofu modules as Kubernetes Jobs.
Package a module written to the CAPTF contract as an OCI image, and CAPTF
runs it, reads its outputs back from state, and reconciles `Cluster`,
`Machine` and `MachinePool` objects against them. There is no Go controller
to write for a new platform, and no second copy of infrastructure logic to
keep in sync with the module you already have.

**Status:** early. Every kind and the module contract are `v1alpha1`, and the
contract may still change before the first real module has provisioned a
cluster with it. There are no end-to-end tests yet.

## Start here

- **Documentation:** [docs.captf.io](https://docs.captf.io/), starting with
  the [Quick Start](https://docs.captf.io/getting-started/quick-start.html).
- **Writing a module:** the
  [Module Contract](https://docs.captf.io/module-author/contract/README.html).
- **Security model:** read
  [what a `Terraform*` object grants](https://docs.captf.io/concepts/security-model.html)
  before deciding who may create one.

## Repositories

| Repository | Holds |
| --- | --- |
| [cluster-api-provider-terraform](https://github.com/captf-io/cluster-api-provider-terraform) | The manager, the runner, `tfcapi-lint`, and the reference modules. |
| [docs](https://github.com/captf-io/docs) | The book published at [docs.captf.io](https://docs.captf.io/). |
| [opentofu-base](https://github.com/captf-io/opentofu-base) | `ghcr.io/captf-io/opentofu-base`, the base image for OpenTofu module images. |
| [terraform-base](https://github.com/captf-io/terraform-base) | `ghcr.io/captf-io/terraform-base`, the base image for Terraform module images. |

## Getting involved

Read [CONTRIBUTING.md](https://github.com/captf-io/.github/blob/main/CONTRIBUTING.md)
before opening a pull request. Report vulnerabilities privately, as described
in [SECURITY.md](https://github.com/captf-io/.github/blob/main/SECURITY.md),
never in a public issue.
