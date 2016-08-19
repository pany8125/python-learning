income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income))
print(new_income)

new_lambda_incom = list(map(lambda x: x*3, income))
print(new_lambda_incom)