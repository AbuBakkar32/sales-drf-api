# sales-drf-api

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Endpoints for Registration and Login

### Registration

```bash
POST http://127.0.0.1:8000/api/v1/register/
```

### Login

```bash
POST http://127.0.0.1:8000/api/v1/login/
```

## Test Case for Registration and Login
### Test case will be found inside the test.py file

```bash
python manage.py test
```

----------------------------------------------------------------------------------------------------------------------------
### For import the data from csv file to database (Sqlite3). I have to download sqlite3.exe file from https://www.sqlite.org/download.html and then run the following command in cmd

```bash
sqlite3 db.sqlite3
```
```bash
.mode csv
```
```bash
.import data.csv tasktwo_salesModel
```
### Now check your database. You will see the data is imported successfully.

----------------------------------------------------------------------------------------------------------------------------
