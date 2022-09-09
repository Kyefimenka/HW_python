import time

def init_rand():
    global seed
    t = time.time()
    return int((t - int(t))*1000000)

def my_rand(N=0, M=1):
  global seed
  seed = (seed * 73129 + 95121) % 100000
  return int((float(seed)/100000)*(M-N)+N)

seed = init_rand()
print(my_rand(1, 10))