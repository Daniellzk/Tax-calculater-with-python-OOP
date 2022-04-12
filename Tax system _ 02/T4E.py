from T4 import T4


class T4E(T4):
    def __init__(self, sin_number, tax_payer_name, year, income, pre_deducted_tax, repay_rate):
        if repay_rate > 1 or repay_rate < 0:
            repay_rate = 0
        self.__repay_rate = repay_rate
        super().__init__("EI", sin_number, tax_payer_name, year, income, pre_deducted_tax)

    def get_repay_rate(self):
        return self.__repay_rate

    def set_repay_rate(self, new_repay_rate):
        if new_repay_rate > 1 or new_repay_rate < 0:
            print("new repay rate invalid")
        else:
            self.__repay_rate = new_repay_rate
