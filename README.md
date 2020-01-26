# Employee Portal

Simple portal to add, edit, seach and view details of an employee

## Requirements

Python 2.7+

## Installation
Steps:
1) Create a virtual environment. Use the below command:
```python
python -m venv ./venv

2) Activate virtual environment. Use the below command:
```python
Linux -> source venv/bin/activate
Windows -> venv\Scripts\activate.bat

3) Install the required dependencies using requirements.txt. Use the below command:
```python
pip install requirements.txt

4) Migrate the models. Use the below command:
```python
python manage.py makemigrations
python manage.py migrate

5) Collect the static files. Use the below command:
```python
python manage.py collectstatic

6) Run the server. Use the below command:
```python
python manage.py runserver

## Usage

Run the server and open localhost:8000 to view the portal