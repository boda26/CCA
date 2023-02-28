import happybase as hb

connection = hb.Connection()
connection.open()

for t in connection.tables():
    connection.delete_table(t, disable=True)

connection.create_table(
    'powers',
    {
        'personal': {},
        'professional': {},
        'custom': {}
    }
)

connection.create_table(
    'food',
    {
        'nutrition': {},
        'taste': {}
    }
)
