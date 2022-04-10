from flask import Flask, render_template, redirect, request
from skaters import Skater

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/skaters')

@app.route('/skaters')
def show_all():
    return render_template("skaters.html", skaters = Skater.display_all())

@app.route('/skater/new')
def create_skater():
    return render_template('new_skater.html')

@app.route('/skater/creator', methods = ['POST'])
def save():
    Skater.add_skater(request.form)
    return redirect('/skaters')
    

if __name__ == "__main__":
    app.run(debug=True)