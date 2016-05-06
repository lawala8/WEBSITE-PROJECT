from flask import Flask, render_template
import os
app = Flask(__name__);

@app.route('/')
def home():
    return render_template('/index1.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/index1')
def blog():
    return render_template('/index1.html')
    
@app.route('/flask_sqlite')
def comments():
    return render_template('/flask_sqlite.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host='0.0.0.0', debug=True)