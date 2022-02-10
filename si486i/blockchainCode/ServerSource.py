import flask
from BlockTools import *
from BlockchainUtilities import *
from os.path import isfile, isdir
from fcntl import flock, LOCK_SH,LOCK_EX, LOCK_UN
from json import dumps, loads
from os import listdir, mkdir
import argparse
import sys

# Package import to work on windows and linux
try:
    sys.path.append("C:\classes")
    sys.path.append("D:\classes")
    from Toolchain.terminal import *
except ModuleNotFoundError:
    sys.path.append("/home/m226252/classes")
    from Toolchain.terminal import *



class StaticServer:
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.blocks = OrderedDict()


    # Maps a block hash to the block itself

        @self.app.route('/head')
        def head():
            return list(self.blocks.keys())[-1]

        @self.app.route('/fetch/<digest>')
        def fetch(digest):
            try:
                return self.blocks[digest]

            except KeyError:
                # HTTP code 400 indicates a bad request error
                return 'hash digest not found', 400

        @self.app.route('/<command>')
        def maintain(command):
            # Grab the commands
            arguments = [c.strip() for c in command.split(" ")]

            # Allow for block addition
            if arguments[0] == "add":
                if arguments[1] == "block":
                    block = arguments[2]
                    block_hash = hash('hex',block.encode()).hexdigest()
                    self.blocks[block_hash] = block

            # Allow for block removal
            elif arguments[0] == "remove":
                if arguments[1] == "head":
                    self.blocks.popitem()

            # Error case
            else:
                return f'command {command} not understood by server', 269

    def run(self,host='lion',port=5000,gen_block=None,override=True):
        if override:
            pass
        elif not self.blocks and gen_block is None:
            block = build_block('',{'chat' : 'my very own blockchain!'},0)
            block_hash = hash('hex',block.encode())
            self.blocks[block_hash] = block
            print(f"head is now {list(self.blocks.keys())[-1]}")
        else:
            block_hash = hash('hex',gen_block.encode())
            self.blocks[block_hash] = gen_block
            print(f"head is now {list(self.blocks.keys())[-1]}")



        self.app.run(host=host,port=port)

class DynamicServer:


################################################################################
################################################################################
#                               CREATE INSTANCE
################################################################################
################################################################################

    def __init__(self):
        printc(f"\t\t\tSTARTING SERVER INIT",BLUE)
        printc(f"\tInit vars",TAN)
        self.app = flask.Flask(__name__)
        self.empty = True
        self.head_hash = None                   # Keep track of whats in current
        self.longest_chain = 0                  # This will be used as a dynamic
                                                #                 'current.json'
        self.scan_chains()                      # Builds the initial chains list
        printc(f"INIT DONE - STARTING\n\n\n",GREEN)



################################################################################
################################################################################
#                    HANDLE HEAD REQUESTS
################################################################################
################################################################################

        @self.app.route('/head')
        def head():

            # Some simple debug code
            print(f"{TAN}\thead request recieved\n\n\n{END}")

            # Check that we have a chain
            if self.empty:
                with open('cache/current.json','w') as file:
                    flock(file,LOCK_SH)
                    info = {'length' = 0, 'head' = ''}
                    file.write(dumps(info))
                    flock(file,LOCK_UN)
                return "", 200
            # Open, lock, read the head file, and send the info back
            with open('cache/current.json') as file :
                flock(file,LOCK_SH)
                info = loads(file.read())
                self.blockchain_len = info['length']
                self.head_hash = info['head']
                flock(file,LOCK_UN)

            # Can't imagine how this would not return 200
            return self.head_hash, 200



################################################################################
################################################################################
#                    HANDLE HASH-FETCH REQUESTS
################################################################################
################################################################################

        @self.app.route('/fetch/<digest>')
        def fetch(digest):

            # Some simple debug code
            print(f"request made: {digest}")

            # Make the (hopefully existing) filename
            filename = f'cache/{digest}.json'

            # Handle an error - 404 == not found here
            if not isfile(filename):
                return f'{RED}{filename} not found in cache{RED}', 404

            # Open up that file up (with locks!) and shoot it back to them
            else:
                with open(filename) as file:
                    flock(file,LOCK_SH)
                    block = file.read()
                    flock(file,LOCK_UN)
                    return block, 200



################################################################################
################################################################################
#                    HANDLE PUSH REQUESTS TO THE SERVER
################################################################################
################################################################################

        @self.app.route('/push', methods=['POST'])
        def push_block():
            received_data = flask.request.form
            printc(f"\trecieved '{str(received_data)[:35]} ... {str(received_data)[-20:]}'",TAN)

################################################################################
#                    Check if the message is decodable at all

            try:
                block = JSON_to_block(received_data['block'])
                printc(f"\tdecoded to '{str(block)[:35]} ... {str(block)[-20:]}'",TAN)

            except JSONDecodeError as j:
                printc(f"\terror decoding sent block",RED)
                return f"{Color.RED}\tblock rejected - check your block encoding!{Color.END}", 400

################################################################################
#                    Check if the block fields are OK

            if not check_fields(block,allowed_versions = [0],allowed_hashes=['']+grab_cached_hashes(cache_location='cache')):
                printc(f"\trejected block",RED)
                printc('\n\n\n',TAN)
                return f"{Color.RED}\tblock rejected!{Color.END}", 400

            else:
                update_chains(block)
                open(f'{hash(block.encode())}')
                printc(f"\taccepted block",GREEN)
                print('\n\n\n')
                return f"{Color.GREEN}\tblock accepted!{Color.END}", 200



################################################################################
################################################################################
#                    EXECUTE AN INSTANCE OF THE SERVER
################################################################################
################################################################################
    def run(self,host='lion',port=5002):
#        print(f{Color.GREEN}SERVER STARTED{Color.END}')
        self.app.run(host=host,port=port)



################################################################################
################################################################################
#                    EXECUTE AN INSTANCE OF THE SERVER
################################################################################
################################################################################
    def scan_chains(self):
        printc(f"\tScanning for local chains",BLUE)
        possible_hashes = []
        hashes_to_prev_hash = {}

        hash_to_info = {}
        if not isdir('cache'):
            mkdir("cache")
            printc(f"\t\tNo blocks found",RED)
            self.all_chains = {}
            return
        for file in listdir('cache/'):
            if file[-5:] == '.json' and not file == 'current.json':
                hash = file[:-5].strip()
                possible_hashes.append(hash)
                with open(f"cache/{file}",'r') as f:
                    prev_hash = loads(f.read().strip())['prev_hash']
                    printc(f"\t\thash {hash} maps to {prev_hash}",TAN)


        for not_possible_end_hash in hashes_to_prev_hash.values():
            possible_hashes.pop(not_possible_end_hash)
        longest = 0
        l_hash = None
        for hash in possible_hashes:
            bl = len(get_blockchain_from_hash(hash,False))
            hash_to_info[hash] = bl
            if bl > longest:
                longest = bl
                l_hash = hash
        printc(f"\t\tFound {len(possible_hashes)} chains",TAN)
        printc(f"\t\tLongest chain: {longest} block",TAN)

        self.empty = not possible_hashes
        self.longest_chain = longest
        self.longest_hash = l_hash
        self.all_chains = hash_to_info

    def update_chains(block):
        pass

if __name__ == '__main__':
    host = input('run on host: ').strip()
    port = input('run on port: ')
    s = DynamicServer()
    if not host and not port:
        s.run()
    else:
        s.run(host=host,port=int(port))
