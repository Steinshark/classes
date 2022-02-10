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
    data, post = http_post(URL['push'],push_data)
    if post == 200:
        printc(f"\tBlock sent successfully",GREEN)

def send_block(msg):
    hosts = {}
    chain   = {}
    longest_chain_len = 0
    # Compile a list of all the head_hashes
    printc(f"Scanning hosts for chain lengths",BLUE)
    for host in open('hosts.txt').readlines():
        try:
            host = host.strip()
            head_hashes[host] = get(f"http://{host}:5002/head", timeout=3).content.decode()
            chatter = ChatService(host=host,port=5002)
            chatter.fetch_blockchain()
            hosts[host] = chatter
            if chatter.info['length'] >= longest_chain_len:
                longest_chain_len = chatter.info['length']
        except:
            print(f"Error connecting to host: {host} on port 5002")

    printc(f"longest chain is len: {longest_chain_len}",BLUE)
    printc(f"Sending out blocks",BLUE)

    for host in hosts:
        if hosts[host].info['length'] >= longest_chain_len:
            printc(f"\tSending block to host {host}",TAN)
            send_chat(msg,host,5002)


if __name__ == "__main__":
    send_block("hi everyone!")
