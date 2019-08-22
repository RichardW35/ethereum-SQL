from web3 import Web3
from organize import *
import time

web3 = Web3(
    Web3.HTTPProvider(
        "https://mainnet.infura.io/v3/84d9161814614d6ea5fbd81ec41fecaa"))

# 2. connection to local node
#web3 = Web3(Web3.IPCProvider('/your-path-to/geth.ipc'))

# load a block.
Nblocks = 100
output_every = 2
start_time = time.time()
try:
    with open('lastblock.txt', 'r') as f:
        start = int(f.read()) + 1
except FileNotFoundError:
    start = 2000000

#define tables that will go to the SQLite database
table_foreverstrong = []

count = 0
#loop over all blocks
for block in range(start, start + Nblocks):

    block_data = get_block_data(block, web3)

    #all transactions on the block
    for hashh in block_data['transactions']:
        #print(web3.toHex(hashh))
        foreverstrong_table = order_table_foreverstrong(hashh, block, web3)
        table_foreverstrong.append(foreverstrong_table)
    count = count + 1
    #print(count)

    if (count % output_every) == 0:
        execute_sql(table_foreverstrong)

        del table_foreverstrong

        table_foreverstrong = []

        #update the current block number to a file
        with open('lastblock.txt', 'w') as f:
            f.write("%d" % block)
    if (count % 10) == 0:
        end = time.time()
        with open('timeperXblocks.txt', 'a') as f:
            f.write("%d %f \n" % (block, end - start_time))
    if (count % 2) == 0:
        print("2 new blocks completed.")