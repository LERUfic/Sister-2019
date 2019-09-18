# Sister-2019
## Tugas 1
Membuat service penyimpanan file yang memiliki list fitur sebagai berikut:
* Meletakan File (Create)
* Menghapus File (Delete)
* Membaca File (Read)
* Merubah Isi File (Update)
* Melihat daftar file yang ada (List)

### Meletakan File (Create)
> **SEND filename**

    Contoh:  
    SEND aguelsatria.txt
### Menghapus File (Delete)
> **DEL filename**

    Contoh:  
    DEL aguelsatria.txt
### Membaca File (Read)
> **READ filename**

    Contoh:  
    READ aguelsatria.txt
### Merubah Isi File File (Update)
> **WRITE filename [option] "text"**  

    List Option:
    - append    Menambahkan text ke dalam file
    
    Contoh:  
    WRITE aguelsatria.txt append "Ini text yang diinputkan"
### Melihat daftar file yang ada (List)
> **GET**   

    Contoh:  
    GET