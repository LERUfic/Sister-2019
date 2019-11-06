import os
import base64
import Pyro4

class FileServer(object):
    def __init__(self):
        self.all_nameserver = ['fileserver1','fileserver2','fileserver3']

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def list(self):
        print("list ops")
        try:
            daftarfile = []
            for x in os.listdir():
                if x[0:4]=='FFF-':
                    daftarfile.append(x[4:])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self,namainstance, name='filename000'):
        nama='FFF-{}' . format(name)
        print("create ops {}" . format(nama))
        try:
            if os.path.exists(name):
                return self.create_return_message('102', 'OK','File Exists')
            f = open(nama,'wb',buffering=0)
            f.close()
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    def read(self,namainstance,name='filename000'):
        nama='FFF-{}' . format(name)
        print("read ops {}" . format(nama))
        try:
            f = open(nama,'r+b')
            contents = f.read().decode()
            f.close()
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')
    def update(self,namainstance,name='filename000',content=''):
        nama='FFF-{}' . format(name)
        print("update ops {}" . format(nama))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open(nama,'w+b')
            f.write(content.encode())
            f.close()
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,namainstance,name='filename000'):
        nama='FFF-{}' . format(name)
        print("delete ops {}" . format(nama))

        try:
            os.remove(nama)
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')

    def replicateCreate(self,namainstance,name='filename000'):
        nama='FFF-{}' . format(name)
        for i in self.all_nameserver:
            if namainstance == i:
                self.create(i,name)
            else:
                uri = "PYRONAME:{}@localhost:7777" . format(i)
                with Pyro4.Proxy(uri) as p:
                    try:
                        p._pyroBind()
                        p.create(i,nama)
                    except Pyro4.errors.CommunicationError:
                        print("Server is not Reachable. Try Again Later!")
            
    def replicateUpdate(self,namainstance,name='filename000',content=''):
        nama='FFF-{}' . format(name)
        for i in self.all_nameserver:
            if namainstance == i:
                self.update(i,name,content)
            else:
                uri = "PYRONAME:{}@localhost:7777" . format(i)
                with Pyro4.Proxy(uri) as p:
                    try:
                        p._pyroBind()
                        p.update(i,nama,content = open(nama,'rb+').read())
                    except Pyro4.errors.CommunicationError:
                        print("Server is not Reachable. Try Again Later!")




if __name__ == '__main__':
    k = FileServer()
    print(k.create('f1'))
    print(k.update('f1',content='wedusku'))
    print(k.read('f1'))
#    print(k.create('f2'))
#    print(k.update('f2',content='wedusmu'))
#    print(k.read('f2'))
    print(k.list())
    #print(k.delete('f1'))

