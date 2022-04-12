from TaxForm import TaxForm


class AnnualTaxReport:
    def __init__(self, sin_number, tax_payer_name, year):

        self.__sin_number = str(sin_number)
        self.__tax_payer_name = str(tax_payer_name).lower()
        self.__year = str(year)

        self.__tax_form_set = set[TaxForm]()
        self.__tax_form_dictionary = {}  # Dictionary {organization_name : Tax_form}

        self.__RRSP_contribution = 0
        self.__RRSP_bracket = 0
        self.__total_income = 0
        self.__total_payed_tax = 0
        self.__tax_balance = 0

    def get_sin_number(self):
        return self.__sin_number

    def get_tax_payer_name(self):
        return self.__tax_payer_name

    def get_year(self):
        return self.__year

    def get_set(self):
        return self.__tax_form_set

    def get_dictionary(self):
        return self.__tax_form_dictionary

    def get_RRSP_contribution(self):
        return self.__RRSP_contribution

    def get_RRSP_bracket(self):
        return self.__RRSP_bracket

    def get_total_income(self):
        return self.__total_income

    def get_total_payed_tax(self):
        return self.__total_payed_tax

    def get_tax_balance(self):
        return self.__tax_balance

    def auto_update(self, form_set: set[TaxForm]):
        total_income = 0
        total_pre_payed_tax = 0

        for form in form_set:
            total_income += form.get_Income()
            total_pre_payed_tax += form.get_tax_credit()

        self.__total_income = total_income
        self.__RRSP_bracket = self.__total_income * 0.18
        self.__total_payed_tax = total_pre_payed_tax
        if len(form_set) != 0:
            self.__tax_balance = self.tax_bracket(total_income - self.__RRSP_contribution) - self.__total_payed_tax
        else:
            self.__tax_balance = 0
        print("-------------------")
        print("total prepaid tax for " + self.__year+" is now $" + str('{:.2f}'.format(total_pre_payed_tax)))
        print("current tax balance for " + self.__year +" is $" + str('{:.2f}'.format(self.__tax_balance)))
        print(self.__year + " RRSP contribution: $" + str('{:.2f}'.format(self.__RRSP_contribution)) + ", " + self.__year + " overall RRSP bracket: $" + str('{:.2f}'.format(self.__RRSP_bracket)))


    def add_tax_form(self, tax_form: TaxForm):
        if tax_form.get_tax_payer_name() == self.get_tax_payer_name() and \
                tax_form.get_sin_number() == self.get_sin_number() and tax_form.get_year() == self.__year:
            if tax_form not in self.__tax_form_set and tax_form.get_organization_name() not in self.__tax_form_dictionary.keys():
                self.__tax_form_set.add(tax_form)
                self.__tax_form_dictionary[tax_form.get_organization_name()] = tax_form

                self.auto_update(self.__tax_form_set)

                print(tax_form.get_organization_name() + " Tax form successfully added")
                print("************************")
            else:
                print("!!!!WARNING!!!  form already existed, to replace form please remove the old one first")
        else:
            print("!!!!WARNING!!!  form doesnt belong to this annual report please double check data")

    def remove_tax_form(self, organization_name: str):
        organization_name = organization_name.lower()
        if organization_name in self.__tax_form_dictionary.keys():
            self.__tax_form_dictionary.pop(organization_name)
            self.__tax_form_set.clear()
            for form in self.__tax_form_dictionary.values():
                self.__tax_form_set.add(form)
            self.auto_update(self.__tax_form_set)

            print("successfully remove tax from: " + organization_name)
        else:
            print("!!!!WARNING!!!  form from " + organization_name + " not found")

    def RRSP_contribution(self, amount: int):
        if amount > 0:
            if (self.__RRSP_contribution + amount) <= self.__RRSP_bracket:
                self.__RRSP_contribution += amount
                self.auto_update(self.__tax_form_set)
                print("successfully finish RRSP contribution process")
            else:
                print("!!!!WARNING  amount entered will make total contribution more than the RRSP bracket")
        else:
            print("!!!!WARNING!!!  invild amount, amount needs to be greater than zero.")

    def report_information(self):
        print("Name: " + self.__tax_payer_name + ", Year: " + self.__year + ", Total Income: " + str(
            self.__total_income) + ", tax Balance: " + str(self.__tax_balance))
        print("tax form list: ")
        for key in self.__tax_form_dictionary.keys():
            print(key + " Tax form")

    def tax_bracket(self, amount: int):

        tax = 0
        if 0 < amount <= 45000:
            tax += amount * 0.26
        else:
            tax += 45000 * 0.26
            if 45000 < amount <= 55000:
                tax += (amount - 45000) * 0.28
            else:
                tax += 10000 * 0.28
                if 55000 < amount <= 65000:
                    tax += (amount - 55000) * 0.3
                else:
                    tax += 10000 * 0.3
                    if 65000 < amount <= 85000:
                        tax += (amount - 65000) * 0.34
                    else:
                        tax += 20000 * 0.34
                        if 85000 < amount <= 120000:
                            tax += (amount - 85000) * 0.36
                        else:
                            tax += 35000 * 0.36
                            if 120000 < amount <= 160000:
                                tax += (amount - 120000) * 0.38
                            else:
                                tax += 40000 * 0.38
                                if 160000 < amount <= 200000:
                                    tax += (amount - 160000) * 0.4
                                else:
                                    tax += 40000 * 0.4
                                    tax += (amount - 200000) * 0.46
        return tax

    def __eq__(self, o: object) -> bool:
        return self.__class__ == o.__class__ and self.__hash__() == o.__hash__()

    def __hash__(self) -> int:
        return hash(self.__tax_payer_name) + hash(self.__sin_number) + hash(self.__year) + 32

    def __str__(self) -> str:
        return "Name: " + self.__tax_payer_name + ", Year: " + self.__year + ", Total Income: " + str(
            self.__total_income) + ", tax Balance: " + str(self.__tax_balance)
