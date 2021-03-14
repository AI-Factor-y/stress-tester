import os
import math
import sys
# code for debug by abhinav p 

myfile=open("optimal_op.txt",'r').readlines()

real_op=open("brute_op.txt",'r').readlines()

input_file=open("testcase.txt",'r').readlines()
flag=True
mini_inp=10000000


ipl=int(sys.argv[1])
offset=int(sys.argv[2])-1
opl=int(sys.argv[3])


min_i_val=0
for i in range(len(myfile)):
	if myfile[i]!=real_op[i]:
		o=math.ceil((i+1)/opl)
		print(f"\nline in output : {(i+1)*opl} | line in input : {(ipl*i)+2}")

		print("testcase number : ",o)
		print("----------------------------------")
		print("input : ")

		for k in range(ipl):
			print(input_file[ipl*(o-1)+1+k],end="")

		print("")

		print("output required : ")

		for k in range(opl):
			print(real_op[i+k],end="")

		print("")
		print("your output : ")

		for k in range(opl):
			print(myfile[i+k],end="")

		print("___________________________________")
		flag=False



		if(len(input_file[ipl*(o-1)+1+offset])<mini_inp):
			mini_inp=len(input_file[ipl*(o-1)+1+offset])
			minimInp=ipl*(o-1)+1
			min_i_val=i


if(flag):
	print("No changes detected .. ")
else:
	print("\n*****************************")
	print("      MINIMUM LENGTH ERROR")
	print("================================")
	i=min_i_val
	o=math.ceil((i+1)/opl)
	print(f"line in output : {(i+1)*opl} | line in input : {(ipl*i)+2}")

	print("testcase number : ",o)
	print("----------------------------------")
	print("input : ")

	for k in range(ipl):
		print(input_file[minimInp+k],end="")

	print("")
	print("output required : ")

	for k in range(opl):
		print(real_op[min_i_val+k],end="")

	print("")
	print("your output : ")

	for k in range(opl):
		print(myfile[min_i_val+k],end="")

	print("___________________________________")
	os.system("pause")