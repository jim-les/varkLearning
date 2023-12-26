from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def under_development():
    return render_template('under_development.html')

if __name__ == '__main__':
    app.run(debug=False,host='varklearning-frt6-main.zeet-jim-les-team.zeet.app')
