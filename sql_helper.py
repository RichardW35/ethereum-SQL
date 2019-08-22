def create_database(cur):
    """ create the schema for the database"""
    foreverstrong = """
    CREATE TABLE IF NOT EXISTS Foreverstrong (
     blockNumber INTEGER, 
     sender TEXT,
     nonce INTEGER, 
     recipient TEXT,
     txHash TEXT PRIMARY KEY,
     value TEXT);"""

    cur.execute(foreverstrong)


def create_index(cur):
    foreverstrong = "CREATE INDEX index_foreverstrong ON Foreverstrong(value, sender, recipient);"

    cur.execute(foreverstrong)


def update_database(cur, table_foreverstrong):
    """ write lists of dictionaries into the database"""
    foreverstrong = """INSERT INTO Foreverstrong VALUES (:blockNumber, :from, :nonce, :to, :txHash, :value); """
    cur.executemany(foreverstrong, table_foreverstrong)
