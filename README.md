create env

'''bash
conda create -n wineq python=3.8 -y
'''

activate env 
'''bash
conda activate wineq
'''


created a req file

install the req
'''bash
pip install -r requirements.txt
'''

download the data from
githup
'''

git init
dvc init
dvc add data_given/winequality.csv

git add . 

git commit -m "first data"

