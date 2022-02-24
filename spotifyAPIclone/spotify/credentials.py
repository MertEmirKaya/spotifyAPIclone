import base64


client_id='8bc58799baca4678b71bca24c14844dc'
client_secret='86a5ab2774a642578cc9abaf3c5896c1'
redirect_uri='http://127.0.0.1:8000/'

message = f"{client_id}:{client_secret}"

messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)

base64Message = base64Bytes.decode('ascii')