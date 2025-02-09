from flask import Flask

app = Flask(__name__)

#adding end point/route
@app.route('/')
def index():
   return "<h1>Index page</h1>"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8081, debug=True)