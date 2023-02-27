from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

version = '1.0.0'

@app.route('/')
def index():
    return render_template('index.html', version=version)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Do something with the data, e.g. send an email
        return redirect(url_for('thanks'))
    else:
        return render_template('contact.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000)
