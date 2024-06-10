import argparse
import cmd
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return 
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)
    return output.decode()

#Mainblock
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
            netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 # connect to server
        '''))
    parser.add_argument('c','--command',action='store_true',help='command shell')
    parser.add_argument('-e','--execute',help='execute specified command')
    parser.add_argument('-l','--listen',action='store_true',help='listen')
    parser.add_argument('-p','--port',type=int,default=5555,help='specified port')
    parser.add_argument('-t','--target',default='192.168.1.203',help='target ip')
    parser.add_argument('-u','--upload',help='upload file')
    args = parser.pars_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args,buffer.encode)

    class NetCat:
        def __init__(self,args,buffer=None):
            self.args = args
            self.buffer = buffer
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

            def run(self):
                if self.args.listen:
                    self.listen()
                else:
                    self.send()

#SendMethod
def send(self):
    self.socket.connect((self.args.target,self.args.port))
    if self.buffer:
        self.socket.send(self.buffer)
    
    try:
        while True:
            recv_len = 1
            response = ''
            while recv_len:
                data = self.socket.recv(4096)
                recv_len = len(data)
                response += data.decode()
                if recv_len < 4096:
                    break
