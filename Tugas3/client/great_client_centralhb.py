import Pyro4
import shlex
import serpent
import threading
import sys
import time

def send_with_ns(file_name):
    # uri = "PYRONAME:greetserver@159.65.129.224:7777"
    uri = "PYRONAME:greetserver@localhost:7777"
    with Pyro4.Proxy(uri) as gserver:
        with open(file_name, "rb") as f:
            byte = f.read(2048)
            while byte != "":
                ser = serpent.dumps(byte, indent=True)
                ser.decode("UTF-8")
                gserver.construct_file(file_name,ser)
                byte = f.read(2048)
            gserver.construct_file(file_name,"FileSent//LERUfic")

def test_with_ns(command):
    # uri = "PYRONAME:greetserver@159.65.129.224:7777"
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.routing(command))

def server_pinger():
    # uri = "PYRONAME:greetserver@159.65.129.224:7777"
    uri = "PYRONAME:greetserver@localhost:7777"
    sequence = 0
    while True:
        time.sleep(1)
        with Pyro4.Proxy(uri) as p:
            try:
                res = p.routing("SEQ " +str(sequence))
                if(res == "Success"):
                    print(sequence)
                    sequence = sequence + 1
                else:
                    print("Server Error!. Try Again Later!")
                    sys.exit()
            except Pyro4.errors.CommunicationError:
                print("Server is not Reachable. Try Again Later!")
                sys.exit()

if __name__=='__main__':
    try:
        t1 = threading.Thread(target=server_pinger, name='server_pinger')
        t1.daemon = True
        t1.start()
        runner_flag = True
        while runner_flag:
            command = raw_input("root@server:~$ ")
            if command == "exit":
                print "Bye"
                sys.exit()
            elif "SEND" in command:
                s_command = shlex.split(command)
                send_with_ns(s_command[1])
            else:
                test_with_ns(command)
    except(KeyboardInterrupt, SystemExit):
        print "Bye"
        sys.exit()