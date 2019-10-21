import nmap
n = 1
nmScan = nmap.PortScanner()
nmScan.scan('RHOST', '1-1024')

for host in nmScan.all_hosts():
    print('Host : %s (%s)' % (host, nmScan[host].hostname()))
    print('State : %s' % nmScan[host].state())
    for proto in nmScan[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nmScan[host][proto].keys()
        for port in lport:
            print ('port : %s(Word%s)\tstate : %s' % (port,n,nmScan[host][proto][port]['state']))
            n += 1