echo
echo 'WELCOME TO THE PREDICTIVE WORLD '
echo 
echo

cd $HOME
code_direcotry=$IDCODE
# echo "Current path is : $Initial_location"

#chnaging and storing path
cd $code_direcotry
echo $IDCODE'filelocation.txt'
curr_location=$(<$IDCODE/filelocation.txt) 
cd ./src


error_criteria=0.05 #Tree:erroe based clustering criteria
significance_level=0.05 #significance level
elimination='False' #elimination default set as Flase
limited_ref_points='False'

#ALL OPTARG is file name 
#it is useful to initialize variable based on the flag passed
while getopts "c:b:a:h:m:t:e:k:f:p:r:s:d:o:l:" arg; do
  case $arg in
    c) 
        flag_passed='-c'
        error_criteria="$OPTARG"
        echo "For Error based clustering, defined criteria :  $error_criteria "
        echo
        ;;
    b)
        flag_passed='-b'
        echo "Type of Bonds in fuel : " 
        fuel_SMILE="$OPTARG"
        echo
        ;;    
    a)
        flag_passed='-a'
        echo "Manual Analysis of fuel-dataset given range of parameter:"
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    h)
        flag_passed='-h'
        echo "Histogram plots of parameters:"
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    m)
        flag_passed='-m'
        echo "Multiple Linear Regression:"
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    t)
        flag_passed='-t'
        #removing old directory
        rm -rf "$curr_location/object_file"
        rm -rf "$curr_location/plots"

        echo "Generate cluster and Training/Testing the model based on tree"
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    e)
        flag_passed='-e'
        echo "External Data passsed to predict the Ignition Delay"
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    k)
        flag_passed='-k'
        echo "External Data passsed to predict the Ignition Delay and to store result seperately"
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    f)
        flag_passed='-f'
        echo "Plotting of all test result"
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    p)  
        flag_passed='-p'
        echo "Plot of average coeffcient value obtained by histogram of coeffcients"
        dataset_location="$curr_location/$OPTARG"
        echo $dataset_location
        echo
        ;;
    r)
        flag_passed='-r'
        echo "Eliminiation of feature set as True"
        elimination=$OPTARG
        echo
        ;;
    l)
        flag_passed='-l'
        echo "Refrence Points are limited by features"
        limited_ref_points=$OPTARG
        echo
        ;;
    s)
        flag_passed='-s'
        significance_level=$OPTARG
        echo "Significance level for backward eliminatio : $significance_level"
        echo
        ;;
    d)
        flag_passed='-d'
        echo 'Generating dataset with transformed feature'
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    o)
        flag_passed='-o'
        #removing old directory
        rm -rf "$curr_location/object_file"
        rm -rf "$curr_location/plots"
        echo "Generate cluster and Training/Testing the model based on tree NOT FOR DEFAULT FUEL"
        dataset_location="$curr_location/$OPTARG"
        echo
        ;;
    ?)
        echo "Wrong argument passed : "
        echo " -c : Critria for error based clustering"
        echo " -b : Bond analysis in the Fuel "
        echo " -a : Analysis for fuel parameters"
        echo " -h : Hiatogram Plots"
        echo " -m : Multiple linear regression"
        echo " -t : Tree based and regression"
        echo " -e : External fuel analysis"
        echo " -f : Plot histogram of all the result"
        echo " -k : External fuel analysis saving all the result"
        echo " -p : plotting of coefficient to find Average values"
        echo " -r : Backward elimination Activation True/False"
        echo " -s : Significance Level for Backward Elimination"
        echo " -o : Other Dataset than fuel if dataset is ready"
        echo " -d : Dataset generation ONLY for fuel contaning SMILES"
  esac
done

########################################################
################Common Function or Ploting #############
########################################################
plotting_fucntion () {
    #moving to plots folder

    cd "$curr_location/plots/"


    #gnerating pdf from tex file 
    # pdflatex Training.tex > /dev/null 2>&1  #to not print output 
    #opeing the pdf file 
    # xdg-open Training.pdf
    echo 'Plotting of Training done'

    # pdflatex Testing.tex > /dev/null 2>&1
    # xdg-open Testing.pdf
    # echo 'Plotting of Testing done'

    # pdflatex Datasize.tex > /dev/null 2>&1
    # xdg-open Datasize.pdf
    echo 'Plotting of Datasize done'

    # pdflatex MaxRelError.tex > /dev/null 2>&1
    # xdg-open MaxRelError.pdf
    echo 'Plotting of MaxRelError done'

    # pdflatex ChildLabel.tex > /dev/null 2>&1
    # xdg-open ChildLabel.pdf
    echo 'Plotting of Labels done'

    cd 
    cd $code_direcotry
    cd ./src

    python coef_tikz_compatible.py "$curr_location/plots/"
    # python Fuel_tikz_compatible.py "$curr_location/plots/"

    dir_to_plot="$curr_location/plots/"
    cd $dir_to_plot
    # pdflatex coefficient.tex > /dev/null 2>&1
    # xdg-open coefficient.pdf
    echo 'Plotting of Coefficients done'

    #in plotting dir, deleting all files except .pdf
    find $dir_to_plot  -name '*.aux' -delete
    find $dir_to_plot  -name '*.tex' -delete
    find $dir_to_plot  -name '*.log' -delete


    # pdflatex FuelsTrainingTesting.tex > /dev/null 2>&1
    # xdg-open FuelsTrainingTesting.pdf
}



################################################
# BASED ON FLAG, IT WILL RUN THE PYTHON SCRIPT #
################################################

##Analysis of fuel dataset
if [ $flag_passed == '-a' ]
then
python DDS.py -a $dataset_location  $curr_location
fi

if [ $flag_passed == '-d' ]
then
python DDS.py -d $dataset_location  $curr_location
fi

if [ $flag_passed == '-b' ]
then
python DDS.py -b $fuel_SMILE $curr_location #SMILE will passed in place of dataset location
echo 'done'
fi

##Histogram plots of data 
if [ $flag_passed == '-h' ]
then
python DDS.py -h $dataset_location $curr_location
fi

##Multiple regression 
if [ $flag_passed == '-m' ]
then
python DDS.py -m $dataset_location $curr_location $elimination $significance_level
fi

if [ $flag_passed == '-t' ]
then
python DDS.py -t $dataset_location $curr_location $error_criteria $elimination $significance_level $limited_ref_points
# plotting_fucntion
fi

#################################
#################################
#other than fuel data set if dataset 
#ready you just want to generate model
#feature selection will be different

if [ $flag_passed == '-o' ]
then
python DDS.py -o $dataset_location $curr_location $error_criteria $elimination $significance_level $limited_ref_points
plotting_fucntion
fi

####Extrenal test
if [ $flag_passed == '-e' ]
then
python DDS.py -e $dataset_location $curr_location
echo 'done'
fi

if [ $flag_passed == '-k' ]
then
python DDS.py -k $dataset_location $curr_location
echo 'done'
fi

if [ $flag_passed == '-f' ]
then
python DDS.py -f $dataset_location $curr_location
echo 'done'
fi


if [ $flag_passed == '-p' ]
then
python DDS.py -p $dataset_location $curr_location
echo 'done'
fi



echo 
echo
echo
echo "Compilation Successful!!  Keep Smiling :) "

cd 
cd $code_direcotry
#removing file
rm filelocation.txt