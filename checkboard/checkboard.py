from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board8x8():
  return render_template("index.html", number=4)

@app.route('/<number>')
def board(number):
  number=round(int(number)/2)
  return render_template("index.html", number=number)

if __name__=="__main__":
  app.run(debug=True)