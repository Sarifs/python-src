# root-me suite mathematique solution
import requests

# Code pour la suite 
# ux = Un 
# u0 = U0
# c0 et c1 correspondent aux constantes de la formulte
def stm(ux,u0,c0,c1):
    if ux == 0:
        return u0
    i = 0
    while (i < ux):
        u0 = (c0 + u0) - (i * c1)
        i = i + 1
    return u0


# api-endpoint
URL = "http://challenge01.root-me.org/programmation/ch1/"

# location given here
# Creation session in so you don't have to handle cookies by yourself
s = requests.Session()
# sending get request and saving the response as response object
r = s.get(url = URL)
# extracting data in json format


# of the first matching location
parse = r.text

index0 = parse.find("[")
lv0 = parse[index0::]

print(lv0)
sp =  lv0.split(' ')
# les valeurs suivantes ont ete determinees apres un split par un espace sur la chaine lvl0
#print (int(sp[1]))
#print (int(sp[9]))
#print (int(sp[13][:-4:]))
#print (int(sp[17][6:-9:]))

ret = stm(int(sp[17][6:-9:]),int(sp[13][:-4:]),int(sp[1]),int(sp[9]))
print(ret)
URL2 = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=" + str(ret)
print(URL2)
r = s.get(url = URL2)
parse = r.text
print(parse)



