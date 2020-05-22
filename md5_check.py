# Exports md5 checksum for the downloaded file

import hashlib
import sys
file_name = sys.argv[1]
print 'md5 check for ' + sys.argv[1]
md5_hash = hashlib.md5()

a_file = open(file_name, "rb")
content = a_file.read()
md5_hash.update(content)

digest = md5_hash.hexdigest() # Returns the md5 checksum in hexadecimal value
print(digest)

with open('md5_from_destination.txt', 'w') as file:
   file.write(digest)
