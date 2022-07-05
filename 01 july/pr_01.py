import time
print("Hello World!")

with open("timeshow.txt") as f:
    print(f"This file was run last time is: {f.read()}")

with open("timeshow.txt", 'w') as f:
    f.write(time.asctime())

