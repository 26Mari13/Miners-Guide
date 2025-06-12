from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/craft')
def craft():
    return render_template('craft.html')

@app.route('/brewing')
def brewing():
    return render_template('brewing.html')

@app.route('/weapons')
def weapons():
    return render_template('weapons.html')

if __name__ == '__main__':
    app.run(debug=True)
