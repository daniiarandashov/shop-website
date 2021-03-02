sudo apt-get install python3
sudo apt-get install virtualenv
virtualenv venv --python=python3
. venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver