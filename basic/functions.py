def beef():
    print("Dayum, functions are cool!")


def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)

beef()
bitcoin_to_usd(3.85)
bitcoin_to_usd(1)
bitcoin_to_usd(13)

def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

buckys_limit = allowed_dating_age(27)
creepy_joe_limit = allowed_dating_age(49)
print("Bucky can date girls", buckys_limit, "or older")
print("Creepy Joe can date girls", creepy_joe_limit, "or older")


# default value for a argument
def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()



