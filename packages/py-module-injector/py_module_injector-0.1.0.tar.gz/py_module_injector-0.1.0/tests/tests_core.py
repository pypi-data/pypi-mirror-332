import unittest
from python_module import Inject, Module, Injector

class Provider:
    _log = "Provider Injetado"

    @classmethod
    def set_log(cls, log):
        cls._log = log
        return cls

    def get(self):
        return self._log

@Inject
class Service:
    def __init__(self, provider: Provider):
        self.provider = provider

    def get_log(self):
        return self.provider.get()

    def process(self):
        return 'Service processed'

@Module(
    instances=[Provider.set_log("Log Alterado")]
)
class ModuleTest:
    def __init__(self):
        pass

    def run(self):
        service = Service()
        return service.process()

class TestDependencyInjection(unittest.TestCase):
    def test_module_registration(self):
        module = ModuleTest()
        self.assertEqual(module.run(), 'Service processed')

    def test_provider_injection(self):
        provider = Provider()
        self.assertEqual(provider.get(), "Log Alterado")

    def test_service_injection(self):
        service = Service()
        self.assertEqual(service.get_log(), "Log Alterado")


    def test_injector_registration(self):
        ModuleTest()
        self.assertIsInstance(Injector.get('ModuleTest', 'Provider'), Provider)

if __name__ == '__main__':
    unittest.main()
