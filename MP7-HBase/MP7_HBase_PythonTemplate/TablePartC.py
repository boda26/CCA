import happybase as hb
import csv

f = open('input.csv', 'r')
f = csv.reader(f)

connection = hb.Connection()
powers = connection.table('powers')

b = powers.batch()
for row in f:
    # print(row)
    b.put(row[0], {
        'personal:hero': row[1],
        'personal:power': row[2],
        'professional:name': row[3],
        'professional:xp': row[4],
        'custom:color': row[5]
    })

b.send()

