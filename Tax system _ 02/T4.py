from abc import ABC

from TaxForm import TaxForm


class T4(TaxForm, ABC):
    def __init__(self, organization_name, sin_number, tax_payer_name, year, income, pre_deducted_tax):
        self.__company_name = str(organization_name).lower()+"t4"
        self.__sin_number = str(sin_number)
        self.__tax_payer_name = str(tax_payer_name).lower()
        self.__year = str(year)

        if income < 0:
            income = 0
        self.__income = income

        if pre_deducted_tax < 0:
            pre_deducted_tax = 0
        self.__pre_deducted_tax = pre_deducted_tax

    def get_organization_name(self):
        return self.__company_name

    def get_sin_number(self):
        return self.__sin_number

    def get_tax_payer_name(self):
        return self.__tax_payer_name

    def get_year(self):
        return self.__year

    def set_income(self,amount):
        self.__income = amount

    def set_pre_deducted_tax(self, amount):
        self.__pre_deducted_tax = amount

    def get_Income(self):
        return self.__income

    def get_tax_credit(self):
        return self.__pre_deducted_tax

    def __hash__(self) -> int:
        return hash(self.__company_name) + hash(self.__tax_payer_name) + hash(self.__sin_number) + hash(self.__year) + 57

    def __eq__(self, o: object) -> bool:
        return self.__class__ == o.__class__ and self.__hash__() == o.__hash__()

    def __str__(self) -> str:
        return "name: " + self.__tax_payer_name + " made " + str(self.__income) + " in " + self.__company_name + " in year " + self.__year

