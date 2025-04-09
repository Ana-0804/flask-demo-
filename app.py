from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret-key-demo-app'

# Dummy in-memory database
messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')
    if name and message:
        messages.append({'name': name, 'message': message})
        flash('Message submitted successfully!')
    else:
        flash('Both name and message are required.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
