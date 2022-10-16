import django
print(django.get_version())
import os, sys
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import re

load_dotenv()
app = django(__name__)

if __name__ == '__main__':
    app.run(debug=True)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )
print(mydb)
    

    
@app.route('/main')
def index():
    return render_template('home.html', title="Girls Who Hack", url=os.getenv("URL"))

@app.route('/')
def Resources():
    return render_template('rsources.html')

