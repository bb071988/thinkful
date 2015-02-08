##Use a while loop to solve the following problem:
##A slow, but determined, walker sets off from Leicester
##to cover the 102 miles to London at 2 miles per hour.
##Another walker sets off from London heading to Leicester
##going at 1 mile per hour. Where do they meet?

walk1 = 0
walk2 = 102


while(walk1 != walk2):
    walk1 +=2
    walk2 -=1

print(walk1)


