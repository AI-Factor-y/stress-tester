@echo off
echo.
echo stress tester by Abhinav p
echo ___________________________
echo.
echo compiling brute.cpp
g++ brute.cpp -o brute_ex
echo compiling optimal.cpp
g++ optimal.cpp -o optimal_ex

echo.
set /p n=Enter number of testfiles : 
echo.
set /p ipl=Number of lines in input of 1 testcase : 
echo.
set /p offset=offset / priority input line  : 
echo.
set /p opl=number of lines in output of 1 testcase :  

echo.

FOR /L %%A IN (1,1,%n%) DO (

	python testgen.py

	brute_ex<testcase.txt>brute_op.txt

	optimal_ex<testcase.txt>optimal_op.txt

	python find_diff.py %ipl% %offset% %opl%

	)

echo.
echo **** stress test completed ****

pause