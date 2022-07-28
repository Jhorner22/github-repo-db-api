import json
from flask import Flask
import pymongo
from pymongo.server_api import ServerApi

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'hello':'world'})

@app.route('/testadd')
def testadd():
    db = dbconnect()
    db.repos.tests.insert_one({'test':'test1'})
    return "added"

def dbconnect():
    print("connecting")
    password =  "!password123"
    client = pymongo.MongoClient(f"mongodb+srv://user2:{password}@cluster0.qfxug.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client.test
    return db

    


if __name__ == '__main__':
    app.run()