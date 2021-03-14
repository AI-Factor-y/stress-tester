# code written by abhinav p

import random
import sys


random.seed()
sys.stdout=open("testcase.txt","w") #output file

def r(lower_limit,upper_limit):
	return random.randint(lower_limit,upper_limit)

def ra(lower_limit,upper_limit):
	return chr(ord('a')+r((ord(lower_limit)-ord('a')),(ord(upper_limit)-ord('a'))))

def raa():
	return chr(ord('a')+r(0,25))

def rf(lower_limit,upper_limit,decimal_places):
	return round(random.uniform(lower_limit,upper_limit),decimal_places)

def nl():
	print("")

# global testcase count
testcase_count=100

def testcase():

	n=r(2,50)
	print(n)



	for _ in range(n):
		x=r(0,500)
		print(x,end=" ")
	nl()
	for _ in range(n-1):
		y=r(0,1)
		print(y,end="")

	nl()





if __name__=="__main__":

	if(testcase_count!=1):
		print(testcase_count)

	for _ in range(testcase_count):
		testcase()