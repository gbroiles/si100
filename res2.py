import resource
import base64
import hashlib
import gzip
import bz2
import lzma

out = base64.standard_b64decode(resource.pdf)
resource = str.encode(resource.pdf)
print("uncompressed length = {:,}".format(len(out)))
print("encoded length = {:,}".format(len(resource)))
print("md5 = {}".format(hashlib.md5(out).hexdigest()))

gzip_string = gzip.compress(resource)
bzip_string = bz2.compress(resource)
lzma_string = lzma.compress(resource)

print("gzip = {:,}  bzip = {:,}  lzma = {:,}".format(len(gzip_string), len(bzip_string), len(lzma_string)))
