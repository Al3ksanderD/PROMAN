import os
import psycopg2
import psycopg2.extras


def get_connection_string():
    # # setup connection string for localhost

    # # to do this, please define these environment variables first
    # user_name = os.environ.get('PSQL_USER_NAME')
    # password = os.environ.get('PSQL_PASSWORD')
    # host = os.environ.get('PSQL_HOST')
    # database_name = os.environ.get('PSQL_DB_NAME')
    #
    # env_variables_defined = user_name and password and host and database_name
    #
    # if env_variables_defined:
    #     # this string describes all info for psycopg2 to connect to the database
    #     return 'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
    #         user_name=user_name,
    #         password=password,
    #         host=host,
    #         database_name=database_name
    #     )
    # else:
    #     raise KeyError('Some necessary environment variable(s) are not defined')
    # for elephantSQL database
    return 'postgres://atvrkdif:lfw6LPy8MgzV9bl0X4RIls4FLXNWg7Ff@manny.db.elephantsql.com/atvrkdif'


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        # we set the cursor_factory parameter to return with a RealDictCursor cursor (cursor which provide dictionaries)
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value

    return wrapper


def connect_login():
    DB_HOST = "manny.db.elephantsql.com"
    DB_NAME = "atvrkdif"
    DB_USER = "atvrkdif"
    DB_PASS = "lfw6LPy8MgzV9bl0X4RIls4FLXNWg7Ff"

    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
