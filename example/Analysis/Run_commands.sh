#!/bin/bash
##Source the file first or run by : source ./run.sh
export IDCODE="~/Data_driven_Kinetics/"
export PATH=$PATH:$IDCODE
alias IDprediction="pwd>~/Data_driven_Kinetics/filelocation.txt && Run.sh"

for i in {1..5000}
do
	echo "Run $i th time"
	python generate_train_test.py
	IDprediction -c 0.1 -t train.csv
	IDprediction -e test.csv
done
