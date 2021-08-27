import nmap
target = input("enter target ip : ")
scanner = nmap.PortScanner()
begin = input("enter the port to begin : ")
end = input("enter the port to end : ")
for i in range(begin,end+1):

	res = scanner.scan(target,str(i))
	res = res['scan'][target]['tcp'][i]['state']

	print(f'port {i} is {res}.')
