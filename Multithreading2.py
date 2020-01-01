import time
import threading

start=time.perf_counter()

def do_something(seconds):                                     #The main function that works in the code
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    print('Done Sleeping')

threads=[]

for _ in range(10):
    t=threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish=time.perf_counter()

print(f'Finished in {round(finish-start)} second(s)')

#Output:

# Sleeping 1.5 second
# Sleeping 1.5 second
# Sleeping 1.5 second
# Sleeping 1.5 second
# Sleeping 1.5 second
# Sleeping 1.5 second
# Sleeping 1.5 second
# Sleeping 1.5 second
# Sleeping 1.5 second
# Sleeping 1.5 second
# Done Sleeping
# Done Sleeping
# Done Sleeping
# Done Sleeping
# Done Sleeping
# Done Sleeping
# Done Sleeping
# Done Sleeping
# Done Sleeping
# Done Sleeping
# Finished in 2 second(s)

#In the above code, when we create the variable 't' and implement threading.Thread to function do_something, it creates simultaneious 10 threads
#Then, with the start() function, the threads begin and then they get appended and then get printed
#However, since we have 10 simultanious threads, the initial function within do_something fucntion gets executed 10 times within 1 second and then
#the all the threads sleep simultaneously for 10 seconds and then next function gets executed 10 times simultaneously.
#This happens due to multithreading