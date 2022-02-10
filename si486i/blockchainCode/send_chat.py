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
        self.peer_nodes = {host : {'length' : 0, 'host' : None, 'fetcher' : None, 'head' : None} for host in self.hosts}

        self.top_peer = self.peers[0]
        self.check_peer_servers()

    def send_chat(self,msg,host,port):
        #Specify all the URLs
        URL = { 'head' : f"http://{host}:{port}/head",
                'push' : f"http://{host}:{port}/push"}

        # Grab the current head hash
        head_hash = get(URL['head']).content.decode()

        # Create the block
        json_encoded_block = build_block(head_hash,{'chat' : msg},0)

        # Build format to send over HTTP
        push_data = {'block' : json_encoded_block}

        # Send it
        printc(f"\tSending block to {host}",TAN)
        try:
            data, post = http_post(URL['push'],push_data)
            if post == 200:
                printc(f"\tBlock sent successfully",GREEN)
            else:
                printc(f"\tCode recieved: {post}, data recieved: {data}",TAN)
        except TypeError:
            printc(f"\tRecieved Null response...",TAN)

    def check_peer_servers(self,msg):

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
                printc(f"\tError in get request on host {host} - unknown reason",RED)
                continue

            except ConnectionRefusedError:
                printc(f"\tError in get request on host {host} - refused",RED)
                continue

            # Attempt to fetch the blockchain of that node
            try:
                # Grab the blockchain
                node_fetcher = FetchService(host=host,port=5002)
                node_fetcher.fetch_blockchain()

                # Assign the fetcher to the node
                self.peer_nodes[host]['fetcher'] = node_fetcher

                # Get info on the chain
                self.peer_nodes[host]['length'] = node_fetcher.info['length']

                # Info
                printc(f"\tConnection to {host} succeeded! Chain of length {blockchain_len} found\n\n",GREEN)

                # Update global chain tracker
                if self.peer_nodes[host]['length'] >= self.peer_nodes[self.top_peer]['length']:
                    self.top_peer = self.peer_nodes[host]['length']

            except BlockChainRetrievalError as b:
                printc(f"\t{b}",TAN)
                printc(f"\tError in fetch blockchain on host {host}", RED)
                continue

        printc(f"longest chain is len: {self.peer_nodes[self.top_peer]['length']} on host {self.top_peer}",BLUE)



if __name__ == "__main__":
    n = Node()
