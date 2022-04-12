from abc import ABC, abstractmethod


class TaxForm(ABC):

    @abstractmethod
    def __init__(self, organization_name, sin_number, tax_payer_name, year):
        self.__organization_name = organization_name
        self.__sin_number = sin_number
        self.__tax_payer_name = tax_payer_name
        self.__year = year

    @abstractmethod
    def get_organization_name(self):
        pass

    @abstractmethod
    def get_sin_number(self):
        pass

    @abstractmethod
    def get_tax_payer_name(self):
        pass

    @abstractmethod
    def get_year(self):
        pass

    @abstractmethod
    def get_Income(self):
        pass

    @abstractmethod
    def get_tax_credit(self):
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def __eq__(self, o: object) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


