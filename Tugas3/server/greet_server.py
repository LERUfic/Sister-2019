# from greet import  *
from greet_centralhb import  *
import Pyro4
import os

def start_with_ns():
    #name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777
    #gunakan URI untuk referensi name server yang akan digunakan
    #untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n localhost -p 7777 list
    daemon = Pyro4.Daemon(host="localhost")
    ns = Pyro4.locateNS("localhost",7777)
    x_GreetServer = Pyro4.expose(GreetServer)
    uri_greetserver = daemon.register(x_GreetServer)
    print("URI greet server : ", uri_greetserver)
    ns.register("greetserver", uri_greetserver)
    daemon.requestLoop()


if __name__ == '__main__':
    if os.path.isfile("session.db"):
        os.remove("session.db")
        open('session.db','a').close()
    else:
        open('session.db','a').close()
    start_with_ns()
