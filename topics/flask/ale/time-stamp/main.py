from flask import Flask, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def get_index():
    # TODO: read the list of log entries
    return render_template('index.html', log_entries=[])

@app.route('/', methods=['POST'])
def post_index():
    # TODO: add one log entry
    # TODO: read the list of log entries
    return render_template('index.html', log_entries=['jetzt!'])
