from AnnualTaxReport import AnnualTaxReport
from TaxForm import TaxForm


class PersonalTaxAccount:
    def __init__(self, sin_number, tax_payer_name, birth_year: int, phone_number: int, address: str):

        self.__sin_number = str(sin_number)
        self.__tax_payer_name = str(tax_payer_name).lower()
        self.__birth_year = birth_year
        self.__phone_number = phone_number
        self.__address = address

        self.__Annual_report_set = set[AnnualTaxReport]()
        self.__Annual_report_dictionary = dict[str, AnnualTaxReport]()  # Dictionary {year : Annual_report}

        self.__RRSP_contribution = 0
        self.__RRSP_bracket = 0
        self.__TFSA_bracket = len(self.__Annual_report_set) * 6000

        self.__tax_balance = 0

    def get_sin_number(self):
        return self.__sin_number

    def get_tax_payer_name(self):
        return self.__tax_payer_name

    def get_birth_year(self):
        return self.__birth_year

    def get_phone_number(self):
        return self.__phone_number

    def get_address(self):
        return self.__address




    def get_RRSP_contribution(self):
        return self.__RRSP_contribution

    def get_tax_balance(self):
        return self.__tax_balance

    def get_Annual_report_set(self):
        return self.__Annual_report_set

    def get_Annual_report_dictionary(self):
        return self.__Annual_report_dictionary

    def get_RRSP_bracket(self):
        return self.__RRSP_bracket

    def get_TFSA_bracket(self):
        return self.__TFSA_bracket


    def set_sin_number(self, new_sin_number: str):
        self.__sin_number = new_sin_number

    def set_tax_payer_name(self, new_name: str):
        self.__tax_payer_name = new_name

    def set_birth_year(self, new_birth_year: int):
        self.__birth_year = new_birth_year

    def set_phone_number(self, new_phone_number: int):
        self.__phone_number = new_phone_number

    def set_address(self, new_address: str):
        self.__address = new_address



    def add_tax_form(self, tax_form: TaxForm):
        pass
        if tax_form.get_tax_payer_name() == self.get_tax_payer_name() and tax_form.get_sin_number() == self.get_sin_number():
            if tax_form.get_year() not in self.__Annual_report_dictionary:
                print(tax_form.get_year() + " Annual report not found or hasn't been filed")
                user_input = int(input("do you want to create " + tax_form.get_year() + " Annual report here? \n Yes reply: 1 or No reply: 0\n reply: "))
                if user_input == 1:
                    annual_report = AnnualTaxReport(self.__sin_number, self.__tax_payer_name, tax_form.get_year())
                    annual_report.add_tax_form(tax_form)
                    self.add_annual_report(annual_report)
                elif user_input == 0:
                    print("tax form not added")
            else:
                self.__Annual_report_dictionary[tax_form.get_year()].add_tax_form(tax_form)
                self.__Annual_report_set.clear()
                for report in self.__Annual_report_dictionary.values():
                    self.__Annual_report_set.add(report)
                self.auto_update(self.__Annual_report_set)
        else:
            print("!!!!WARNING!!! form doesnt belong to this account please double check data")

    def remove_tax_form(self, year: str, organization_name: str):

        if year in self.__Annual_report_dictionary.keys():
            self.__Annual_report_dictionary[year].remove_tax_form(organization_name)
            self.__Annual_report_set.clear()
            for report in self.__Annual_report_dictionary.values():
                self.__Annual_report_set.add(report)
            self.auto_update(self.__Annual_report_set)

        else:
            print("!!!!WARNING!!! " + year + " Annual report not existed, therefore unable to remove tax form form it")



    def add_annual_report(self, annual_report: AnnualTaxReport):
        if annual_report.get_tax_payer_name() == self.get_tax_payer_name() and annual_report.get_sin_number() == self.get_sin_number():
            if annual_report not in self.__Annual_report_set and annual_report not in self.__Annual_report_dictionary:
                self.__Annual_report_set.add(annual_report)
                self.__Annual_report_dictionary[annual_report.get_year()] = annual_report

                self.auto_update(self.__Annual_report_set)

                print(annual_report.get_year() + " Annual report successfully added")
                print("************************")
            else:
                print("!!!!WARNING!!!  Annual report already existed, to replace report please remove the old one first")
        else:
            print("!!!!WARNING!!!  Annual report doesn't belong to this Account, please verify data entry")

    def remove_annual_report(self, year: str):
        if year in self.__Annual_report_dictionary.keys():
            self.__Annual_report_set.remove(self.__Annual_report_dictionary[year])
            removed_report = self.__Annual_report_dictionary.pop(year)

            self.auto_update(self.__Annual_report_set)

            print("Successfully remove " + removed_report.get_year() + " report")
            print("************************")
        else:
            print("!!!!WARNING!!!  Annual report from " + year + " not found")

    def auto_update(self, annual_report_set: set[AnnualTaxReport]):
        rrsp_contribution = 0
        rrsp_bracket = 0
        tax_balance = 0

        for report in annual_report_set:
            rrsp_bracket += report.get_RRSP_bracket()
            rrsp_contribution += report.get_RRSP_contribution()
            tax_balance += report.get_tax_balance()

        self.__RRSP_contribution = rrsp_contribution
        self.__RRSP_bracket = rrsp_bracket - rrsp_contribution
        self.__tax_balance = tax_balance
        self.__TFSA_bracket = len(annual_report_set) * 6000


    def RRSP_contribution(self, amount: int):
        if amount > 0:
            temp_amount = amount
            annual_bracket = 0
            new_set = set()
            copy_of_dictionary = self.__Annual_report_dictionary.copy()
            for report in copy_of_dictionary.values():
                annual_bracket = report.get_RRSP_bracket()
                if temp_amount >= annual_bracket:
                    report.RRSP_contribution(annual_bracket)
                    temp_amount -= annual_bracket
                else:
                    report.RRSP_contribution(temp_amount)
                    temp_amount = 0
                new_set.add(report)
            if temp_amount > 0:
                print("!!!!WARNING!!!  amount entered will make total contribution more than the RRSP bracket")
            else:
                self.__Annual_report_set.clear()
                self.__Annual_report_set = new_set
                self.__Annual_report_dictionary = copy_of_dictionary
                self.auto_update(self.__Annual_report_set)

        else:
            print("!!!!WARNING!!!  invild amount, amount needs to be greater than zero.")








    def get_account_information(self):
        print("Name: " + self.get_tax_payer_name() + "\n" + "Sin#: " + str(self.get_sin_number()) + "\n" + "phone#: " + str(self.get_phone_number()) + "\n" + "Address: " + self.get_address() + "\n" + "Tax Balance: " + str('{:.2f}'.format(self.get_tax_balance())) + "\n" + "RRSP contribution: " + str('{:.2f}'.format(self.get_RRSP_contribution())) + ", RRSP bracket: " + str('{:.2f}'.format(self.get_RRSP_bracket())) + "\n" + "TFSA Bracket: " + str(self.get_TFSA_bracket()))


