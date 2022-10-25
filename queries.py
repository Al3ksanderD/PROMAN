import connection


@connection.connection_handler
def get_boards(cursor):
    cursor.execute("""SELECT * FROM boards;""")
    boards = cursor.fetchall()

    return boards
    # return connection.execute_select(
    #     """
    #     SELECT * FROM boards
    #     ;
    #     """
    # )

def get_card_status(status_id):
    """
    Find the first status matching the given id
    :param status_id:
    :return: str
    """
    status = connection.execute_select(
        """
        SELECT * FROM statuses s
        WHERE s.id = %(status_id)s
        ;
        """
        , {"status_id": status_id})

    return status




def get_cards_for_board(board_id):
    cursor.execute("""SELECT * FROM cards;""")
    cards = cursor.fetchall()


    matching_cards = connection.execute_select(
        """
        SELECT * FROM cards
        WHERE cards.board_id = %(board_id)s
        ;
        """
        , {"board_id": board_id})

    return matching_cards
