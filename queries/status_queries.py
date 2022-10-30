import connection


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
        ORDER BY id ASC
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
