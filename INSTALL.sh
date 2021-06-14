#updating
echo 'Updating System'
sudo apt-get update

#install python
echo 'Installing Python'
sudo apt-get install python3.6

#install RDkit
echo 'Installing RDKIT'
sudo apt-get install python3-rdkit
conda install -c rdkit rdkit
#conda install -c conda-forge rdkit

#numpy
echo 'Installing NUMPY'
pip install numpy

#scipy
echo 'Installing SCIPY'
pip install scipy

#matplotlib
echo 'Installing MATPLOTLIB'
pip install matplotlib

#pandas
echo 'Installing PANDAS'
pip install pandas

#regex
echo 'Installing REGEX'
pip install regex

#statsModel
echo 'Installing STATMODELS'
pip install statsmodels

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

#latex
echo 'Installing texlive'
sudo apt-get install texlive-full