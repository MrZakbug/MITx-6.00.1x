# Write a procedure that converts an American number (between 0 and 99), written as a string, into the equivalent
# Mandarin.

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    us_num = int(us_num)
    if us_num <=10 and us_num >= 0:
        return trans[str(us_num)]
    elif us_num < 20 and us_num > 10:
        return trans['10'] + ' ' + trans[str(us_num%10)]
    elif us_num < 100 and us_num >+ 20:
        if us_num%10 > 0:
            return trans[str(us_num//10)]+ ' ' + trans['10'] + ' ' + trans[str(us_num%10)]
        else:
            return trans[str(us_num//10)]+ ' ' + trans['10']

print(convert_to_mandarin('99'))