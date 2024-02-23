# Project Command Pattern and Plugins

In this assignment, you will be learning how to make an interactive command line application that runs as an application and not a "script" that just executes once.  We will learn to use the command pattern and how to automaticly load commands using a simple plugin architecutre.  In addition, you will learn when to use exceptions through try catch or to use an if statment to guard your program from bad data. This unit is important because it starts to take our program from a simple script to an actual application and it begins to provide some structure, so that we can add new functionality.  This code is going to get you ready for the mid-term project, which will have a short time deadline and require both code and a paper that explains your programs architecure, design patterns, and functionality in some detail.  

 **You add this functionality to your previous assignment 4 - This is repo only covering the features in the lecture videos**

# Submission Requirements

1.  First watch the lecture and try out my code for the command main/command branch that is covered in the first lecture.  Make sure you understand how REPL and the command pattern works.  Add this to your previous program and make your calculator program interactive so that you have 4 commands: add, subtract, multiply, and divide.  

2.  (Bonus) - Try to make a menu command that lists the commands in the commands dictionary.  You would want to list the available commands, when the program starts and whenever the user types "menu".  I don't show you how to do this, but it will really help you understand and you will be required to do this in the next assignment.     

3.  Once you feel comfortable understanding how your program works and you have your calculator functions working as commands, you will need to update your tests and try to get to 100% test coverage.

4.  Once you get your program working interactivly and have covered it with tests the next step is to watch the lecture on plugins and you will learn how to quickly refactor your program to make it automaticly load plugins, so you don't have to manually add commands to your program.  In the future, you will just put a new command/plugin folder with a dunder init.py file inside the app/plugins folder and it will automaticly be made available as a command in the application.

5. (Bonus) - Get ahead of the curve for next week and ask ChatGPT about adding multiprocessor capabilities, so that your commands / plugins run on their own core.  If you ask ChatGPT like I do at the end of the 2nd video, you will see that its a relativly minor change that will be useful in the future.  Eventually, we will enable asynchronous operations, where you will be able to run multiple commands simultaneously.  Normally, a program runs on one core/thread and it has to run synchronously, which means it can't do anything else while its running a part of your program.  Asyncrounous operation will allow us to run multiple commands at once like how you may download multiple files at one time in a program.  As we go through the course, we will identify challenges and solutions to improve the performance by managing memory usage and taking advantage of a computers available cpu resources. 

## Highly Recommended Videos to Watch - I would Watch Them

1. [Python Loop Performance - Really Interesting and Important to Understand](https://www.youtube.com/watch?v=Qgevy75co8c)
2. [Habits of The Good Programmer - Why we are programming the way we are with Design Patterns](https://www.youtube.com/watch?v=q1qKv5TBaOA&t=2s)
3. [Inventor of Python Talking about the Global Interpreter Lock and multicore issues with Python](https://www.youtube.com/watch?v=m4zDBk0zAUY)
4. [Design Patterns Explained - Level up your programming Game](https://www.youtube.com/watch?v=tv-_1er1mWI)

Content

###  Read, Evaluate, Print, Loop (REPL) (main Branch) - Keeping an app running 
*  The Command object oriented design pattern - Making your app do more than one thing.

### Command Assignment Readings
* https://refactoring.guru/design-patterns/command

### Command Pattern Lecture (Command Branch) - Instructor Required - [here](https://youtu.be/3DVUN091T5g)

* Knowing when to use If statements and Exceptions by following Easier to ask for forgiveness than permission(EAFP), or Look Before You Leap LBYL.

* Adding Plugins with Using ChatGPT - Gets rid of the manual loading of commands

### Plugins Lecture (Plugins Branch) - Instructor Required - [here](https://youtu.be/c2PmjazGW2w)

## Setup Instructions
1. Clone the repo
2. CD into the project folder
3. Create the virtual environment 
4. Activate the virtual environment (VE)
5. Install Requirements

## Test Commands
1. pytest run all tests
2. pytest tests/test_main.py <- Run just the tests in this file
3. pytest --pylint --cov <- Run Pylint and Coverage (Can be run independently)

## Current Libraries Installed
1. [Pytest - Testing Framework](https://docs.pytest.org/en/8.0.x/)
2. [Faker - Fake Data Creation](https://faker.readthedocs.io/en/master/)
3. [Pytest Coverage](https://pytest-cov.readthedocs.io/en/latest/readme.html)
4. [Pytest Pylint](https://pylint.readthedocs.io/en/stable/development_guide/contributor_guide/tests/launching_test.html)
## Adding Library
1.  Make sure you are in the correct VE, if not sure run "deactivate"
2.  Activate the VE
3.  Run pip freeze > requirements.txt