from __future__ import annotations
#from icecream_cafe.IcecreamBuilder import Iceman

class Facade:

    def __init__(self, iceman1: Iceman, iceman2: Iceman) -> None:
        self.iceman1 = iceman1
        self.iceman2 = iceman2

    def iceman1_operation(self) -> None:

        print("Basic icecream: ")
        self.iceman1.build_pure_icecream()

        print("\n")

        print("Complex icecream: ")
        self.iceman1.build_complex_icecream()

        print("\n")


    def iceman2_operation(self) -> None:
        print("Basic icecream: ")
        self.iceman2.build_pure_icecream()

        print("\n")

        print("Complex icecream: ")
        self.iceman2.build_complex_icecream()

        print("\n")
