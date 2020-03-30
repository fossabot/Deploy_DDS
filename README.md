
:fire:  Data Driven Simulator is python base script which predicts the ignition delay based on the experimental data. It uses error based clustering technique to divide the data into three clusters based on relative and absolute error of predicted and actual ignition delay to obtain the regression models.

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

Example:
##Ignition delay Finder

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


:fire:  **-a	file name** - Analyze the Dataset by for selected range of parameters

ex: IDprediction -a  file_name.csv  

:fire:  **-b	FuelSMILE** - To find out available bonds in the fuel

ex: IDprediction -b  CCC 

:fire:  **-h	file name** - To find out histogram plots of separated fuel with separated feature

ex: IDprediction -h  file_name.csv 

:fire:  **-c	value** - To define the **c**riteria for error based clustering

:fire:  **-r	True/False** - To activate/deactivate back elimination in regression

:fire:  **-s	value** - To specify significance level


:fire:  **-m	file name** - To find out **m**ultiple linear regression of data 

ex: IDprediction -c 0.05 -r True -s 0.05 True m  file_name.csv 

:fire: **-c Separation Criteria -t	file name** - Tree Model **g**eneration for given data with given separation **c**riteria

ex: IDprediction -c 0.05 -r False -g  file_name.csv 

:fire:  **-e	file name** -Prediction of Ignition delay for **e**xteranl data (Complete above Model generation first)

ex: IDprediction -e  test_data.csv 

:fire:  **-p	file name** - **p**lot and obtain of average value of coefficient from coefficient file (If coefficient result obtained many times and there is variation in coefficients)

ex: IDprediction -p  coefficient_3.csv 



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

