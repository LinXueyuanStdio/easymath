from abc import ABCMeta, abstractmethod

class Limit(metaclass=ABCMeta):
    @abstractmethod
    def definition(self, N="N", n="n", distence=r"||", limit="a"):
        pass

    @abstractmethod
    def _definition(self, varepsilon=r"\varepsilon", N="N", n="n", distence=r"||", limit="a"):
        pass
