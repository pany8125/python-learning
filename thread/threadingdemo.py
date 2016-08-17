import threading

class BuckyMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = BuckyMessenger(name='Sending messages')
y = BuckyMessenger(name='Receiving messages')
x.start()
y.start()
