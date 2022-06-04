import random
def passwordgen():
    lowerchar = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    upperchar = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    spsymbol = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','~','`','<','>',',','.','?','/',';',':']
    numericchar = ['1','2','3','4','5','6','7','8','9','0']
    password1 = random.choice(lowerchar)+random.choice(upperchar)+random.choice(spsymbol)+random.choice(numericchar)
    password2 = random.choice(lowerchar)+random.choice(upperchar)+random.choice(spsymbol)+random.choice(numericchar)
    # password must be of 8 characters 
    password = password1 + password2
    return password
print("Generate Password of length 8 characters - ")
print("generated password = ",passwordgen())