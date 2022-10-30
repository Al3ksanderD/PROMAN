from main import app
from flask import render_template, request, make_response
from util import json_response
import mimetypes
from queries import board_queries

mimetypes.add_type('application/javascript', '.js')
app.secret_key = 'lubie0placki'


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
    return board_queries.get_boards()


@app.route("/api/boards/<int:board_id>", methods=["PUT"])
def rename_board(board_id: int):
    """
    Update the specific board according to its id
    """
    new_title = request.json
    board_queries.rename_board(new_title, board_id)
    return render_template('index.html')


@app.route("/api/boards/add", methods=["POST"])
@json_response
def add_board():
    board = request.json
    board_title = board["title"]
    board_id = board_queries.add_board(board_title)
    return board_id


@app.route("/api/boards/delete/<int:board_id>", methods=["DELETE"])
def delete_board(board_id):
    board_queries.delete_board(board_id)

    return make_response("404")
