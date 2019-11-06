import Pyro4
import base64
import json
import sys

default_namainstance = sys.argv[1] or "fileserver"

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(default_namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    f.replicateCreate(default_namainstance,'slide1.pdf')
    f.replicateUpdate(default_namainstance,'slide1.pdf', content = open('slide1.pdf','rb+').read())

    f.replicateCreate(default_namainstance,'slide2.pptx')
    f.replicateUpdate(default_namainstance,'slide2.pptx', content = open('slide2.pptx','rb+').read())

    print(f.list())
    d = f.read(default_namainstance,'slide1.pdf')
    #kembalikan ke bentuk semula ke dalam file name slide1-kembali.pdf
    open('slide1-kembali.pdf','w+b').write(base64.b64decode(d['data']))

    k = f.read(default_namainstance,'slide2.pptx')
    #kembalikan ke bentuk semula ke dalam file name slide2-kembali.pptx
    open('slide2-kembali.pptx','w+b').write(base64.b64decode(k['data']))


