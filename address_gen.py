
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:17313"%("username", "password"))
#username and password must be same with the username and password entered in flo.conf file

address = rpc_connection.getnewaddress()

print(address)
