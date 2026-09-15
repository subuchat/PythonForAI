
## create virtual environment before further developing ## 

Windows :
--------------------------------
Create :  python -m venv myenv
Activate: myenv\Scripts\activate.bat
update pip : python -m pip install --upgrade pip

 -------------------------------
** install your package within that virtual environment by 
$python -m pip install package_name

* Or if you have requirements.txt then install below way 
$ python -m pip install -r requirements.txt


* If you need to upgrade pip 
$ python -m pip install --upgrade pip

* keep all libraries and dependencies intalled within a single requirements.txt
$ python -m pip freeze > requirements.txt



## Different other package usages
Once basic data strcuture and control structure done , lets explore 
* matplotlib
* numpy
* Pandas

-- These will be very useful for Machine learning usage

## Sequence to Learn
Before you jump for AI related programming using Python , idea is to start from beginning.
You can learn here Python , also if you know - can brush up
* Start with **FundamentalOfPython** - where you can learn python programming , its control and data structures
* Now check 'ExampleOfOtherlib' , to learn matplotlib , pandas , numpy usage
  - these are very useful package for machine learning/ deep learning
* Now you can check 'MachineLearningExamples' for machine learning use cases
    - Best use colab for these files , else make virtual env
    - It contain basic of Supervised , Unsupervised learning
    - Try to understand different method to measure model outcome ( like RMSE for Regression and Accuracy for Classification)
    