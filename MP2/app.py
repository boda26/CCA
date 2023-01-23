from flask import Flask, request
app = Flask(__name__)

myseed = 0

@app.route('/', methods = ['POST', 'GET'])
def myapp():
    global myseed
    if request.method == 'POST':
        myseed = request.json.get('num')
        myseed = int(myseed)
        print('POST: ' + str(myseed))
        return str(myseed)
    else:
        print('GET: ' + str(myseed))
        return str(myseed)
