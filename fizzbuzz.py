## fizz buzz
##If the number is divisible by 3, instead of the number you say “fizz”.
##If it’s divisible by 5, you say “buzz”.
##And finally if it’s divisible by both 3 and 5, you say “fizz buzz”. 

# -*- coding: cp1252 -*-


upperLimit = 100

x=1

while(x < upperLimit + 1):

    fizz = False
    buzz = False

    if(x % 3==0):
         fizz = True

    if(x % 5 ==0):
        buzz = True

    if(fizz and buzz):
        print("fizz buzz")
    elif(fizz):
            print('fizz')
    elif(buzz):
            print('buzz')
    else:
        print(x)

    x+=1
    
