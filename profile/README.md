<p align="center">
  <a href="https://docs.captf.io/">
    <img src="https://raw.githubusercontent.com/captf-io/.github/refs/heads/main/profile/assets/hero.svg" width="100%" alt="CAPTF: your modules are the provider. Turn the Terraform and OpenTofu you already trust into Kubernetes clusters, on any platform.">
  </a>
</p>

<p align="center">
  <a href="https://docs.captf.io/"><img src="https://img.shields.io/badge/Read_the_docs-docs.captf.io-5B8CFF?style=for-the-badge&logo=mdbook&logoColor=white" alt="Read the docs"></a>
  <a href="https://docs.captf.io/getting-started/quick-start.html"><img src="https://img.shields.io/badge/Quick_start-try_it-A974FF?style=for-the-badge" alt="Quick start"></a>
</p>
<p align="center">
  <a href="https://cluster-api.sigs.k8s.io/"><img src="https://img.shields.io/badge/Cluster_API-infrastructure_provider-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Cluster API infrastructure provider"></a>
  <a href="https://opentofu.org/"><img src="https://img.shields.io/badge/OpenTofu-supported-FFDA18?style=flat-square&logo=opentofu&logoColor=black" alt="OpenTofu supported"></a>
  <a href="https://developer.hashicorp.com/terraform"><img src="https://img.shields.io/badge/Terraform-supported-7B42BC?style=flat-square&logo=terraform&logoColor=white" alt="Terraform supported"></a>
  <img src="https://img.shields.io/badge/License-Apache_2.0-4ADE80?style=flat-square" alt="Apache 2.0 license">
</p>

<br>

<h2 align="center">Stop writing a new provider for every platform.</h2>

<p align="center">
  Cluster API needs an infrastructure provider for every platform you run on,<br>
  and you already have the Terraform that builds it. <b>CAPTF makes that module the provider.</b><br>
  No Go controller to write. No second copy of your infrastructure logic to keep in sync.
</p>

<br>

<p align="center">
  <img src="https://raw.githubusercontent.com/captf-io/.github/refs/heads/main/profile/assets/how-it-works.svg" width="100%" alt="How it works: write a Terraform or OpenTofu module, package it as an OCI image, CAPTF runs it as Kubernetes Jobs, and Cluster API gets a real cluster.">
</p>

<br>

## Why teams reach for CAPTF

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>Any platform</h3>
      <p>If Terraform or OpenTofu can provision it, CAPTF can build a cluster on it: public cloud, private cloud, bare metal, or the libvirt box under your desk.</p>
    </td>
    <td width="33%" valign="top">
      <h3>Zero Go</h3>
      <p>Your module is the provider. CAPTF runs it, reads its outputs from state, and reconciles <code>Cluster</code>, <code>Machine</code> and <code>MachinePool</code> against them.</p>
    </td>
    <td width="33%" valign="top">
      <h3>The whole Cluster API</h3>
      <p>Clusters, machines and autoscaled machine pools. ClusterClass. Kubeadm and RKE2 control planes. <code>clusterctl move</code>.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h3>State that lives with the cluster</h3>
      <p>Terraform state is stored in Kubernetes Secrets next to the object it belongs to, and backed up. There's no bucket to create and no backend to wire up.</p>
    </td>
    <td valign="top">
      <h3>Drift, caught</h3>
      <p>Scheduled drift checks and your module's own health outputs feed Cluster API conditions and machine remediation, so problems come to you.</p>
    </td>
    <td valign="top">
      <h3>Guardrails built in</h3>
      <p>Plan approval before apply. Credentials scoped to the namespaces you name. Locked-down Jobs, with privilege escalation rejected at admission.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h3>Lint before you ship</h3>
      <p><code>tfcapi-lint</code> checks your module and its image against the contract before a cluster ever sees them.</p>
    </td>
    <td valign="top">
      <h3>Operable on day one</h3>
      <p>Prometheus metrics and alerts, documented conditions and events, and runbooks for failing Jobs, stuck destroys, stale locks and more.</p>
    </td>
    <td valign="top">
      <h3>A supply chain you can audit</h3>
      <p>Multi-arch OpenTofu and Terraform base images, rebuilt weekly, shipped with SBOMs and provenance attestations.</p>
    </td>
  </tr>
</table>

## From module to cluster in two moves

Package the module you already have on one of our base images, using its example <code>Dockerfile</code>:

```sh
podman build --build-arg ROLE=machine -t registry.example.com/acme/machine:v1.0.0 .
```

Then point Cluster API at it:

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1alpha1
kind: TerraformMachineTemplate
metadata:
  name: acme
spec:
  template:
    spec:
      source:
        image: registry.example.com/acme/machine:v1.0.0
```

That's the core of it: every machine stamped from that template is now built by your module.
[Your First Module](https://docs.captf.io/getting-started/first-module.html) walks through it end to end.

> [!TIP]
> **Get in early.** CAPTF is `v1alpha1` and pre-release, and its module contract is still open to change.
> If you have Terraform that builds clusters, this is the moment to shape how CAPTF runs it.
> Try the [Quick Start](https://docs.captf.io/getting-started/quick-start.html), then open an issue and tell us what your platform needs.

## Explore

- **[cluster-api-provider-terraform](https://github.com/captf-io/cluster-api-provider-terraform)**: the provider, with its manager, runner, `tfcapi-lint` and reference modules.
- **[docs](https://github.com/captf-io/docs)**: the book behind [docs.captf.io](https://docs.captf.io/).
- **[opentofu-base](https://github.com/captf-io/opentofu-base)**: `ghcr.io/captf-io/opentofu-base`, the base image for OpenTofu modules.
- **[terraform-base](https://github.com/captf-io/terraform-base)**: `ghcr.io/captf-io/terraform-base`, the base image for Terraform modules.

<br>

<p align="center">
  <a href="https://docs.captf.io/"><b>Documentation</b></a> ·
  <a href="https://github.com/captf-io/.github/blob/main/CONTRIBUTING.md"><b>Contributing</b></a> ·
  <a href="https://github.com/captf-io/.github/blob/main/SECURITY.md"><b>Security</b></a>
  <br><br>
  <sub>Built for <a href="https://cluster-api.sigs.k8s.io/">Cluster API</a>. Apache 2.0.</sub>
</p>
