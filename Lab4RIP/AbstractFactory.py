from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractAirport(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    различные абстрактные продукты. Эти продукты называются семейством и связаны
    темой или концепцией высокого уровня. Продукты одного семейства обычно могут
    взаимодействовать между собой. Семейство продуктов может иметь несколько
    вариаций, но продукты одной вариации несовместимы с продуктами другой.
    """
    @abstractmethod
    def create_cargo_plane(self) -> AbstractСargoPlane:
        pass

    @abstractmethod
    def create_passenger_plane(self) -> AbstractPassengerPlane:
        pass


class ConcreteAirport1(AbstractAirport):
    """
    Конкретная Фабрика производит семейство продуктов одной вариации. Фабрика
    гарантирует совместимость полученных продуктов. Обратите внимание, что
    сигнатуры методов Конкретной Фабрики возвращают абстрактный продукт, в то
    время как внутри метода создается экземпляр конкретного продукта.
    """

    def create_cargo_plane(self) -> AbstractСargoPlane:
        return ConcreteСargoPlane1()

    def create_passenger_plane(self) -> AbstractPassengerPlane:
        return ConcretePassengerPlane1()


class ConcreteAirport2(AbstractAirport):
    """
    Каждая Конкретная Фабрика имеет соответствующую вариацию продукта.
    """

    def create_cargo_plane(self) -> AbstractСargoPlane:
        return ConcreteСargoPlane2()

    def create_passenger_plane(self) -> AbstractPassengerPlane:
        return ConcretePassengerPlane2()


class AbstractСargoPlane(ABC):
    """
    Каждый отдельный продукт семейства продуктов должен иметь базовый интерфейс.
    Все вариации продукта должны реализовывать этот интерфейс.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Конкретные продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteСargoPlane1(AbstractСargoPlane):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteСargoPlane2(AbstractСargoPlane):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractPassengerPlane(ABC):
    """
    Базовый интерфейс другого продукта. Все продукты могут взаимодействовать
    друг с другом, но правильное взаимодействие возможно только между продуктами
    одной и той же конкретной вариации.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Продукт B способен работать самостоятельно...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractСargoPlane) -> None:
        """
        ...а также взаимодействовать с Продуктами A той же вариации.

        Абстрактная Фабрика гарантирует, что все продукты, которые она создает,
        имеют одинаковую вариацию и, следовательно, совместимы.
        """
        pass


"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcretePassengerPlane1(AbstractPassengerPlane):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    Продукт B1 может корректно работать только с Продуктом A1. Тем не менее, он
    принимает любой экземпляр Абстрактного Продукта А в качестве аргумента.
    """

    def another_useful_function_b(self, collaborator: AbstractСargoPlane) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcretePassengerPlane2(AbstractPassengerPlane):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractСargoPlane):
        """
        Продукт B2 может корректно работать только с Продуктом A2. Тем не менее,
        он принимает любой экземпляр Абстрактного Продукта А в качестве
        аргумента.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(airport: AbstractAirport) -> None:
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    product_a = airport.create_cargo_plane()
    product_b = airport.create_passenger_plane()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteAirport1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteAirport2())