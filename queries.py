import connection


# BOARD__________________________________________________________________________________________________-
@connection.connection_handler
def get_boards(cursor):
    cursor.execute("""SELECT id,title,priority FROM boards WHERE user_id IS NULL """)
    boards = cursor.fetchall()
    return boards


@connection.connection_handler
def get_private_boards(user_id):
    return connection.execute_select(
        """
        SELECT * FROM boards
        WHERE user_id = %(user_id)s
        ;
        """
        , {"user_id": user_id}, fetchall=True)


@connection.connection_handler
def add_board(title):
    board_id = connection.execute_select(
        """
        INSERT INTO boards (title)
        VALUES (%(title)s)
        RETURNING id;
        """,
        {"title": title}, False
    )
    return board_id


@connection.connection_handler
def rename_board(board, board_id):
    connection.execute_query(
        """UPDATE boards
           set title = %s
           WHERE id = %s;"""
        , (board["title"], board_id))


@connection.connection_handler
def delete_board(board_id):
    return connection.execute_query(
        """
        DELETE FROM boards
        WHERE id = %(board_id)s
        """, {"board_id": board_id})


# CARDS___________________________________________________________________________________________________


@connection.connection_handler
def get_cards_for_board(cursor, board_id):
    cursor.execute(
        """
        SELECT * FROM cards
        WHERE cards.board_id = %(board_id)s
        ORDER BY card_order 
        ;
        """
        , {"board_id": board_id})
    cards = cursor.fetchall()

    return cards


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
    connection.execute_query(
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


# @connection.connection_handler
# @app.route("/api/cards/<int:card_id>/update", methods=["PUT"])
# def update_card_name(card_id: int):
#     new_card_name = request.json
#     update_card_name(card_id, new_card_name)
#
#     return render_template('index.html')
#

# STATUS____________________________________________________________________________________________________

@connection.connection_handler
def get_card_status(status_id):
    status = connection.execute_select(
        """
        SELECT * FROM statuses s
        WHERE s.id = %(status_id)s
        ;
        """
        , {"status_id": status_id})

    return status


@connection.connection_handler
def get_statuses():
    return connection.execute_select(
        """SELECT * FROM statuses
        ORDER BY id 
        ;
        """
    )


@connection.connection_handler
def add_status(title, board_id):
    connection.execute_query(
        """
        INSERT INTO statuses (title, board_id)
        VALUES (%(title)s, %(board_id)s)
        """,
        {"title": title,
         "board_id": board_id
         }
    )


@connection.connection_handler
def rename_status(status, status_id):
    connection.execute_query(
        """UPDATE statuses
           set title = %s
           WHERE id = %s;"""
        , (status["title"], status_id))


@connection.connection_handler
def update_status_id(new_status_id, card_id, status_id):
    connection.execute_query(
        """
        UPDATE cards
        set status_id = %s
        WHERE (id = %s AND status_id = %s);
        """
        , (new_status_id, card_id, status_id))


@connection.connection_handler
def delete_status(status_id):
    return connection.execute_query(
        """
        DELETE FROM statuses
        WHERE id = %(status_id)s        
        """, {"status_id": status_id})
