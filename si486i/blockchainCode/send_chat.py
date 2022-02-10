from BlockTools import *
from BlockchainErrors import *
from json import dumps
from show_chat import FetchService
from requests import get
from requests.exceptions import ConnectionError
import sys
# Package import to work on windows and linux
try:
    sys.path.append("C:\classes")
    sys.path.append("D:\classes")
    from Toolchain.terminal import *
except ModuleNotFoundError:
    sys.path.append("/home/m226252/classes")
    from Toolchain.terminal import *


class Node:

    def __init__(self):
        self.peers = list(map(lambda x : x.strip(),open("hosts.txt",'r').readlines()))
        self.peer_nodes = {host : {'length' : 0, 'host' : None, 'fetcher' : None, 'head' : None} for host in self.peers}

        self.top_peer = self.peers[0]
        self.check_peer_servers()

    def check_peer_servers(self):

        # Checkk the state of all peer nodes
        printc(f"Checking Peer Nodes",BLUE)
        for host in self.peers:
            # Info
            printc(f"\tTrying to connect to host: {host}", TAN)

            # Attempt to get the head hash that the peer is on
            try:
                head_hash = get(f"http://{host}:5002/head", timeout=3).content.decode()
                self.peer_nodes[host]['head'] = head_hash

            except ConnectionError:
                printc(f"\tError in get request on host {host} - unknown reason\n\n",RED)
                continue

            except ConnectionRefusedError:
                printc(f"\tError in get request on host {host} - refused\n\n",RED)
                continue

            # Attempt to fetch the blockchain of that node
            try:
                # Grab the blockchain
                node_fetcher = FetchService(host=host,port=5002)
                node_fetcher.fetch_blockchain()

                # Assign the fetcher to the node
                self.peer_nodes[host]['fetcher'] = node_fetcher

                # Get info on the chain
                node_chain_len = node_fetcher.info['length']
                self.peer_nodes[host]['length'] = node_chain_len

                # Info
                printc(f"\tConnection to {host} succeeded! Chain of length {node_chain_len} found\n\n",GREEN)

                # Update global chain tracker
                if node_chain_len >= self.peer_nodes[self.top_peer]['length']:
                    self.top_peer = host

            except BlockChainRetrievalError as b:
                printc(f"\t{b}",TAN)
                printc(f"\tError in fetch blockchain on host {host}\n\n", RED)
                continue

        printc(f"longest chain is len: {self.peer_nodes[self.top_peer]['length']} on host {self.top_peer}",BLUE)

    def update_peer_node_iterative(self,host,full_blockchain,peer_head_hash):
        for (hash,block) in full_blockchain:
            post_data = {'block' : block_to_JSON(block)}

            if 


if __name__ == "__main__":
    n = Node()
