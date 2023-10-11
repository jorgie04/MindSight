from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def acc():
    return render_template("login.html")

accounts = {'jowjie':'jowjie_dev',
          'tin':'tin_dev',
          'joker':'joker_dev',
          'tet' : 'tet_UI',
          'matt' : 'matt_UI'
          }

@app.route('/login-form', methods = ['POST','GET'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username not in accounts:
        return render_template('login.html', info = 'Invalid User')
    else: 
        if accounts[username] != password:
            return render_template('login.html', info = 'Invalid Password')
        else:
            return render_template('welcome.html')
        
if __name__ == '__main__':
    app.run(debug=1, host='0.0.0.0', port=5001)
