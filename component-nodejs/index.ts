import * as pulumi from "@pulumi/pulumi";

export interface MyComponentArgs {
    /** A required input string. */
    input: pulumi.Input<string>;
}

/**
 * MyComponent is an example component resource. Replace its inputs, outputs,
 * and child resources with your own.
 */
export class MyComponent extends pulumi.ComponentResource {
    /** An example output computed from the input. */
    public readonly output: pulumi.Output<string>;

    constructor(name: string, args: MyComponentArgs, opts?: pulumi.ComponentResourceOptions) {
        super("${PROJECT}:index:MyComponent", name, args, opts);

        this.output = pulumi.output(args.input).apply(s => `Hello, ${s}!`);

        this.registerOutputs({
            output: this.output,
        });
    }
}
