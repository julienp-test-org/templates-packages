from typing import Optional, TypedDict

import pulumi


class MyComponentArgs(TypedDict):
    """Arguments accepted by MyComponent."""

    input: pulumi.Input[str]


class MyComponent(pulumi.ComponentResource):
    """An example component resource. Replace its inputs, outputs, and child
    resources with your own."""

    output: pulumi.Output[str]
    """An example output computed from the input."""

    def __init__(
        self,
        name: str,
        args: MyComponentArgs,
        opts: Optional[pulumi.ResourceOptions] = None,
    ):
        super().__init__("${PROJECT}:index:MyComponent", name, {}, opts)

        self.output = pulumi.Output.from_input(args["input"]).apply(
            lambda s: f"Hello, {s}!"
        )

        self.register_outputs({"output": self.output})
