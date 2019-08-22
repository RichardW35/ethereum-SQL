def get_block_data(block, web3):
    """ build a block table to be compatible with SQLite data types"""
    block_data = web3.eth.getBlock(block)

    return block_data


def order_table_foreverstrong(hashh, block, web3, balance=False):

    #open transaction data
    tx_data = web3.eth.getTransaction(hashh)

    #get addresses
    addr_from = tx_data['from']
    addr_to = tx_data['to']

    #build a foreverstrong table
    foreverstrong_table = {}
    foreverstrong_keys = [
        'from', 'to', 'value', 'hash', 'nonce', 'blockNumber'
    ]

    #convert types to be SQLite-compatible
    for nn in foreverstrong_keys:
        if nn == "hash":
            foreverstrong_table["txHash"] = web3.toHex(tx_data[nn])
        elif nn == "value":
            foreverstrong_table["value"] = str(tx_data[nn])
        else:
            foreverstrong_table[nn] = tx_data[nn]

    return foreverstrong_table


def execute_sql(table_foreverstrong):
    import os
    from sql_helper import create_database, update_database, create_index
    import sqlite3 as sq3

    db_name = 'blockchain.db'
    db_is_new = not os.path.exists(db_name)

    #connect to the database
    conn = sq3.connect(db_name)  # or use :memory: to put it in RAM
    cur = conn.cursor()

    if db_is_new:
        print('Creating a new DB.')
        create_database(cur)
        create_index(cur)
        update_database(cur, table_foreverstrong)
    else:
        update_database(cur, table_foreverstrong)
    conn.commit()
    conn.close()
