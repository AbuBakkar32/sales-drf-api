# sales-drf-api

## Installation
#### Before installation make sure you have installed python 3.9 or above version in your system

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
#### For import the data from csv file to database (Sqlite3). I have to download sqlite3.exe file from https://www.sqlite.org/download.html and then run the following command in cmd

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

----------------------------------------------------------------------------------------------------------------------------

### Generate PDF file API

```bash
GET http://127.0.0.1:8000/api/sales/v1/report/
```
### Generate CSV file API (Additional Feature Used)

```bash
GET http://127.0.0.1:8000/api/sales/v1/csv/
```

### Generate PDF file will be found inside project folder
```
salesproject/report.pdf
```
### Click on [PDF Report](https://drive.google.com/file/d/1a0mc9kDwsGUMOb9FZ4HUro53h3fjFfZJ/view?usp=sharing) to see the report

----------------------------------------------------------------------------------------------------------------------------


### Last Two question's answer pie chart and line chart attach below using the Given data
![sales_performance_pie_chart.png](salesproject%2Fsales_performance_pie_chart.png)
![sales_performance_line_chart.png](salesproject%2Fsales_performance_line_chart.png)

## Contact me
1. [Linkedin](https://www.linkedin.com/in/abu-bakkar-siddik-17b860196/) <br>
2. [Github](https://github.com/AbuBakkar32)
3. [Facebook](https://www.facebook.com/abubakkarswe)
