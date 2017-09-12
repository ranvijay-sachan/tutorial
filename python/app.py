import os

from flask import Flask, request, render_template

from network.parse_passwd import get_remote_user_info

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login_form.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        data = get_remote_user_info(request.form['host'], request.form['username'], request.form['password'])
        return render_template('result.html', result=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
