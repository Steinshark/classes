from BlockTools import http_post, build_block
from json import dumps
from show_chat import ChatService
from requests import get


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
    post = http_post(URL['push'],push_data)

def scan_chains():
    head_hashes = {}
    chain_len   = {}
    # Compile a list of all the head_hashes
    for host in open('hosts.txt').readlines():
        try:
            host = host.strip()
            head_hashes[host] = get(f"http://{host}:5002/head", timeout=3).content.decode()
            chatter = ChatService(host=host,port=5002)
            chatter.fetch_blockchain()
            chain_len[host] = chatter.info['length']
            print(f"host: {host} has longest chain of {chain_len[host]}")
        except:
            print(f"Error connecting to host: {host} on port 5002")


if __name__ == "__main__":
    scan_chains()

    send_chat("hello world!",'lion',5002)
