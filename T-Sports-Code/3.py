import sys


data = sys.stdin.read().split()

if data:
    n = int(data[0])
    m = int(data[1])
    
  
    idx = 2

    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        
        if u < v:
            print(f"{u} {v}")
        else:
            print(f"{v} {u}")