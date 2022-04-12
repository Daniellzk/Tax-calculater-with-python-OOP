from AnnualTaxReport import AnnualTaxReport
from T2202 import T2202
from T4 import T4
from T4E import T4E
from TaxForm import TaxForm
from PersoanlTaxAccount import PersonalTaxAccount


print("Welcome to the Tax calculate system!!")
print("********----------------********")
print("Creating new Personal Tax account")
sin_number = input("please enter sin number: ")
tax_payer_name = input("please enter tax payer name: ")
birth_year = int(input("please enter birth year: "))
phone_number = int(input("please enter phone number: "))
address = input("please enter address: ")

print()
print()

newPersonalTaxAccount = PersonalTaxAccount(sin_number, tax_payer_name, birth_year, phone_number, address)
system_quit = 0
while system_quit != 1:
    print("-----------Menu-----------------")
    print('to exit the system enter "0"\nTo add new tax form enter "1"\nTo remove tax form enter "2"\nTo remove annual report enter"3"\nTo make RRSP contribution enter "4"\n\nTo displace all the tax form and Annual report enter "5"\nTo display account information enter "6"\nTo change phone number or address enter "7"\n')
    user_input = input("please enter your option: ")

    if int(user_input) == 0:
        system_quit = 1
        print("***Thanks for using Tax calculating system !***")

    elif int(user_input) == 1:
        print("---------add tax form--------------")
        print('What type of tax form you want to create?\n T4 enter "1", T2202 enter "2", T4E enter "3"')
        form_type_user_input = int(input("please enter your option: "))
        if form_type_user_input == 1:
            organization_name = input("enter company name: ")
            sin_number = input("please enter sin number: ")
            tax_payer_name = input("please enter tax payer name: ")
            year = input("please enter year: ")
            income = int(input("enter income: "))
            pre_deducted_tax = int(input("enter pre-deducted tax amount: "))

            if income > 0 and pre_deducted_tax >= 0:
                new_t4 = T4(organization_name,sin_number,tax_payer_name,year,income,pre_deducted_tax)
                newPersonalTaxAccount.add_tax_form(new_t4)
            else:
                print("income input or pre-deducted tax amount is not valid, false to add T4.\nPlease try again.")

        elif form_type_user_input == 2:
            organization_name = input("enter institution name: ")
            sin_number = input("please enter sin number: ")
            tax_payer_name = input("please enter tax payer name: ")
            year = input("please enter year: ")
            tuition = int(input("enter tuition amount: "))

            if tuition > 0:
                new_t2202 = T2202(organization_name,sin_number,tax_payer_name,year,tuition)
                newPersonalTaxAccount.add_tax_form(new_t2202)
            else:
                print("tuition amount is not valid\nPLease try to recreate T2202")

        elif form_type_user_input == 3:
            sin_number = input("please enter sin number: ")
            tax_payer_name = input("please enter tax payer name: ")
            year = input("please enter year: ")
            income = int(input("enter income: "))
            pre_deducted_tax = int(input("enter pre-deducted tax amount: "))

            if income > 0 and pre_deducted_tax >= 0:
                new_t4e = T4E(sin_number,tax_payer_name,year,income,pre_deducted_tax,repay_rate=0.2)
                newPersonalTaxAccount.add_tax_form(new_t4e)
            else:
                print("income input or pre-deducted tax amount is not valid, false to add T4E.\nPlease try again.")

        else:
            print("input invalid")

    elif int(user_input) == 2:
        print("-----------remove tax form-------------")
        year = input("enter tax form year: ")
        name = str(input("enter organization name: "))
        print("if the tax form is T4 enter 1, if it is T2202 enter 2, if it is T4E enter 3")
        form_type_user_input = int(input("enter here: "))
        if form_type_user_input == 1:
            organization_name = name + "t4"
        elif form_type_user_input == 2:
            organization_name = name + "t2202"
        elif form_type_user_input == 3:
            organization_name = name + "t4"
        newPersonalTaxAccount.remove_tax_form(year, organization_name)

    elif int(user_input) == 3:
        print("-----------remove annual report-------------")
        print("***WARNING**** Removing Annual report will also REMOVE all the tax form inside the report \nand REFUND all the RRSP contribution****")
        print()
        year = input("Enter the YEAR of the Annual report you want to remove: ")
        newPersonalTaxAccount.remove_annual_report(year)

    elif int(user_input) == 4:
        print("----------make RRSP contribution-------------")
        print("Current Overall RRSP bracket is: " + str('{:.2f}'.format(newPersonalTaxAccount.get_RRSP_bracket())))
        RRSP_contribution = int(input("enter amount of contribution: "))
        newPersonalTaxAccount.RRSP_contribution(RRSP_contribution)

    elif int(user_input) == 5:
        print("-----------Listing all Tax form and Annual report----------")
        if len(newPersonalTaxAccount.get_Annual_report_set()) == 0:
            print("No tax form or Annual report found")
        else:
            for report in newPersonalTaxAccount.get_Annual_report_dictionary().values():
                print(report.get_year() + " Annual report: ")
                if len(report.get_set()) == 0:
                    print("** Empty")
                else:
                    for form in report.get_dictionary().values():
                        if form.get_organization_name()[-1] == "4":
                            print(form.get_organization_name()[0:-2] + " " + form.get_organization_name()[-2:])
                        elif form.get_organization_name()[-1] == "2":
                            print(form.get_organization_name()[0:-5] + " " + form.get_organization_name()[-5:])


    elif int(user_input) == 6:
        print("-----------Personal Tax account information-----------------")
        newPersonalTaxAccount.get_account_information()

    elif int(user_input) == 7:
        print("-----------Changing Personal information-----------------")
        print('if you want to change phone number enter "1", if you want to change address enter "2"')
        change_user_input = int(input("enter here: "))
        if change_user_input == 1:
            user_input = int(input("Please enter new phone number: "))
            newPersonalTaxAccount.set_phone_number(user_input)
            print("information updated---------------")
            newPersonalTaxAccount.get_account_information()
        elif change_user_input == 2:
            user_input = input("Please enter new address: ")
            newPersonalTaxAccount.set_address(user_input)
            print("information updated---------------")
            newPersonalTaxAccount.get_account_information()
        else:
            print("invalid input!!!")




























