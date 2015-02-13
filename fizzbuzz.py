## fizz buzz
##If the number is divisible by 3, instead of the number you say “fizz”.
##If it’s divisible by 5, you say “buzz”.
##And finally if it’s divisible by both 3 and 5, you say “fizz buzz”. 

# -*- coding: cp1252 -*-

import sys

upperLimit = None

x=1

inputList =[1,2,3,4,5,6,7,8,9,10]
outputList =['1','2','fizz','4','buzz','fizz','7','8','fizz',
             'buzz','11','fizz','13','14','fizzbuzz']



def fizzbuzz(x):

    if(x % 3==0 and x % 5 ==0):
        return 'fizz buzz'
    elif(x % 3==0):
        return 'fizz'
    elif(x % 5 ==0):
        return 'buzz'
    else:
        return str(x)

def test():

    for i, item in enumerate(inputList):
        print('Asserting that {} = {}'.format(fizzbuzz(item),outputList[i]))
        assert(fizzbuzz(item) == outputList[i])


while(upperLimit == None):
    if len(sys.argv) >= 2:
        tempLimit = sys.argv[1]
        upperLimit = int(tempLimit)

    else:
        tempLimit = raw_input("Please enter an integer to fizzbuzz  ")
        try:
            upperLimit = int(tempLimit)
        except:
            print("invalid input ")
            
        
test()
    
while(x < upperLimit + 1):

    print(fizzbuzz(x))

    x+=1
    
