#coding=utf-8

from flask import Flask
from flask import render_template
import test

app = Flask(__name__)

cnx_cfg = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'eiac-sys',
}

@app.route('/')
def index():
  x = test.add()
  return x

@app.route('/admin')
def admin():
  return 'admin page11'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
  # show the user profile for that user
  return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  # show the post with the given id, the id is an integer
  return 'Post %d' % post_id

if __name__ == '__main__':
  app.run(port=8081, debug=True)
