from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name, l):
    info('function f')
    print('hello', name)
    print(l)
    l[1]=4
    print(l)

if __name__ == '__main__':
    info('main line')
    l = [1,2,3]
    p = Process(target=f, args=('bob', l))
    p.start()
    p.join()
    print(l)