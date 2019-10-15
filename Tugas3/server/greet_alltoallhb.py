import random
import subprocess
import shlex
import serpent
import Pyro4
import pickle
import os

class GreetServer(object):
    def __init__(self):
        if (os.stat("session.db").st_size == 0):
            self.all_clients = {}
        else:
            with open('session.db','rb') as f:
                self.all_clients = pickle.load(f)

    def get_ls(self):
        return subprocess.check_output(["ls","-a","-l"])

    def delete_rm(self,file_name):
        return subprocess.check_output(["rm", file_name])

    def read_cat(self,file_name):
        return subprocess.check_output(["cat", file_name])
    
    def touch_mytralala(self,file_name):
        return subprocess.check_output(["touch", file_name])

    def write_update(self,file_name,option,text):
        if option == "append":
            with open(file_name, "a") as myfile:
                myfile.write(text+'\n')
        return subprocess.check_output(["cat", file_name])

    def seq_check(self,sequence):
        # xclient_ip = Pyro4.current_context.client.sock.getpeername()[0]
        xclient_ip = Pyro4.current_context.client_sock_addr
        # print(xclient_ip)
        client_ip = xclient_ip[0]+str(xclient_ip[1])
        if client_ip in self.all_clients:
            if (int(self.all_clients[client_ip])+1 == int(sequence)):
                self.all_clients[client_ip] = str(sequence)
            else:
                return "Failed"
        else:
            self.all_clients[client_ip] = str(0)
            
        with open('session.db','wb') as f:
            pickle.dump(self.all_clients,f, pickle.HIGHEST_PROTOCOL)
        with open('session.db', "rb") as f:
            byte = f.read(5120)
            ser = serpent.dumps(byte, indent=True)
            ser.decode("UTF-8")
            return ser
        # return "Success"

    def routing(self,command):
        _gs = GreetServer()
        if "GET" in command:
            return _gs.get_ls()
        elif "DEL" in command:
            s_command = shlex.split(command)
            return _gs.delete_rm(s_command[1])
        elif "Touch" in command:
            s_command = shlex.split(command)
            return _gs.touch_mytralala(s_command[1])
        elif "READ" in command:
            s_command = shlex.split(command)
            return _gs.read_cat(s_command[1])
        elif "WRITE" in command:
            # WRITE haha.txt append "text"
            s_command = shlex.split(command)
            return _gs.write_update(s_command[1], s_command[2], s_command[3])
        elif "SEQ" in command:
            s_command = shlex.split(command)
            return _gs.seq_check(s_command[1])
        else:
            return "{}: command not found!".format(command)

    def construct_file(self,file_name,data):
        data = str(data)
        f = open(file_name+'lerufic','ab')
        if data == "FileSent//LERUfic":
            f.close()
            return subprocess.check_output(["mv", file_name+'lerufic',file_name])
        else:
            f = open(file_name+'lerufic','ab')
            ser = serpent.loads(data)
            f.write(ser.encode('utf-8'))
            f.close()
            return


if __name__ == '__main__':
    k = GreetServer()
