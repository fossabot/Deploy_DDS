#updating
echo 'Updating System'
sudo apt-get update

#install python
echo 'Installing Python'
sudo apt install python3.8

#install RDkit
echo 'Installing RDKIT'
pip install rdkit-pypi

#numpy
echo 'Installing NUMPY'
pip install numpy

#scipy
echo 'Installing SCIPY'
pip install scipy

#matplotlib
echo 'Installing MATPLOTLIB'
python3 -m pip install matplotlib

#pandas
echo 'Installing PANDAS'
python3 -m pip install pandas

#regex
echo 'Installing REGEX'
pip install regex

# #statsModel
# echo 'Installing STATMODELS'
# pip install statsmodels

#collection
echo 'Installing collections-libs'
pip install collections-extended

#random
echo 'Installing RANDOM'
pip install random2

#seaborn
echo 'Installing SEABORN'
pip install seaborn

#sklearn
echo 'Installing SKLEARN'
pip install -U scikit-learn

#coverage
echo 'Installing COVERALL'
pip install coveralls

#codecov
echo 'Installing CODECOVERAGE'
pip install codecov

# #latex
# echo 'Installing texlive'
# sudo pip install latex
# sudo apt-get install -y texlive texlive-latex-extra texlive-latex-recommended