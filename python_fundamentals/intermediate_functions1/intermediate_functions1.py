import random
def randInt(min=0, max=100):
    if min > max or max < 0 or min < 0:
        return False
    else:
        num = random.random()*(max-min)+ min
    return round(num)

print(randInt(-1,10))
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
#BONUS: account for any edge cases (eg. min > max, max < 0)
