from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def main_page():
  if 'gold' not in session:
    session['gold'] = 0
  if 'history' not in session:
    session['history'] = ''
  session['cards'] = [
    {'name': 'Gendel',
    'text': 'take money from people in gendel',
    'button': 'gendel money'},
    {'name': 'Chest',
    'text': 'search in the chest',
    'button': 'find money'},
    {'name': 'Bank',
    'text': 'steal from bank',
    'button': 'robbery'},
    {'name': 'Azino777',
    'text': 'take chances with Casino',
    'button': 'Lohanutsa'}
  ]
  return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
  if request.form['which_form'] == 'Gendel':
    gold = random.randint(1, 40)
    session['gold'] += gold
    session['history'] += '<p class="earn">Earned ' + str(gold) + ' at ' + request.form['which_form'] + '</p>'
  elif request.form['which_form'] == 'Chest':
    gold = random.randint(1, 5)
    session['gold'] += gold
    session['history'] += '<p class="earn">Earned ' + str(gold) + ' at ' + request.form['which_form'] + '</p>'
  elif request.form['which_form'] == 'Bank':
    gold = random.randint(1, 20)
    session['gold'] += gold
    session['history'] += '<p class="earn">Earned ' + str(gold) + ' at ' + request.form['which_form'] + '</p>'
  elif request.form['which_form'] == 'Azino777':
    gold = random.randint(-200, 100)
    session['gold'] += gold
    if gold > 0:
      session['history'] += '<p class="earn">Earned ' + str(gold) + ' at ' + request.form['which_form'] + '</p>'
    else:
      session['history'] += '<p class="lost">Lost ' + str(gold) + ' at ' + request.form['which_form'] + '</p>'
  return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
  session.clear()
  return redirect('/')


if __name__=="__main__":
  app.run(debug=True)
