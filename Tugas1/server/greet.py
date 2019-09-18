import random
import subprocess
import shlex
import serpent

class GreetServer(object):
    def __init__(self):
        pass

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
