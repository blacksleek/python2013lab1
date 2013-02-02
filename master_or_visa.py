def master_and_visa(self): # boolean function
    if self[0] == "4": # visa
        if len(self) == 13 or len(self) == 16:
            return True
        else:
            return False
    elif self[:2] == "51" or self[:2] == "52" or self[:2] == "53" or self[:2] == "54" or self[:2] == "55": # master
        if len(self) == 16:
            return True
        else:
            return False
    else:
        return False

def check_digit(self): # boolean function
    try:
        check_digit = int(self[-1])
        number = list(self[:-1])
        number.reverse() # double the number starting from check digit, going leftwards
        for i in range(0,len(number),2):
            number[i] = str(2 * int(number[i]))
        for i in range(len(number)):
            if len(number[i]) > 1:
                number[i] = int(number[i][0]) + int(number[i][1]) # adding individual numbers which has 2 digits
        for i in range(len(number)):
            number[i] = int(number[i])
        sum_digit = int(str(int(sum(number)) * 9)[-1]) # obtaining the correct check digit
        if sum_digit == check_digit:
            return True
        else:
            return False
    except:
        return False

def master_or_visa(self):
    if master_and_visa(self) and check_digit(self):
        if self[0] == "4":
            print("VISA")
        else:
            print("MASTERCARD")
    else:
        print("INVALID CARD NUMBER")


number = input("Input Credit Card Number: ")
master_or_visa(number)
