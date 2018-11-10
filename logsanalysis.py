#!/usr/bin/env python2

import psycopg2


def answer(query):
        # Executing Query
    cursor.execute(query)
    # Fetching results
    return cursor.fetchall()


if __name__ == "__main__":
    DBNAME = "news"

    # Connecting to the database
    database = psycopg2.connect(database=DBNAME)

    # Getting a cursor
    cursor = database.cursor()

    # ----------------------------
    # Query 1
    # This query uses VIEW articleLogs
    query = ("SELECT title, count(articleLogs.replace) as views "
             "FROM articles, articleLogs WHERE slug = replace "
             "GROUP BY title "
             "ORDER BY views DESC "
             "LIMIT 3; ")

    results = answer(query)

    # Printing results
    print "1. What are the most popular three articles of all time?"
    for row in results:
        sentence = "Article titled '{}' has {} views.".format(row[0], row[1])
        print sentence

    # ----------------------------
    # Query 2
    results = answer("SELECT name, count(articleLogs.replace) as views "
                     "FROM articles, articleLogs, authors "
                     "WHERE slug = replace and authors.id = articles.author "
                     "GROUP BY name "
                     "ORDER BY views desc;")

    # Printing results
    print "\n2. Who are the most popular article authors of all time?"
    for row in results:
        sentence = "Author '{}' has {} views.".format(row[0], row[1])
        print sentence

    # ----------------------------
    # Query 3
    # This query uses VIEW dayStatus
    # Casting to floast was used to get an arethmatic value
    results = answer("SELECT day, "
                     "((faliure::float/ (success::float+faliure::float))*100 )"
                     " as percentage "
                     "FROM dayStatus "
                     "WHERE ( ( (success+faliure) * 0.01) <= faliure);")

    # Printing results
    print "\n3. On which days did more than 1% of requests lead to errors?"
    for row in results:
        sentence = "Day {} had {:0.2f}% of requests lead to errors.".format(
            row[0], row[1])
        print sentence

    # Closing the database
    database.close()
