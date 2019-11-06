# Tugas 5

## Permasalahan
Membuat sebuah data-centric agar ketika client ingin mengakses data dari salah satu tiga fileserver, bisa mengakses file yang benar.

## Desain Infrastruktur
![infra](images/infra.png)

## Penyelesaian
Solusi yang saya tawarkan adalah dengan menggunakan sistem replikasi. Jadi semisal client1 mengirim data dan diterima oleh server1. Maka server1 akan bertugas sebagai Replication Manager untuk mereplikasi file ke server lainnya.

Berikut potongan code untuk replikasi pada server
```python
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
```
## Hasil Percobaan
Berikut adalah kondisi awal pada masing-masing server.
![awal](images/before.png)

Dan berikut adalah kondisi akhir pada masing-masing server setelah client1 menjalankan perintah
![akhir](images/after.png)

Berikut adalah kondisi terminal dan cara menjalankan program pythonnya.
![terminal](images/terminal.png)