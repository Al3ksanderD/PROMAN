from flask import Flask, render_template, url_for, session, flash, request, redirect, jsonify
from dotenv import load_dotenv
from util import json_response
import mimetypes
import queries
from connection import connect_login
import psycopg2.extras
import re
from werkzeug.security import generate_password_hash, check_password_hash
import connection

mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)
load_dotenv()
app.secret_key = 'lubie0placki'




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display/<board_id>')
def display(board_id):

    boards = queries.get_boards()
    cards = queries.get_cards_for_board(board_id)
    return render_template('display.html', boards=boards, cards=cards)


# BOARD____________________________________________________________________________________________-

@app.route("/board")
def display_board():
    return render_template('board.html', title="ProMan Board!")


# @app.route("/api/boards/private")
# @json_response
# def get_private_boards():
#     """
#     All the private boards
#     """
#     user_id = request.args['user']
#     return queires.get_private_boards(user_id)


@app.route("/api/boards")
@json_response
def get_boards():
    """
    All the public boards
    """
    return queries.get_boards()


@app.route("/api/boards/<int:board_id>", methods=["PUT"])
def rename_board(board_id: int):
    new_title = request.json
    queries.rename_board(new_title, board_id)
    return render_template('index.html')


@app.route("/api/boards/add", methods=["POST"])
@json_response
def add_board():
    board = request.json
    board_title = board["title"]
    board_id = queries.add_board(board_title)
    return board_id


@app.route("/api/boards/delete/<int:board_id>", methods=["DELETE"])
def delete_board(board_id):
    queries.delete_board(board_id)

    return make_response("404")


# CARDS______________________________________________________________________________________________________


@app.route("/api/cards")
@json_response
def get_all_cards():
    return queries.get_cards()


@app.route("/api/boards/<int:board_id>/cards/")
@json_response
def get_cards_for_board(board_id: int):
    return queries.get_cards_for_board(board_id)


@app.route("/api/boards/<int:board_id>/cards/add", methods=["POST"])
def add_card(board_id: int):
    card = request.json
    queries.add_card(card, board_id)

    return render_template("index.html")


@app.route("/api/cards/<int:card_id>/update", methods=["PUT"])
def rename_card_name(card_id: int):
    new_card_name = request.json
    queries.rename_card_name(card_id, new_card_name)

    return render_template('index.html')


@app.route("/api/cards/delete/<int:card_id>", methods=["DELETE"])
def delete_card(card_id):
    queries.delete_card(card_id)

    return make_response("201")


# STATUS_________________________________________________________________________________________________

@app.route("/api/statuses")
@json_response
def get_statuses():
    return queries.get_statuses()


@app.route("/api/statuses/<int:status_id>", methods=["PUT"])
def update_status_title(status_id: int):
    new_title = request.json
    queries.rename_status(new_title, status_id)
    return redirect("/")


@app.route("/api/cards/<int:card_id>/update/<int:status_id>", methods=["PUT"])
def update_status_id(card_id: int, status_id: int):
    """
    Update the status_id of a card
    """
    new_status_id_dict = request.json
    new_status_id = new_status_id_dict["new_status_id"]
    queries.update_status_id(new_status_id, card_id, status_id)
    return render_template('index.html')


@app.route("/api/statuses/add", methods=["POST"])
def create_status():
    status = request.json
    title = status["title"]
    board_id = status["board_id"]
    queries.add_status(title, board_id)

    return redirect("/")


@app.route("/api/statuses/delete/<int:status_id>", methods=["DELETE"])
def delete_status(status_id):
    queries.delete_status(status_id)

    return make_response("201")


# REGISTER/LOGIN MODULE____________________________________________________________________________________________
conn = connect_login()


def home():
    if 'loggedin' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(password)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            password_rs = account['password']
            print(password_rs)
            if check_password_hash(password_rs, password):
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                return redirect(url_for('index'))
            else:
                flash('Incorrect username/password')
        else:
            flash('Incorrect username/password')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        _hashed_password = generate_password_hash(password)

        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account)

        if account:
            flash('Account already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers!')
        elif not username or not password or not email:
            flash('Please fill out the form!')
        else:
            cursor.execute("INSERT INTO users (fullname, username, password, email) VALUES (%s,%s,%s,%s)",
                           (fullname, username, _hashed_password, email))
            conn.commit()
            flash('You have successfully registered!')
    elif request.method == 'POST':

        flash('Please fill out the form!')

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id = %s', [session['id']])
        account = cursor.fetchone()
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))


def login_required(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        if 'id' in session:
            return function(*args, **kwargs)
        else:
            flash("You are not logged in")
            return redirect(url_for('login'))

    return wrap


def already_logged_in(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        if 'id' not in session:
            return function(*args, **kwargs)
        else:
            flash(f"You are already logged in, {session['username']}")
            return redirect(url_for('login_page'))

    return wrap


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
