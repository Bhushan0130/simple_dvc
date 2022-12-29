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

'''bash
git init

'''bash
dvc init

'''bash
dvc add data_given/winequality.csv

git add . 

git commit -m "first data"

one liner update for readme
git add . && git commit -m "update Readme.md"
git remote add origin https://github.com/Bhushan0130/simple_dvc.git
git branch -M main
git push origin main


tox command -
'''bash

tox
''''
for rebuilding
'''bash
tox -r
'''

pytest command
'''bash
pytest-v
'''

setup commands -
pip install -e .


'''Way to create own building packages
python setup.py sdist bdist_wheel
'''
