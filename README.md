# Fizzbuzz

### Description

A simple Python program that prints the numbers from 1 to 100. But for multiples of three it prints "Fizz" instead of the number and for the multiples of five it prints "Buzz". For numbers which are multiples of both three and five it prints "FizzBuzz".

### Installation

- Ensure you have python 3.6 or higher installed. Documentation for this can be found [here](https://www.python.org/downloads/)
- Inside your terminal, clone the repository into your folder of choice with the command `git clone https://github.com/tapiwa03/fizzbuzz.git`
- In your terminal, change directory to the `fizzbuzz` project folder that has just been created
- While inside the fizzbuzz project folder on the terminal, create a virtual environment by entering the following command `python3 -m venv venv`
- Start the virtual environment by entering this command in the terminal `source venv/bin/activate`. For windows users make user of `.\venv\Scripts\activate`
- Install requirements by entering this command in the terminal `pip3 install -r requirements.txt`

### Running The Program

- In the terminal enter the command `python3 main.py` and the program will execute as expected
- If you want to add your own parameters you can by appending the numbers
- Appending one number like this `python3 main.py 300` will set start to 1 and end to 300
- Appending two numbers like this `python3 main.py 300 700` will set start to 300 and end to 700

### Linting The Code

- To check for linting errors you can run the command `flake8 .`
- To auto lint the file after writing your code you can run the command `black main.py`
