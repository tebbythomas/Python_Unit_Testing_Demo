# Python unit testing demo

<p>
This repo consists of 2 demos showcasing how Python's inbuilt <b>unittesting</b> module can be used to perform unit testing.
<br />
The files to note are:
<br />
<br />
1. <b>calc.py</b>: A simple Python calculator program with basic addition, subtraction, multiplication and division methods
<br />
2. <b>test_calc.py</b>: The corresponding unittest file that uses asserts methods to test all the operations defined in calc.py
<br />
3. <b>employee.py</b>: A simple depiction of an Employee object with fields like first name, last name, salary and also a dummy call to an external API to find out the employees schedule
<br />
4. <b>test_employee.py</b>: This code is the unittest file for employee.py and shows how assert functions can be used to test all the methods of employee.py like email, pay, full names.
<br />
Also a <b>mocked_get</b> assertion is used to mimic testing a call to an external API and testing its responses.
