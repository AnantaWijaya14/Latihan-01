class Stack:
    def __init__(self):
        self.items = []

    # Memeriksa apakah stack kosong
    def isEmpty(self):
        return self.items == []
    # Menambah objek/data ke dalam stack
    def push(self, item):
        self.items.append(item)
    # Mengeluarkan data dari stack
    def pop(self):
        return self.items.pop()
    # Menampilkan objek terakhir dari stack
    def peek(self):
        return self.items[len(self.items)-1]
    # Mehitung panjang stack
    def size(self):
        return len(self.items)
    # Mehitung Nilai terbesar dari stack
    def size(self):
        return max(self.items)
    # Mehitung nilai terkecil dari stack
    def size(self):
        return min(self.items)
    def show_all(self):
        if self.isEmpty():
            print("satck kosong")           
        else:
            print("data pada stack : ")
            for item in reversed(self.items):
                print(item)

    # Menu dari aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("=========================")
            print("| Menu aplikasi stack |")
            print("=========================")
            print("1. Push objek")
            print("2. Pop objek")
            print("3. Cek Empty")
            print("4. Tampil objek terakhir")
            print("5. Panjang dari stack")
            print("6. Nilai terbesar dari stack")
            print("7. Nilai terkecil dari stack")
            print("8. Jumlah seluruh nilai dari stack")
            print("=========================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                obj = str(input("Masukan objek yang ingin anda tambahkan: "))
                self.push(obj)
                print("Object "+obj+" telah ditambahkan")
                x = input("")
            elif(pilihan=="2"):
                print("Objek "+self.pop()+" dihapus")
                x = input("")
            elif(pilihan=="3"):
                print(self.isEmpty())
                x = input("")
            elif(pilihan=="4"):
                print("Objek terakhir: "+self.peek())
                x = input("")
            elif(pilihan=="5"):
                print("Panjang dari stack adalah:"+str(self.size()))
                x = input("")
            elif(pilihan=="6"):
                print("Nilai terbesar dari stack adalah:"+str(self.size()))
                x = input("")
            elif(pilihan=="7"):
                print("Nilai terkecil dari stack adalah:"+str(self.size()))
                x = input("")
            elif(pilihan=="8"):
                s.show_all()
                x = input("")
            else:
                pilih="n"
if __name__ == "__main__":
    s=Stack()
    s.mainmenu()
