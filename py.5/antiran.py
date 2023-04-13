import queue
antrian = queue.Queue()
print(antrian.empty()) #true
antrian.put(1)
antrian.put(2)
antrian.put(3)
antrian.put(4)
print(antrian.get([1])) #1
print(antrian.get([2])) #2
print(antrian.empty()) # False
print(antrian.queue)