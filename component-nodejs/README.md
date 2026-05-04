# ${PROJECT}

${DESCRIPTION}

This is a [Pulumi component package](https://www.pulumi.com/docs/iac/concepts/components/)
written in TypeScript. It exposes one or more `pulumi.ComponentResource` types
that can be consumed from any Pulumi language.

## Develop

Install dependencies:

```sh
npm install
```

Edit `index.ts` to define the inputs, outputs, and child resources of your
component. The class exported from `index.ts` is the component implementation;
its `super(...)` call's first argument (`${PROJECT}:index:MyComponent`) is the
type token consumers will see.

Type-check the package locally:

```sh
npm run typecheck
```

## Test

Inside any Pulumi program, add this package as a local dependency:

```sh
pulumi package add <path-to-this-directory>
```

Then run `pulumi up` against the program to exercise your component end to
end. Iterate by editing the component, re-running `pulumi up`, and observing
the resulting plan.

See the [component package docs](https://www.pulumi.com/docs/iac/guides/building-extending/components/packaging-components/)
for more on consuming your component from Python, Go, .NET, and other
languages.
