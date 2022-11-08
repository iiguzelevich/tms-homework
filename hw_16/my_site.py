from flask import Flask
from flask import render_template

app = Flask(__name__)

menu = [{"name": "About", "url": "about"},
        {"name": "Information", "url": "information"},
        {"name": "Users", "url": "users"},
        {"name": "Feedback", "url": "feedback"}]


@app.route('/')
def main():
    return render_template('main.html', title='My site', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/feedback')
def write_to_us():
    return render_template('write_to_us.html', title='Feedback')


@app.route('/information')
def get_information():
    return render_template('information.html', title='Information')


@app.errorhandler(404)
def not_found(error):
    return render_template('page404.html')


if __name__ == '__main__':
    app.run(debug=True)
