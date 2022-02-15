#########################################################################################
#######################################  IMPORTS  #######################################
#########################################################################################
from BlockchainErrors import *
from json import loads, dumps, JSONDecodeError
from requests import get, post,Timeout, RequestException
from os.path import isfile, isdir, join
from os import mkdir, listdir
import sys
# Package import to work on windows and linux
try:
    sys.path.append("C:\classes")
    sys.path.append("D:\classes")
    from Toolchain.terminal import *
except ModuleNotFoundError:
    sys.path.append("/home/m226252/classes")
    from Toolchain.terminal import *

#########################################################################################
############################ FUNCTIONS FOR PROCESSING BLOCKS ############################
#########################################################################################

# Make a request to where the head hash should be
def retrieve_head_hash(host="cat",port="5000",timeout=3):
    url = f"http://{host}:{port}/head"

    try:
        return get(url,timeout=timeout).content.decode()
        #print(f"recieved {}")
    except Timeout:
        raise ConnectionException(f"{Color.RED}Error: timeout requesting response from {url}")
    except RequestException:
        raise ConnectionException(f"{Color.RED}{Color.BOLD}Error: something went wrong connecting to {url}{Color.END}")
    except ConnectionError:
        raise ConnectionException(f"{Color.RED}Error: something went wrong connecting to {url}{Color.END}")


# Yields a block's 'prev_hash' field, given a block
def retrieve_prev_hash(block):
    # Check length requirements - can be 64 or 0 (for genesis block)
    try:
        if not len(block['prev_hash']) in [0,64]:
            raise HashRetrievalException(f"{Color.RED}Error: fetching of '{block['prev_hash'][:70]}'... not a valid hash'{Color.END}")
    except KeyError:
        raise HashRetrievalException(f"{Color.RED}Error: fetching of '{str(block)[:70]}...' missing 'prev_hash' key'{Color.END}")
    return block['prev_hash']


# Convert JSON representation of a block to python dictionary representation of a block
def JSON_to_block(JSON_text):
    try:
        return loads(JSON_text)
    except JSONDecodeError:
        raise DecodeException(f"{Color.RED}Error Decoding JSON: '{JSON_text[:50]}' as block{Color.END}")


# Convert python dictionary representation of a block to JSON representation of a block
def block_to_JSON(block):
    return dumps(block)


# Takes a hash and makes a request to the given URL to return the block with that hash
def retrieve_block(hash_decoded,host="cat",port="5000",timeout=3):
    url = f"http://{host}:{port}/fetch/{hash_decoded}"
    try:
        return get(url,timeout=timeout).content.decode()
    except Timeout:
        raise ConnectionException(f"{Color.RED}Error: timeout requesting response from {url}{Color.END}")
    except RequestException:
        raise ConnectionException(f"{Color.RED}Error: something went wrong connecting to {url}{Color.END}")
    except ConnectionError:
        raise ConnectionException(f"{Color.RED}Error: something went wrong connecting to {url}{Color.END}")


# Wrapper function for post
def http_post(host,port,payload,timeout=2):
    try:
        url = f"http://{host}:{port}/push"
        return post(url,data=payload,timeout=timeout)
    except Timeout:
        raise ConnectionException(f"{Color.RED}error: timeout requesting response from {url}")
    except RequestException:
        raise ConnectionException(f"{Color.RED}Error: something went wrong connecting to {url}{Color.END}")


# builds a block given the three fields and returns as JSON
def build_block(prev_hash,payload,ver):
    new_block = {   'prev_hash'     : prev_hash,
                    'payload'       : payload,
                    'version'       : ver}
    try:
        encoded_block = dumps(new_block)
        return encoded_block
    except JSONEncodeException as j:
        raise BlockCreationException(j)


# returns a list of all the allowed hashes
def grab_cached_hashes(cache_location='cache'):
    allowed_hashes = [(file.split('.')[0]).strip() for file in listdir(cache_location) if file.split('.')[-1] == 'json' and not file.split('.')[0] == 'current']
    return allowed_hashes


def iter_local_chain(hash):
    length = 0
    while not hash == '':
        length += 1
        try:
            file = f"cache/{hash}.json"
            hash = loads(open(file).read())['prev_hash']
        except FileNotFoundError:
            printc(f"\t\t{file} was not found in cache",RED)
            return length
    return length
#########################################################################################
########################## FUNCTIONS FOR PROCESSING BLOCKCHAIN ##########################
#########################################################################################


# given a processed block (python dictionary), check the block for keys, then check
# key values using the named parameters
def check_fields(block,allowed_versions=[0],allowed_hashes=[''],trust=False):
    if trust:
        return True
    # Ensure 'version' field checks out
    if (not 'version' in block) or\
       (not block['version'] in allowed_versions):
        print("bad version")
        return False


    # Ensure 'prev_hash' field checks out
    elif (not 'prev_hash' in block) or\
         (not block['prev_hash'] in allowed_hashes):
        print(block['prev_hash'] in allowed_hashes)
        print("bad hash")
        return False


    # Ensure the payload checks out
    elif (not 'payload' in block) or\
         (not isinstance(block['payload'],dict)) or\
         (('chat' in block['payload']) and (not isinstance(block['payload']['chat'],str))):

        print("bad payload")
        return False


    # Ensure block length req is met <= 1KB
    elif (len(block_to_JSON(block)) > 1024):
        print("bad len")
        return False

    return True


# Sends a block containing 'msg' to 'host' on 'port'
def send_chat(msg,host,port):
    #Specify all the URLs
    URL = { 'head' : f"http://{host}:{port}/head",
            'push' : f"http://{host}:{port}/push"}

    # Grab the current head hash
    head_hash = get(URL['head']).content.decode()
    print(f"received {head_hash}")
    # Create the block
    json_encoded_block = build_block(head_hash,{'chat' : msg},0)

    # Build format to send over HTTP
    push_data = {'block' : json_encoded_block}

    # Send it
    printc(f"\tSending block to {host}",TAN)
    try:
        post = http_post(host,5002,payload=push_data)
        if post.status_code == 200:
            printc(f"\tBlock sent successfully",GREEN)
        else:
            printc(f"\tCode recieved: {post} of type {type(post)}",TAN)
    except TypeError as t:
        printc(t,RED)
        printc(f"\tRecieved Null response...",TAN)
