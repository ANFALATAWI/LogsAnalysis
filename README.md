# Logs Analysis
This project uses psql and python to retrieve data from the SQL *news* database.

## Getting Started
### Download the News.sql database
[news.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Install the virtual machine
Here Virtual Box + vagrant were used.
[Install Virtual Box](https://www.virtualbox.org/wiki/Downloads)
[Install Vagrant](https://www.vagrantup.com/downloads.html)
[Download the VM configuration](https://github.com/udacity/fullstack-nanodegree-vm)
run `$ vagrant up`  to set up vagrant then `$ vagrant ssh`  to log in to the Linux VM.

### Set up the files
Move the *news.sql* and *logsAnalysis.py* files to your vagrant directory.

## Prerequisites
Two views were created to query this database easier, to create these views run `$ psql news`  inside your vagrant terminal to operate on the database, then type the create view commands below:

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
SELECT time::timestamp::date as day,
count(case status when '200 OK' then 1 else null end) as success,
count(case status when '404 NOT FOUND' then 1 else null end) as faliure
FROM log
GROUP BY day;
```

## Running this program
To run this program, inside your VM run `$ vagrant ssh ` cd to /vagrant, where your news.sql and logsAnalysis.py files should exist, and type `$ python logsAnalysis.py`  to run.
