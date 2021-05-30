
:fire:  Data Driven Simulator is python base script which predicts the ignition delay based on the experimental data. It uses error based clustering technique to divide the data into three clusters based on relative error in prediction and sign of prediction error to obtain the accurate regression models. It works perfectly fine with data having continious dependent (output) variable.

---
## System Requirements:

:fire:  OS : Ubuntu (This document is written for Ubuntu) 

:fire:  Python 3.6+

:fire:  RDKit - an open-source package.

---
## Installation:

:fire:  Download the solver and add in your './home ' directory.
:fire:  Open your ./bashrc file and add Sourcing line at the bottom of file.
Replace "path to" with your system location

---
**Sourcing :**

:fire:  Add the following command in your './bashrc' file 

export CLEANCODE="~/path to/Data_driven_Kinetics/"

export PATH=$PATH:$CLEANCODE

alias IDprediction="pwd>~/path to/Data_driven_Kinetics/filelocation.txt && Run.sh"

**Example:**
If you have kept the folder in ./home directory then configure .bashrc with following command:

\#Package command Finder:

export CLEANCODE="~/Data_driven_Kinetics/"

export PATH=$PATH:$CLEANCODE

alias IDprediction="pwd>~/Data_driven_Kinetics/filelocation.txt && Run.sh"


---
**Dependency:**

:fire:  To install all the dependency use INSTALL.sh file. Run command given below in the terminal

<div class="text-orange mb-2">
chmod +x INSTALL.sh

./INSTALL.sh
</div>
 

---

## Running the program:
---
After initial setup,

Open terminal.
Type "IDprediction -arguments"


Input arguments to 'IDprediction' is specified as below:

Consider the data file as 'file_name.csv'


:fire:  **-a	file name** - To ‘**a**nalyze’ the data-set by selecting range of parameters

ex: IDprediction -a  file_name.csv  

:fire:  **-b	FuelSMILE** - To find the '**b**ond’ types in given fuel

ex: IDprediction -b  CCC 

:fire:  **-h	file name** - To generate '**h**istogram’ plots of parameters for each fuel individually

ex: IDprediction -h  file_name.csv 

:fire:  **-c	value** - To define the '**c**riteria' for error based clustering

:fire:  **-l 	value** - To ‘**l**imit’ number of reference point

:fire:  **-r	True/False** - To '**r**emove’ feature by backelimination

:fire:  **-s	value** - To specify **s**ignificance level


:fire:  **-m	file name** - To find out **m**ultiple linear regression of data 

ex: IDprediction -c 0.05 -l 10 -r True -s 0.05  -m  file_name.csv 

:fire: **-t file name** - ‘**T**ree’ type regression based clustering algorithm

ex: IDprediction -c 0.05 -r False -t file_name.csv 

:fire:  **-e	file name** - '**E**xternal' Dataset used for prediction (Complete above Model generation first)

ex: IDprediction -e  test_data.csv 

:fire:  **-k	file name** - To run code multiple ‘(**k**)’ times and store all test prediction result in different directory

ex: IDprediction -k testset.csv

:fire:  **-f	file name** - Probability density ‘**f**unction’ plot of testing result after running code 'k' times

ex: IDprediction -f testset.csv


:fire:  **-p	file name** - **p**lot and obtain of average value of coefficient from coefficient file (If coefficient result obtained many times and there is variation in coefficients)

ex: IDprediction -p  coefficient_3.csv 

:fire:  **-o	file name** - To run any '**o**ther’ dataset than fuel

ex: IDprediction -c 0.05 -l 10 -o anyFile.csv

**Don’t forget to make changes in ’feature selection.py
file’**

---
Brought up by :
---

<dl>
      <a href="https://krithikasivaram.github.io">
         <img alt="CCC Group" src="https://github.com/pragneshrana/logos/blob/master/logo.jpg"
         width=100" height="100">
      </a>
      <a href="http://sivaramambikasaran.com/">
         <img alt="SAFRAN Group" src="https://github.com/pragneshrana/logos/blob/master/17197871.png"
         width=100" height="100">
      </a>
</dl>

