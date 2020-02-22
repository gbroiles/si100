import resource
import base64
import hashlib

out = base64.standard_b64decode(resource.pdf)
print(len(out))
print(hashlib.md5(out).hexdigest())
