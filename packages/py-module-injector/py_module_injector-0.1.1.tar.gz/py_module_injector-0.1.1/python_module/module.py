import inspect
from typing import List, Type, TypeVar
from .typing import RegisterModuleType
from .injector_instance import Injector
from ._logger import Logger

logger = Logger()

T = TypeVar('T')

def get_decorator_calling_module():
    """
    Encontra o módulo onde o decorator foi usado.
    """
    stack = inspect.stack()
    for frame_info in stack:
        module = inspect.getmodule(frame_info.frame)
        if module and module.__name__ != __name__:  # Ignora o módulo onde o decorator foi definido
            return module.__name__
    return "__main__"


def Module(*, instances: List[RegisterModuleType] = []) -> Type:
    """
    Module decorator for registering instances in the dependency injector.

    Parameters:
        instances (list):
            - Lista de objetos `RegisterModuleType` a serem registrados no módulo.
            - Cada objeto `RegisterModuleType` pode conter:
                - `implementation`: Um dicionário com a chave sendo o nome da implementação e o valor sendo outro dicionário com a configuração dessa implementação.
                - `factory`: Uma função ou callable que será usada para criar instâncias dessa dependência.

    Usage Example:
        @Module(
            instances=[
                {
                    "implementation": Provider,
                    "factory": lambda: Provider(log="Provider Injetado")
                }
            ]
        )
        class ModuleExemple:
            def run(self):
                service = Service()
                return service.process()
    """

    calling_module_name = get_decorator_calling_module()

    def decorator(cls):
        def __init__(self, *args, **kwargs):
            module_name = calling_module_name
            if not (instances and len(instances)):
                raise ValueError('Instances are required')
            for instance in instances:
                implementation = instance.get("implementation", None)
                factory = instance.get("factory", None)
                if not implementation:
                    raise ValueError('Instance is required')
                Injector.register(implementation.__name__,
                                  implementation, module_name, factory)
                logger.success(
                    f'✅ Instance registered {implementation.__name__}')
            super(cls, self).__init__(*args, **kwargs)
        cls.__init__ = __init__
        return cls
    return decorator