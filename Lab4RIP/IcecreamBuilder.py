from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any
from Observer import StartIcecreamObserver, FinishIcecreamObserver,IcecreamObserver
from Facade import Facade
#from icecream_cafe.Observer import StartIcecreamObserver, FinishIcecreamObserver,IcecreamObserver
#from icecream_cafe.Facade import Facade

class Icecream():

    def __init__(self) -> None:
        self.cream = []
        self.syrop = []
        self.addition = []

    def set_cream(self, part: Any) -> None:
        self.cream.append(part)
    def set_syrop(self, part: Any) -> None:
        self.syrop.append(part)
    def set_addition(self, part: Any) -> None:
        self.addition.append(part)

    def list_parts(self) -> None:
        print(f"Base - "," ".join(self.cream))
        print(f"Syrop - "," ".join(self.syrop))
        print(f"Addition - "," ".join(self.addition))

class IcecreamBuilder(ABC):
    icecream_type = None

    @abstractproperty
    def icecream(self) -> None:
        pass

    @abstractmethod
    def produce_cream(self) -> None:
        pass

    @abstractmethod
    def produce_syrop(self) -> None:
        pass

    @abstractmethod
    def produce_addition(self) -> None:
        pass


class Type1IcecreamBuilder(IcecreamBuilder):

    def __init__(self) -> None:
        self.icecream_type = "Type 1 icecream"
        self.reset()

    def reset(self) -> None:
        self._icecream = Icecream()


    @property
    def icecream(self) -> Icecream:
        icecream = self._icecream
        self.reset()
        return icecream

    def produce_cream(self) -> None:
        self._icecream.set_cream("Plombir")

    def produce_syrop(self) -> None:
        self._icecream.set_syrop("Caramel")

    def produce_addition(self) -> None:
        self._icecream.set_addition("Crushed nuts")

class Type2IcecreamBuilder(IcecreamBuilder):

    def __init__(self) -> None:
        self.icecream_type = "Type 2 icecream"
        self.reset()

    def reset(self) -> None:
        self._icecream = Icecream()


    @property
    def icecream(self) -> Icecream:
        icecream = self._icecream
        self.reset()
        return icecream

    def produce_cream(self) -> None:
        self._icecream.set_cream("Creme brulee")

    def produce_syrop(self) -> None:
        self._icecream.set_syrop("Chocolate syrop")

    def produce_addition(self) -> None:
        self._icecream.set_addition("Cookies")


class Iceman:

    def __init__(self, name, start_observer, finish_observer) -> None:
        self._builder = None
        self.name = name
        self._start_icecream_observer = start_observer or StartIcecreamObserver()
        self._finish_icecream_observer = finish_observer or FinishIcecreamObserver()

    @property
    def builder(self) -> IcecreamBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: IcecreamBuilder) -> None:
        self._builder = builder
        self.notify(self._start_icecream_observer)

    def build_pure_icecream(self) -> None:
        self.builder.produce_cream()
        self.notify(self._finish_icecream_observer)

    def build_complex_icecream(self) -> None:
        self.builder.produce_cream()
        self.builder.produce_syrop()
        self.builder.produce_addition()
        self.notify(self._finish_icecream_observer)

    def notify(self, observer: IcecreamObserver) -> None:
        print("Waiter speaks:")
        observer.update(self)


if __name__ == "__main__":

    director1 = Iceman("Iceman1", None, None)
    builder1 = Type1IcecreamBuilder()
    director1.builder = builder1

    director2 = Iceman("Iceman2", None, None)
    builder2 = Type2IcecreamBuilder()
    director2.builder = builder2

    icemans = Facade(director1, director2)
    icemans.iceman1_operation()
    icemans.iceman2_operation()

    print("-------------------------------------------------------------")
    director = Iceman("Iceman1", None, None)
    builder = Type1IcecreamBuilder()
    director.builder = builder

    print("Basic icecream: ")
    director.build_pure_icecream()

    print("\n")

    print("Complex icecream: ")
    director.build_complex_icecream()

    print("\n")

    print("Custom icecream: ")
    builder.produce_cream()
    builder.produce_syrop()
    builder.icecream.list_parts()

    print("\n")