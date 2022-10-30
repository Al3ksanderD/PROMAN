import connection


@connection.connection_handler
def get_cards_for_board(board_id):
    matching_cards = data_manager.execute_select(
        """
        SELECT * FROM cards
        WHERE cards.board_id = %(board_id)s
        ORDER BY card_order 
        ;
        """
        , {"board_id": board_id})

    return matching_cards


@connection.connection_handler
def add_card(card, board_id):
    connection.execute_query(
        """INSERT INTO cards (board_id, status_id, title, card_order)
        VALUES (%(board_id)s, %(status_id)s, %(title)s, %(card_order)s)
        """,
        {"title": card["title"],
         "board_id": board_id,
         "status_id": card["status_id"],
         "card_order": card["card_order"]})


@connection.connection_handler
def delete_card(card_id):
    data_manager.execute_query(
        """
        DELETE FROM cards
        WHERE id = %(id)s
        """,
        {"id": card_id})


@connection.connection_handler
def rename_card_name(card_id, new_card_name):
    return connection.execute_query(
        """
        UPDATE cards
        set title = %(new_card_name)s
        WHERE id = %(card_id)s;
        """, {"new_card_name": new_card_name["title"],
              "card_id": card_id
              }
    )
