from main import app
from flask import render_template, request, make_response
from util import json_response
import mimetypes
from queries import card_queries

mimetypes.add_type('application/javascript', '.js')
app.secret_key = 'lubie0placki'


@app.route("/api/cards")
@json_response
def get_all_cards():
    return card_queries.get_cards()


@app.route("/api/boards/<int:board_id>/cards/")
@json_response
def get_cards_for_board(board_id: int):
    return card_queries.get_cards_for_board(board_id)


@app.route("/api/boards/<int:board_id>/cards/add", methods=["POST"])
def add_card(board_id: int):
    card = request.json
    card_queries.add_card(card, board_id)

    return render_template("index.html")


@app.route("/api/cards/<int:card_id>/update", methods=["PUT"])
def rename_card_name(card_id: int):
    new_card_name = request.json
    card_queries.rename_card_name(card_id, new_card_name)

    return render_template('index.html')


@app.route("/api/cards/delete/<int:card_id>", methods=["DELETE"])
def delete_card(card_id):
    card_queries.delete_card(card_id)

    return make_response("201")
