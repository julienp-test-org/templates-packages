# ${PROJECT}

${DESCRIPTION}

This is a [Pulumi component package](https://www.pulumi.com/docs/iac/concepts/components/)
written in Python. It exposes one or more `pulumi.ComponentResource` types
that can be consumed from any Pulumi language.

## Develop

The recommended toolchain uses [`uv`](https://docs.astral.sh/uv/), but a
classic virtualenv works too. To install dependencies:

```sh
uv sync
```

Edit `component/component.py` to define the inputs, outputs, and child
resources of your component. The class defined there is the component
implementation; its `super().__init__(...)` call's first argument
(`${PROJECT}:index:MyComponent`) is the type token consumers will see.

## Test

Inside any Pulumi program, add this package as a local dependency:

```sh
pulumi package add <path-to-this-directory>
```

Then run `pulumi up` against the program to exercise your component end to
end. Iterate by editing the component, re-running `pulumi up`, and observing
the resulting plan.

See the [component package docs](https://www.pulumi.com/docs/iac/guides/building-extending/components/packaging-components/)
for more on consuming your component from TypeScript, Go, .NET, and other
languages.
