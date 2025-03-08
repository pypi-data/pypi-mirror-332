import inspect
from functools import wraps

from .injector_instance import Injector
from ._logger import Logger

logger = Logger()


def Inject(target=None, module_name: str = None):
    """
    Decorator to inject dynamic dependencies into classes and __init__ methods.

    Parameters:
        target:
            - The target class where dependencies will be injected.
            - If used on an __init__ method, it applies dependency injection to its parameters.

        module_name (str, optional):
            - Name of the module from which dependencies should be resolved.
            - If not provided, the last registered module will be used as the default.

    Usage Example:

        @Inject(module_name="ModuleExemple")
        class ServiceBase:
            def __init__(self, provider: Provider):
                self.provider = provider

            def get_log(self):
                return self.provider.get()



        @Inject(module_name="ModuleExemple")
        class ServiceBase:
            def __init__(self, provider: Provider):
                self.provider = provider

            def get_log(self):
                return self.provider.get()
    """

    if inspect.isclass(target):
        # Se for uma classe, aplicamos a injeção no __init__
        original_init = target.__init__

        @wraps(original_init)
        def wrapped_init(self, *args, **kwargs):
            # Debug
            logger.warning(f"🔹 Starting injection on class ({target.__name__})...")
            injected_kwargs = {}

            # Obtém a assinatura do __init__
            init_signature = inspect.signature(original_init)
            for name, param in init_signature.parameters.items():
                if name == "self":
                    continue
                if name not in kwargs:
                    type_hint = param.annotation
                    if type_hint != param.empty:
                        instance = Injector.get(
                            module_name, type_hint.__name__)
                        if instance:
                            injected_kwargs[name] = instance
                            logger.success(
                                f"✅ Instance {name} ({type_hint.__name__}) injected in {target.__name__}")

            # Atualiza kwargs com os valores injetados
            kwargs.update(injected_kwargs)
            original_init(self, *args, **kwargs)  # Chama o __init__ original

        # Substitui o __init__ original pela versão modificada
        target.__init__ = wrapped_init
        return target  # Retorna a classe modificada

    elif callable(target):
        # Se for um método, aplicamos a injeção apenas nele
        @wraps(target)
        def wrapped_function(self, *args, **kwargs):
            # Debug
            logger.warning(f"🔹 Starting injection on method ({target.__name__})...")
            injected_kwargs = {}

            # Obtém a assinatura da função
            func_signature = inspect.signature(target)
            for name, param in func_signature.parameters.items():
                if name == "self":
                    continue
                if name not in kwargs:
                    type_hint = param.annotation
                    if type_hint != param.empty:
                        instance = Injector.get(
                            module_name, type_hint.__name__)
                        if instance:
                            injected_kwargs[name] = instance
                            logger.error(
                                f"✅ Instance {name} ({type_hint.__name__}) injected in {target.__name__}")

            # Atualiza kwargs com os valores injetados
            kwargs.update(injected_kwargs)
            return target(self, *args, **kwargs)  # Chama a função original

        return wrapped_function  # Retorna a função modificada

    else:
        # Caso o decorador seja chamado sem argumentos (ex: @Inject)
        def wrapper(inner_target):
            return Inject(inner_target, module_name=module_name)

        return wrapper