import connection
from psycopg2.extras import RealDictCursor

@connection.connection_handler
def get_boards(cursor):
    cursor.execute("""SELECT * FROM boards;""")
    boards = cursor.fetchall()

    return boards


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



@connection.connection_handler
def get_cards_from_board(cursor: RealDictCursor, board_id):
    query = """
            SELECT *
            FROM cards
            WHERE cards.board_id = %(board_id)s
            ORDER BY id;
            """

    cursor.execute(query, {'board_id': board_id})
    return cursor.fetchall()

@connection.connection_handler
def add_new_board(cursor: RealDictCursor, new_board_title):
    query = """
            INSERT INTO boards(title) 
            VALUES (%(new_board_title)s)
            returning id, title;
            """

    cursor.execute(query, {'new_board_title': new_board_title})
    new_board_id = cursor.fetchall()
    return new_board_id
