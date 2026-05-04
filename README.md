# Pulumi Package Templates

This repo contains the templates for `pulumi package new`, which scaffolds a
new [Pulumi package](https://www.pulumi.com/docs/iac/concepts/packages/).
After running `pulumi package new`, edit the generated sources to implement
your package.

## Available templates

| Template | Language |
| --- | --- |
| `component-nodejs` | TypeScript on Node.js |
| `component-python` | Python |

## Adding a new template

1. Create a new directory for the template at the root of this repo. By
   convention the language is included as a suffix, e.g. `component-go`.
2. Add a `PulumiPlugin.yaml` declaring the runtime and a `template:` block
   describing the template. The `template:` block is removed from the manifest
   when the template is instantiated.
3. Add the language-specific scaffolding for the package. `${PROJECT}` and
   `${DESCRIPTION}` placeholders in any non-binary file are substituted with
   the user-supplied package name and description at instantiation time.
4. Add a `README.md` that walks the user through developing and testing
   their package.
