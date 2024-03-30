from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if ID number is valid (for demonstration purposes)
        id_number = request.form['id']
        if len(id_number) in [8, 9] and id_number.isdigit():
            # Redirect to the index page if ID number is valid
            return redirect(url_for('index'))
        else:
            # Render the login page again with an error message if ID number is invalid
            return render_template('login.html', error="Invalid ID number. Please enter an 8 or 9-digit number.")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
