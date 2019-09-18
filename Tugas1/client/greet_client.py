import Pyro4
import shlex
import serpent

def send_with_ns(file_name):
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
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.routing(command))

if __name__=='__main__':
    runner_flag = True
    while runner_flag:
        command = raw_input("root@server:~$ ")
        if command == "exit":
            print "Bye"
            break
        elif "SEND" in command:
            s_command = shlex.split(command)
            send_with_ns(s_command[1])
        else:
            test_with_ns(command)