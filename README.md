# Logs Analysis
This project uses psql and python to retrieve data from an SQL database.

## Getting Started
you must have the news.sql file in your vagrant directory, as this program queries that database.

## Prerequisites
Two views were created  to query this database easier

### View 1: articleLogs
This view strips the *path* column from the *Log* table of the path and only leaves the article’s slug from that log.
It is used to join articles on logs using the slug.

to create this view:
```
CREATE VIEW articleLogs as
SELECT replace(path, '/article/', '')
FROM log;
```

### View 2: dayStatus
This view displays each day, the number of successful logs and number of failed logs for each day.
It is used to calculate the percentage of failed logs for each day.

to create this view:
```
CREATE VIEW dayStatus as 
SELECT time::timestamp::date as day, count(case status when '200 OK' then 1 else null end) as success, count(case status when '404 NOT FOUND' then 1 else null end) as faliure
FROM log group by day;
```

## Running this program
To run this program, download the logsanalysis.py file in your vagrant directory, run vagrant ssh, cd to /vagrant, where your news.sql file should exist, and type ` python logsanalysis.py`  to run.
