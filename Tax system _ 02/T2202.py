from abc import ABC

from TaxForm import TaxForm


class T2202(TaxForm, ABC):
    def __init__(self, organization_name, sin_number, tax_payer_name, year, tuition):
        self.__school_name = str(organization_name).lower() + "t2202"
        self.__sin_number = str(sin_number)
        self.__tax_payer_name = str(tax_payer_name).lower()
        self.__year = str(year)
        self.__tuition = tuition

    def get_organization_name(self):
        return self.__school_name

    def get_sin_number(self):
        return self.__sin_number

    def get_tax_payer_name(self):
        return self.__tax_payer_name

    def get_year(self):
        return self.__year

    def get_Income(self):
        return 0.001

    def get_tax_credit(self):
        return self.__tuition * 0.15

    def __hash__(self) -> int:
        return hash(self.__school_name) + hash(self.__tax_payer_name) + hash(self.__sin_number) + hash(self.__year) + 43

    def __eq__(self, o: object) -> bool:
        return self.__class__ == o.__class__ and self.__hash__() == o.__hash__()

    def __str__(self) -> str:
        return self.__tax_payer_name + " go to " + self.__school_name + " and paid " + str(
            self.__tuition) + " in " + self.__year + " school year."
