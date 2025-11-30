import requests



# api-endpoint
URL = "http://challenge01.root-me.org/programmation/ch8/"

# location given here
# Creation session in so you don't have to handle cookies by yourself
s = requests.Session()
# sending get request and saving the response as response object
r = s.get(url = URL)
# extracting data in json format


# of the first matching location
parse = r.text
print(parse)




