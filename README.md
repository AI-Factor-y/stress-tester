# stress-tester

author
------
Abhinav p (@Ai-FActor-y)

what is a stress tester
------------------------

When you are trying to find an optimal solution to a problem but you want to check whether your solution fails at some test cases.
If you already know a straight forward less efficient brute force approach then you can validate your optimal solution with the brute force solution as reference.

how it works
------------
testgen.py is generates random testcases and creates a testcase.txt file.

two cpp programs(brute and optimal) run through the testcases and create respective output files

finddiff.py file compares the two output files and also keeps the input testcases as reference to find where the two files disagree


whats inside
-----------
1:brute.cpp

write your brute force code here. input and output is std
___________

2:optimal.cpp

this is your optimal code . the code that you want to test whether it is write or wrong

__________
3: testgen.py

this file is used to create you testcases

it has functions to help you code faster . write the nature of you testcase in function testcase and set the number of testcases you want to generate

1: r(lower_limit,upper_limit) : returns a random number within lower and upper limit

2: ra(lower_limit,uppe_limit) : returns a random character within lower and upper limit (limits are characters not integers)

3: raa() : return a character between a-z

4: nl() : print a new line

5: testcase_count : number of test case to generate

_____________
4: stress.bat

a batch files that runs the entire process in just one click. it also asks for parameters

__________

how to run
------------
write you testcase definition in testgen.py

write your brute force in brute.cpp, optimal code in optimal.cpp

double click stress.bat or type stress in command terminal


ui help
-------
number of testfiles : it refers to the number of times the testcases files are created . the more the number , more number of checks are made

Number of lines in input of 1 testcase : refers to your input lines in one testcase

offset / priority input line  : this part asks which part of the input is important. it helps the code to find the smallest input that fails. this helps in faster debugging

number of lines in output of 1 testcase : output lines for 1 testcase


features
---------

1: output line number : which line in output file fails

2: which testcase fails

3: which line in input fails and the input that failed the stress test is displayed in console

4: output of testcases of both approach, brute and optimal if they differ

5: gives the minimum length testcase. the smallest testcase that failed . this helps in debugging


about this code
-------------

this code is written by abhinav p and was meant for personal use. this tool is still under development .

Licensed under apache 
