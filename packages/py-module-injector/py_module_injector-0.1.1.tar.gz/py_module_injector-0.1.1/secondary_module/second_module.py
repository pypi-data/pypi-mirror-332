class Provider:
    def __init__(self, log):
        self._log = log

    def set_log(self, log):
        self._log = log

    def get(self):
        return self._log

class SecondaryModule:
    def __init__(self):
        print(self.__module__)