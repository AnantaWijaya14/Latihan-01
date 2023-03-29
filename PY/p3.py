#membuat class untuk node
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data 
        self.next_node = next_node

    #Mengmabil data dari node
    def get_data(self):
        return self.data

    #Mengambil node berikutnya
    def get_next(self):
        return self.next_node

    #Menentukan node berikutnya
    def set_next(self,new_next):
        self.next_node = new_next
#Membuat class untuk linked list
class LinkedList(object):
    def __init__(self, head =None):
        self.head = head

    #Menambah node baru
    def insert(self,data):
        #Insisialisasi node baru
        new_node = Node(data)
        #Menunjuk node berikutnya dari node baru ke node uang ditunjuk oleh HEAD
        new_node.set_next(self.head)
        #HEAD menunjuk ke node baru
        self.head = new_node

    #Menghitung panjang list
    def size(self):
        #Membuat pointer baru menunjuk kenode yang ditunjuk oleh HEAD
        current = self.head
        count = 0
        # Perulangan untuk menghitung node
        while current:
            count += 1
            current = current.get_next()
            return count

        #Mencari sebuah daya [ada list
        def search(self,data):
            #Membuat pointer baru menunjuk ke node yang di tunjuk oleh HEAD
            current = self.head
            found = False
            # Perulangan mencari node yang dicari
            while current and found is False:
                if current.get_data() == data:
                    found = True
                else:
                    current = current.get_next()

            return found

            # Menghapus node
            def delete(self,data):
                current = self.head
                previous = None
                found = False
                while current and found is False:
                    if current and found is False:
                        found = True
                    else:
                        previous = current
                        current = current.get_next()
                if current is None:
                    raise ValueEror("Data not in list")
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())

                



        