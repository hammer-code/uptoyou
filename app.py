from flask import Flask, render_template,url_for
app = Flask(__name__)
app.config.from_object('config');

@app.route('/')
def index():
   return render_template('depan.html')

@app.route('/say')
def say():
   return render_template('say.html')

if __name__ == '__main__':
   app.run(debug = True)
