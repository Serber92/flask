from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'idi nah'

@app.route('/')
def index():
  if 'main_number' not in session:
    session['main_number'] = random.randint(1,100)
  return render_template('index.html')

if __name__=="__main__":
  app.run(debug=True)