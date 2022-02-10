from BlockTools import *
from BlockchainErrors import *
from json import dumps
from show_chat import ChatService
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


def send_chat(msg,host,port):
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
    data, post = http_post(URL['push'],push_data)
    if post == 200:
        printc(f"\tBlock sent successfully",GREEN)

def send_block(msg):
    hosts = {}
    chain   = {}
    longest_chain_len = 0
    head_hash = {}
    # Compile a list of all the head_hashes
    printc(f"Scanning hosts for chain lengths",BLUE)
    for host in open('hosts.txt').readlines():
        printc(f"\tTrying to connect to host: {host}", TAN)
        try:
            host = host.strip()
            head_hash[host] = get(f"http://{host}:5002/head", timeout=3).content.decode()
        except BlockChainVerifyError:
            printc(f"\tError in get request on host {host}",RED)
            continue
        except ConnectionError:
            printc(f"\tError in get request on host {host}",RED)
        except ConnectionRefusedError:
            printc(f"\tError in get request on host {host}",RED)


        try:
            chatter = ChatService(host=host,port=5002)
            chatter.fetch_blockchain()
            hosts[host] = chatter
            if chatter.info['length'] >= longest_chain_len:
                longest_chain_len = chatter.info['length']
        except BlockChainRetrievalError as b:
            printc(f"\t{b}",TAN)
            printc(f"\tError in fetch blockchain on host {host}", RED)

    printc(f"longest chain is len: {longest_chain_len}",BLUE)
    printc(f"Sending out blocks",BLUE)

    for host in hosts:
        if hosts[host].info['length'] >= longest_chain_len:
            printc(f"\tSending block to host {host}",TAN)
            send_chat(msg,host,5002)


if __name__ == "__main__":
    send_block(input("New message for block: "))
