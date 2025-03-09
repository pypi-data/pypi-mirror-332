import python_module as p_m
from ..second_module import Provider

@p_m.Inject
class TerciaryModule:
    def __init__(self, provider: Provider):
        self.provider = provider
        print(self.provider.get())
