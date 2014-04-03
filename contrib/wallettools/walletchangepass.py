from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:9332")
pwd = raw_input("Enter old wallet password: ")
pwd2 = raw_input("Enter new wallet password: ")
access.walletpassphrasechange(pwd, pwd2)
