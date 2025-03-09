class InstanceInjector:
    def __init__(self):
        self._modules = {}

    def set_module(self):
        return {
            "_instances": {},
        }

    def register_instance(self, name, instance, module_name):
        if module_name not in self._modules:
            self._modules[module_name] = self.set_module()
        self._modules[module_name]["_instances"][name] = instance()

    def get(self, module_name, name):
        if not module_name:
            if not self._modules:
                raise ValueError("No modules have been registered yet.")
            # Pega o último módulo registrado
            module_name = list(self._modules.keys())[-1]

        if module_name not in self._modules:
            raise ValueError(f"Module ({module_name}) not found")

        module = self._modules[module_name]

        if name in module["_instances"]:
            return module["_instances"][name]

        raise ValueError(
            f"Instance or provider ({name}) not found in module ({module_name})"
        )