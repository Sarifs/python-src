import requests
from PIL import Image
import pytesseract
import numpy as np

filename = 'Untitled.png'
img1 = np.array(Image.open(filename))
print(img1)
#text = pytesseract.image_to_string(img1)





# api-endpoint
""" URL = "http://challenge01.root-me.org/programmation/ch8/"

# location given here
# Creation session in so you don't have to handle cookies by yourself
s = requests.Session()
# sending get request and saving the response as response object
r = s.get(url = URL)
# extracting data in json format


# of the first matching location
parse = r.text
print(parse)
 """



