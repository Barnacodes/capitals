# The European Capitals Source

It’s quite common to forget the capitals of all countries of Europe. You are going to learn about a simple but powerful tool that can help you solve the before mentioned issue which works with an intuitive question/answer method.

This paper will guide you through the acknowledgment of how using this useful program. Let’s now get to the point and please, follow all the steps listed below:

## 1. How to populate the database

Open the terminal from your computer and access the directory ‘capitals’. 
Here you can find the folder ‘tests’ which contains the file ‘test’ charged to test the whole code.  
If the test succeed you can then move forward to the folder ‘scripts’ where you can find the file ```dbmanager.py``` where you will insert a *username* and a *password* as follows

*Commands*

* -a *username*
* -p *password*

If you have done everything properly the following mssage will appear:
```
USERNAME has been correctly inserted in ourdatabase
```

## 2. Run the Program

So far so good? Let’s move forward.

Exit from the folder ‘scripts and run the file ```main.py``` by checking whether you have the authorisation to have access to data. Now, you are probably asking yourself how to do this: you simply insert *username* and *password* again followed by the capital or country you are interested in but be careful, the arguments you need are now -c for your username and -p for your password.
```
python3 main.py -c USERNAME -p PASSWORD Rome
```
## Commands and line parameters
 
* -a insert username
* -p password if correct and present in ```ourdatabase.db```
* -c check the username  if correct and present in ```ourdatabase.db```
* -p check if correct and present in ```ourdatabase.db```

# Verbosity

About CAPITALS:

* level 0
"Returns the state of the input capital"

* level 1
"The capital of 'state' is 'your input' "

* level 2
" We are checking your input in order to understand if it is contained in the list of capitals, The capital of 'state' is 'your input' "

About STATES

* level 0
"Returns the capital of the input state"

* level 1
"The European state whose capital is 'capital' is 'your input' "

* level 2
 "We are checking your input in order to understand if it is contained in the list of capitals, The European state whose capital is 'capital' is 'your input' "
