class Divide_by_zero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"В данном примере делить на ноль нельзя")


div = Divide_by_zero(55, 5)
print(Divide_by_zero.divide_by_null(5, 0))
print(Divide_by_zero.divide_by_null(55, 5))
print(div.divide_by_null(100, 0))
