# Overview

<img style="float: right;" src="https://images-na.ssl-images-amazon.com/images/I/619wcNR9O5L._AC_SL1500_.jpg" alt="drawing" width="200"/> This project is for a part of the SEG2105 Course at the University of Ottawa. It is a tribute to one of Dieter Rams' most iconic designs, the ET66 calculator (which is an iteration of the 1980 ET55). 

By the start of the 1980's calculators were common household products. Upon the release of the ET55, Braun's calculator design stood apart for its approachability, aesthetic and simplicity.

While it is currently possible to buy a [reissue of the ET66 calculator](https://www.amazon.ca/Braun-BNE001BK-Reissue-Calculator-Black/dp/B00DUDU2Q6), this project is meant to serve as a free software alternative that anyone can use and enjoy.

### 10 Principles for Good Design, [Dieter Rams](https://ifworlddesignguide.com/design-specials/dieter-rams-10-principles-for-good-design):

1. *Good design is innovative*
2. *Good design makes a product useful*
3. *Good design is aesthetic*
4. *Good design makes a product understandable*
5. *Good design is unobtrusive*
6. *Good design is honest*
7. *Good design is long-lasting*
8. *Good design is thorough down to the last detail*
9. *Good design is environmentally friendly*
10. *Good design is as little design as possible*

# Requirements

   1. The calculator should perform the basic arithmetic operations of an ordinary calculator
   2. The design should closely replicate the Braun ET66
   3. The program should be runnable on Windows, Linux and Mac

# System Architecture
The program is completely contained in the file ET66.py, except for the .gif image file of the calculator, which must be kept in the same folder as the script.

The following diagram shows the Python packages and their methods used and the two core classes and their methods:

<img src="https://raw.githubusercontent.com/166inter/ET66/master/ET66%20program%20architechture.jpg" alt="drawing" width="700"/>

### How to modify or add new features
The main functionality of the program is found in image_click. There are many possiblities to simplify or refactor the actions for each "hit" or click. If one is interested in making a new calculator face, one would need to modify the image_rects list to map the buttons correctly, along with ensuring the dimensions and screen match. 

Please note that the calculator provides basic functionality, however there are some known issues (as shown in testCases.txt)
# How to run

### Make sure the following dependencies are installed:

   1. python 3
   2. pip (recommended to install tkinter)
   3. tkinter (can install via the python package manager with `pip install tkinter`)


### Run the following commands:

   `git clone github.com/166inter/ET66.git`

   `cd ET66`

   `python ET66.py`
