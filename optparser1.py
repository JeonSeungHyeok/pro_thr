import optparse

parser = optparse.OptionParser('<usage> Port Scan -H <Host> -P <Port>')
parser.add_option('-H', dest='host', type='string', help='specify host')
parser.add_option('-P', dest='port', type='string', help='specify port')

(options, args) = parser.parse_args()

host = options.host
port = options.port

if host == None or port == None:
    print(parser.usage)
else:
    print(host)
    print(port)