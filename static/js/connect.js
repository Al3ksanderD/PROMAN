const {Pool, Client} = require('pg')

const pool = new Pool({
    user: 'atvrkdif',
    host: 'manny.db.elephantsql.com',
    database: 'atvrkdif',
    password: 'lfw6LPy8MgzV9bl0X4RIls4FLXNWg7Ff',
    port: 5432,
})

pool.query('SELECT NOW()', (err, res) => {
    console.log(err, res)
    pool.end()
})

const client = new Client({
    user: 'atvrkdif',
    host: 'manny.db.elephantsql.com',
    database: 'atvrkdif',
    password: 'lfw6LPy8MgzV9bl0X4RIls4FLXNWg7Ff',
    port: 5432,
})
function addBoard(){
client.connect()
client.query('INSERT INTO public.boards (id, title, priority, user_id)\n' +
    'VALUES (22, \'dodany z funkcji\', 0, null);\n',
    (err, res) => {
        console.log(err, res)
        client.end()
    })};

addBoard();