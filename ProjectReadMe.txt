View 1:
articleLogs
create view articleLogs as select replace(path, '/article/', '') from log;

Query 1:
select title, count(articleLogs.replace) as views
from articles, articleLogs
where slug = replace
group by title
order by views desc limit 3;

