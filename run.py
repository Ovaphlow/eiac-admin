#coding=utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Index page!'

@app.route('/admin')
def admin():
  return 'admin page'

if __name__ == '__main__':
  app.run(port=8081)
