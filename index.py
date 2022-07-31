from random import random
from flask import *
import mysql.connector
import random

app = Flask(__name__)
conn = mysql.connector.connect(host = "localhost",user = "root",password = "**************",database = "tinyurl")
cursor = conn.cursor()
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        url = request.form.get("url")
        encoded_url = "127.0.0.1:8080/"
        for i in range(0,10):
            encoded_url += key[random.randint(0,len(key)-1)]
        query = 'insert into urls(url,encoded_url) values("{}","{}")'.format(url,encoded_url)
        cursor.execute(query)
        conn.commit()
        return render_template("index.html",resp = "Requested url: \n"+encoded_url)

@app.route("/<url>")
def redirect(url):
    url = "127.0.0.1:8080/"+str(url)
    query = "select url from urls where encoded_url='{}';".format(url)
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data)!=0:
        return """<script>function Redirect() {{
               window.location = "{}";
            }}            
            document.write("You will be redirected to login page in 1 sec.");
            setTimeout('Redirect()', 1000);</script>""".format(str(data[0][0]))
    return render_template("index.html",resp = "Requested url Does'nt exist!!!")


if __name__ == "__main__":
    app.run("127.0.0.1",8080)
    cursor.close()