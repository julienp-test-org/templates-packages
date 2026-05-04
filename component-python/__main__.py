from pulumi.provider.experimental import component_provider_host

from component import MyComponent

if __name__ == "__main__":
    component_provider_host([MyComponent], "${PROJECT}")
