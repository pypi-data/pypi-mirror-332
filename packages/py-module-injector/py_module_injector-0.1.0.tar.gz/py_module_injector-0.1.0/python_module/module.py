from ast import TypeVar
from typing import List, Type
from .injector_instance import Injector
from ._logger import Logger

logger = Logger()

T = TypeVar('T')

def Module(*, module_name: str = None, instances: List[Type] = []) -> Type:
    """
    Module decorator for registering instances in the dependency injector.

    Parameters:
        module_name (str, optional):
            - Name of the module to be registered in the injector.
            - If not provided, the class name (`cls.__name__`) will be used as the default.

        instances (list):
            - List of instances or providers to be registered in the module.
            - Example: `[Provider.set_log("Custom log message")]`

    Usage Example:
        @Module(
            module_name="ExampleModule",
            instances=[Provider.set_log("Log updated!")]
        )
        class ExampleModule:
            def run(self):
                service = Service()
                return service.process()

        if __name__ == '__main__':
            example_module = ExampleModule()
            print(example_module.run())
    """

    def decorator(cls):
        def __init__(self, *args, **kwargs):
            nonlocal module_name  # Ensure module_name is properly referenced
            if not module_name:
                module_name = cls.__name__
            if not (instances and len(instances)):
                raise ValueError('Instances are required')
            for instance in instances:
                Injector.register_instance(instance.__name__, instance, module_name)
                logger.success(f'✅ Instance registered {instance.__name__}')
            super(cls, self).__init__(*args, **kwargs)
        cls.__init__ = __init__
        return cls
    return decorator