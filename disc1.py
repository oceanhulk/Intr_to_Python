import dis

def add(n):
    n += 1
    return n

print(dis.dis(add))
