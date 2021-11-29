# CompactURL
Compact long URL to shortener one

# Virtual environments
recommend working with virtual environments when building apps with Django
# Check Package in virtual environments
pip freeze

# Or Package we need 
asgiref==3.4.1
autopep8==1.6.0
Django==3.2.9
pycodestyle==2.8.0
pytz==2021.3
sqlparse==0.4.2
toml==0.10.2

# Built virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Make and run the migrations
python3 manage.py makemigrations <br/>
python3 manage.py migrate 

# Run the application
python3 manage.py runserver [addport]

# Run the test
python3 manage.py test  
