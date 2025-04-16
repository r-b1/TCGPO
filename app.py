from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary "database" (we'll upgrade this later)
users = {}
items_for_trade = []
wanted_items = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('dashboard'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
