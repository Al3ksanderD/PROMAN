import connection


@connection.connection_handler
def get_boards():
    """
    Gather all boards
    :return:
    """

    return connection.execute_select(
        """
        SELECT * FROM boards
        WHERE user_id IS NULL 
        ;
        """
        , fetchall=True)


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
        WHERE id = %(b_id)s
        """, {"b_id": board_id})
