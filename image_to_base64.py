import base64
import sys
import json

# example
# /home/apiweb3c/test/kayu_manis.jpg
path = sys.argv[1]

with open(path, "rb") as image_file:
	encoded_string = base64.b64encode(image_file.read())

print(encoded_string.decode('utf-8'))
