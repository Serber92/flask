from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "idi nah"

@app.route('/')
def start_page():
  if 'visits' in session:
    session['visits'] += 1
  else:
    session['visits'] = 1
  return render_template('index.html')

@app.route('/destroy_session')
def destroy():
  session.pop('visits')
  return redirect('/')

if __name__=='__main__':
  app.run(debug=True)
