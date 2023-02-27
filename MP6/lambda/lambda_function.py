import json
import sys
import redis
import pymysql


DB_HOST = "mp6db-instance-1.cnag5gqfiq7a.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASS = "12345678"
DB_NAME = "mp6"
DB_TABLE = "heroes"
REDIS_URL = "redis://mp6cluster.ycbdub.ng.0001.use1.cache.amazonaws.com:6379"

TTL = 10

class DB:
    def __init__(self, **params):
        params.setdefault("charset", "utf8mb4")
        params.setdefault("cursorclass", pymysql.cursors.DictCursor)

        self.mysql = pymysql.connect(**params)

    def query(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_idx(self, table_name):
        with self.mysql.cursor() as cursor:
            cursor.execute(f"SELECT MAX(id) as id FROM {table_name}")
            idx = str(cursor.fetchone()['id'] + 1)
            return idx

    def insert(self, idx, data):
        with self.mysql.cursor() as cursor:
            hero = data["hero"]
            power = data["power"]
            name = data["name"]
            xp = data["xp"]
            color = data["color"]
            
            sql = f"INSERT INTO herostb (`id`, `hero`, `power`, `name`, `xp`, `color`) VALUES ('{idx}', '{hero}', '{power}', '{name}', '{xp}', '{color}')"

            cursor.execute(sql)
            self.mysql.commit()

def read(use_cache, indices, Database, Cache):
    res = []
    cached = {}
    for i in indices:
        if use_cache:
            data = Cache.get(i)
            if data:
                res.append(json.loads(data))
                cached[i] = True
        if not use_cache or data == None:
            sql = f'SELECT * FROM heroes WHERE id={i}'
            data = Database.query(sql)
            if data:
                res.append(data[0])
                cached[i] = False
                Cache.set(i, json.dumps(data[0]))

    
def write(use_cache, sqls, Database, Cache):
    for sql in sqls:
        idx = Database.get_idx('heroes')
        sql['id'] = idx
        Database.insert(idx=idx, data=sql)
        if use_cache:
            Cache.set(idx, json.dumps(sql))


def lambda_handler(event, context):
    
    USE_CACHE = (event['USE_CACHE'] == "True")
    REQUEST = event['REQUEST']
    
    # initialize database and cache
    try:
        Database = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit()
        
    Cache = redis.Redis.from_url(REDIS_URL)
    
    result = []
    if REQUEST == "read":
        # event["SQLS"] should be a list of integers
        result = read(USE_CACHE, event["SQLS"], Database, Cache)
    elif REQUEST == "write":
        # event["SQLS"] should be a list of jsons
        write(USE_CACHE, event["SQLS"], Database, Cache)
        result = "write success"
    
    
    return {
        'statusCode': 200,
        'body': result
    }