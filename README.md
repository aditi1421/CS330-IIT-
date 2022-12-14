# Project Description :

## The purpose of this assignment is to get you to use Finite Automata concepts in solving real-life problems.

  File cs330.py is the code for the first part. Access code is "22087". Unlock code is '220871' while the lock code is '220874'. Characters from 0-9 are accepted.As soon as the last digit of the access code is entered, the program will signal the action taken (lock or unlock).

In the second part, randomgen.py tests how easy or difficult it is for an intruder to unlock the lock without actually knowing the code.This one takes a longer time since the intruder does not know the length of the string.

The program discards any other inputs whether it be alphabet characters or special characters.

# Pre Requisites: 
### The instructions below are for a Linux environment (Ubuntu 22.04).
1. Python
2. Git

# Installation :
1. To install `python`:
```
$ sudo apt update
$ sudo apt install python3
```

2. To install the `coverage` module :
```
$ pip install coverage
```

3. To install `git`:
```
$ sudo apt-get update
$ sudo apt-get install git-all
```

# Configuration: 
1. Clone the repository
```
  $ git clone https://github.com/aditi1421/CS330-IIT-
  $ cd CS330-IIT
```
2. Run unit tests 
```
 $ python3 -m coverage run -m unittest
```
3. View unittest coverage report:
```
 $ python3 -m coverage report
```
To run the execuatble: 
First part , run cs330.py, the Security Device simulator:
Unlock code - 220871
Lock code - 220874
```
$ ./cs330.py
```
Second part, run 
```
 $ ./randomgen.py
```
# Author:
Aditi Kumar 

# Questions:
akumar91@hawk.iit.edu

