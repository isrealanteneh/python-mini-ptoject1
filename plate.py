def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# requirment to check the first two letter
def firstLetter(s):
    if s[:2].isalpha():
        isalpha = True
    else:
        isalpha = False
    return isalpha

# function to check if the first number is 0

def findzero(s):
    for i in range(len(s)):
     if s[i].isnumeric():
            x = s[i]
            s.split(x)
            if x == '0':
                return False
            else:
                return True
                break
    else:
        return True
    

#  requirment to check if the number is in the middel
def middelNumber(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            if s.endswith(s[i]) == False:
                if s[i + 1].isnumeric():
                    valid = True
                else:
                    valid =False
                    break
        else:
            valid = True
    return valid

# function to check amount of total word
def amount(s):
    if len(s) <= 6:
        istrue = True
    else:
        istrue = False
    return istrue

# function to check is their any dot comma and punctuate marks
def checkPunctuate(s):
    if s.isalnum():
        istrue = True
    else:
        istrue = False
    return istrue

def is_valid(s):
    if firstLetter(s) and amount(s) and middelNumber(s) and checkPunctuate(s) and findzero(s):
        isValid = True
    else: isValid = False

    return isValid



main()

