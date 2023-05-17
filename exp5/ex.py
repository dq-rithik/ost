class InvalidAgeException(Exception):
    pass
class notEligible(Exception):
    pass
class OverBound(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise InvalidAgeException
    elif num <18:
        raise notEligible
    elif num > 100:
        raise OverBound
    else:
        print("Eligible to Vote")
                
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
except notEligible:
    print("Not eligible to vote")
except OverBound:
    print("Age is out of bound")