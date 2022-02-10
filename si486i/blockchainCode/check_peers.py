from BlockchainUtilities import *
from BlockchainErrors import *

# Package import to work on windows and linux
try:
    sys.path.append("C:\classes")
    sys.path.append("D:\classes")
    from Toolchain.terminal import *
except ModuleNotFoundError:
    sys.path.append("/home/m226252/classes")
    from Toolchain.terminal import *


hosts = [line.strip() for line in open('hosts.txt').readlines()]
ports = ["5000","5001","5002"]

for host in hosts:
    printc(f"attempting conneciton to {host} on port {port}",BLUE)
    for port in ports:
        try:
            blockchain_download = get_blockchain(host,port)
            size = len(blockchain_download)
            print(f"{Color.GREEN}blockchain verified!\n{size} blocks in chain{Color.END}\n")


        except BlockChainVerifyError as b:
            print(b)

            print(f"Error Verifying Blockchain\n\n")

        except BlockChainError as b:
            print(f"Error Downloading Blockchain: Terminated\n\n")
            continue
