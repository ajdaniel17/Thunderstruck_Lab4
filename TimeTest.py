import time

Duration = 1.0
print(Duration)
Start = time.time()
print(Start)
while((time.time() - Start) < Duration):
    print("Not Time yet")
print(time.time()-Start)
    