import ipfshttpclient

def add(file):
    #Upload dos dados médicos pro IPFS
    ipfs=ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    res=ipfs.add(file)
    #print('Hash Ipfs -- ',res['Hash'])
    return res['Hash']

def cat(cid):
    #Upload dos dados médicos pro IPFS
    ipfs=ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    print(cid)
    return ipfs.cat(cid)
    