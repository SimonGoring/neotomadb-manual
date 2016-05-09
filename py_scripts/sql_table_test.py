## Here we generate the output table for the SQL command.  We should be able to just copy & paste the command:

import pymysql
import sys
from tabulate import tabulate
import csv

# We connect to the database:
con = pymysql.connect(user='root', db = 'neotoma', password = 'c@mpf1re', host = 'localhost')

# We then execute the sql command:

cur = con.cursor(pymysql.cursors.DictCursor)

cur.execute("   SELECT RelativeAges.RelativeAge, RelativeAges.CalAgeYounger, \
   RelativeAges.CalAgeOlder \
   FROM RelativeAgeScales INNER JOIN RelativeAges ON \
   RelativeAgeScales.RelativeAgeScaleID = RelativeAges.RelativeAgeScaleID \
   WHERE (((RelativeAgeScales.RelativeAgeScale) = 'North American land mammal ages'));;")

result = cur.fetchall()

# And output to a csv file:

output = open('csvs/relativeage.csv', 'w', newline='')

all_keys = set().union(*(d.keys() for d in result))

wr = csv.DictWriter(output, delimiter=',', quotechar='"', fieldnames = all_keys)

wr.writeheader()

for i in result:
	wr.writerow(i)
