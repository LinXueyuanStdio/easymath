from .definition import Limit

class Sequence(Limit):
    def __init__(self, symbol="x"):
        self.symbol = symbol
    
    def definition(self, N="N", n="n", distence=r"||", limit="a"):
        return r"$\forall \varepsilon > 0,"+r" \exists "+N+" > 0,"+r" \forall "+n+" > "+N+",$\n"+"$"+distence+self.symbol+"_"+n+" - "+limit+distence+r"< \varepsilon$"
    
    def _definition(self, varepsilon=r"\varepsilon", N="N", n="n", distence=r"||", limit="a"):
        return r"$\exists "+varepsilon+" > 0,"+r" \forall "+N+" > 0,"+r" \exists "+n+" > "+N+",$\n"+"$"+distence+self.symbol+"_"+n+" - "+limit+distence+r"\geqslant \varepsilon$"
