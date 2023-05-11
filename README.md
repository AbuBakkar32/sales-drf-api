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
POST http://127.0.0.1:8000/api/auth/v1/register/
```

### Login

```bash
POST http://127.0.0.1:8000/api/auth/v1/login/
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
## API Endpoints for "data insertion and manipulation" of sales model for app tasktwo

### Insertion and get list of data

```bash
POST http://127.0.0.1:8000/api/sales/v1/sales
```

### Update, Delete and get single data

```bash
PUT http://127.0.0.1:8000/api/sales/v1/sales/1
```

```bash
DELETE http://127.0.0.1:8000/api/sales/v1/sales/1
```

```bash
GET http://127.0.0.1:8000/api/sales/v1/sales/1
```
