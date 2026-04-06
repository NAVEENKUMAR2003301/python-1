import threading
import time



def update_db():
    time.sleep(5)
    print("update....")



def update1(num):
    for i in range(1,num+1):
        print(i)


a = threading.Thread(target=update_db)
a.start()
update1(10)

print(threading.active_count())
print(threading.enumerate())


