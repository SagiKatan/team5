IsItWorking: bool = bool(input("is it?"))


def test():

    if IsItWorking:
        print("Its working")
        print("WWWWW")

    if not IsItWorking:
        print(":c")


test()


def funny_func(number):
    return -1*number


def funnier_func(number):
    if number<0: return 0.5 ** number
    return number ** 2
