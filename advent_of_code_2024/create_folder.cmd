@ECHO OFF
IF "%~1"=="" (
    EXIT /B 2
)

SET day_n="day%~1"
mkdir %day_n%
cd %day_n%
copy NUL p1.py
copy NUL p2.py
copy NUL input1
copy NUL input2
copy NUL test1
copy NUL test2
cd ..