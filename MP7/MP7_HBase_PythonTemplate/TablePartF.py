import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
powers = connection.table('powers')

data = []
for key, value in powers.scan():
    data.append(value)

for d in data:
    for d1 in data:
        color = d[b'custom:color']
        name = d[b'professional:name']
        power = d[b'personal:power']

        color1 = d1[b'custom:color']
        name1 = d1[b'professional:name']
        power1 = d1[b'personal:power']

        if name != name1 and color == color1:
            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))



