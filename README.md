*****The overall program structure:

The program is built based on python OOP concept, it's a Tax calculating software which constructed by 4 classes.

    First is the Tax form class, which is an Abstract class, it is the core of the software.
and the blue-print for class like T4, T2202 and T4E. The T4 and T2202 inherit from tax form to provide more specific attribute to the user.
and T4E inherit from T4.Then we have Annual Tax Report class which contain all the tax forms that belongs to that specific tax year.
on top of that Personal Tax account is the top of the ladder it will contain all the Annual tax reports.

On the data structure side, Set and Dictionary are both implemented. Using set for the tax form in the Annual report level
so that the user can not add the same tax form twice, and Dictionary is also used parallel with the set so that other class can easily pick us the Tax form object via the key.
the similar structure is also used in the Personal tax account level to manage the Annual tax report, so no Annual report can be added twice.

Tax Form -> Annual Tax report -> Personal Tax account.



******The Abilities of the program:
    the Tax system focus on helping Ontario user to calculate their income like T4 and T4E with consideration of T2202 (tuition),
it will also help user calculate their tax balance after the pre-deducted tax as well as the RRSP and TFSA.
they can also contribute to their RRSP via this program and the system will automatically recalculate the available RRSP bracket.
The program provide user with ease when it comes to adding tax form. With user's approval, Annual Tax report will automatically generate
if the current year of the tax form has not been filed yet.

In General, user will be able to
    1.add tax form of any year, the program will test to see if the tax form information match the account information before added
    2.remove tax form from any year, the program will test to see if the tax form exist
    3.remove annual report, the program will test to see if the report exist
    4.make RRSP contribution, the program will test to see if the RRSP contribution is within the bracket.

    5.to displace the account information:
             Name:
             Sin#:
             phone#:
             Address:
             Tax Balance:
             RRSP contribution: , RRSP bracket:
             TFSA Bracket:

    6. change personal information: phone number or address

***** Instruction *****
    the program will start by asking user to create and account, then will displace a Menu like this:
                _____________________________
                to exit the system enter "0"
                To add new tax form enter "1"
                To remove tax form enter "2"
                To remove annual report enter"3"
                To make RRSP contribution enter "4"
                To display account information enter "5"
                To change phone number or address enter "6"
                ___________________________________________

*** User can exit the program when enter 0

*** Add a new tax form, the program will displace 3 options
for user to determine what type of Tax form (T4, T2202, T4E) he/she want to add:

                ---------add tax form--------------
                What type of tax form you want to create?
                 T4 enter "1", T2202 enter "2", T4E enter "3"
                please enter your option:

then user need to enter some information related to the form, take a T4 as an example:
                ________________
                enter company name: McMaster
                please enter sin number: 123456
                please enter tax-payer name: Tony Smile
                please enter year: 2021
                enter income: 120000
                enter pre-deducted tax amount: 25000
                ---------------------------------------

the form will only be added if the information like sin# and name matches with the one in the account.


if the annual report has not been filed yet for the that particular tax year,
program will ask user if he would like to file the annual report:
                ______________________________________
                2021 Annual report not found or hasn't been filed
                do you want to create 2021 Annual report here?
                 Yes reply: 1 or No reply: 0
                 reply:
                ____________________________________

if user reply 1, the annual report will be automatically generated.:
                ___________________________________
                total prepaid tax for 2021 is now $25000
                current tax balance for 2021 is $11900.0
                2021 RRSP contribution: $0, 2021 overall RRSP bracket: $21600.0
                mcmastert4 Tax form successfully added
                ************************
                2021 Annual report successfully added
                ************************
                ____________________________________

*** Remove a tax form: user need to enter the year, the organization name and the tax form type
(because you can get pay from McMaster and go to school there which make you have a T4 and T2202 from the same organization)

                -----------remove tax form-------------
                enter tax form year: 2021
                enter organization name: s
                if the tax form is T4 enter 1, if it is T2202 enter 2, if it is T4E enter 3
                enter here: 1
                -------------------

*** Remove Annual report, they need to enter the year of the annual report:

                -----------remove annual report-------------
                ***WARNING**** Removing Annual report will also REMOVE all the tax form inside the report and REFUND all the RRSP contribution****

                Enter the YEAR of the Annual report you want to remove: 2021
                Successfully remove 2021 report
                ************************

*** To make RRSP contribution, user will need to enter the amount they want to contribute,
the program will validate the input amount to make sure it doesn't exceed the bracket,
the program will also automatically distribute the RRSP contribution to each Year's bracket.

                ----------make RRSP contribution-------------
                Current Overall RRSP bracket is: 11970.00
                enter amount of contribution: 11970
                -------------------
                total prepaid tax for 2021 is now $13800.00
                current tax balance for 2021 is $-2287.20
                2021 RRSP contribution: $9720.00018, 2021 overall RRSP bracket: $9720.00
                successfully finish RRSP contribution process
                -------------------
                total prepaid tax for 2022 is now $5000.00
                current tax balance for 2022 is $-2335.00
                2022 RRSP contribution: $2249.999820000001, 2022 overall RRSP bracket: $2250.00
                successfully finish RRSP contribution process

***To display all tax form and Annual report enter 5

***To display account information by enter 6 at the menu level

*** change address or phone number: user need to pick they want to change phone number or address:

                -----------Changing Personal information-----------------
                if you want to change phone number enter "1", if you want to change address enter "2"
                enter here: