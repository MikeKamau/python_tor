import socks
import socket
import urllib

#The following two lines connect to the local SOCKS5 proxy that's started on port 9050 when tor
#starts up.
socks.set_default_proxy(socks.SOCKS5,"127.0.0.1", 9050)
socket.socket = socks.socksocket

#The following line is to connect to http://icanhazip.com, which displays the ip address of the client connecting to it.
#This line is to ensure that our code is working as expected and we are not revealing our real ip adress.
print(urllib2.urlopen('http://icanhazip.com').read())

#After verifying that your real ip is not being broadcast, you can add any other code from here on out and be assured that it's been tunneled
#through tor.