# The directory holding the captf-io checkouts, for the README fragments
# (readme/README.md). The .github repository itself is always this checkout.
WORKSPACE ?= ..

.PHONY: help readme readme-check

help: ## Show targets.
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F ':.*## ' '{printf "%-16s %s\n", $$1, $$2}'

readme: ## Render the banners and sync the fragments into every README in WORKSPACE.
	PYTHONDONTWRITEBYTECODE=1 python3 readme/sync.py --workspace $(WORKSPACE)

readme-check: ## Fail if a banner or a README block in WORKSPACE is out of date.
	PYTHONDONTWRITEBYTECODE=1 python3 readme/sync.py --check --workspace $(WORKSPACE)
