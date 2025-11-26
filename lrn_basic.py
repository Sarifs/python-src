#sub sequence
str = "expension"
print(str[2::]) # resulte  = pension
# find substring

s = "Babylone babies and saletile sisters"
index = s.find("sister")
print(index) # return the index of first letter of subsequence postion

#string to int

s = "42"
num = int(s)
print(num)

#Create function in pyton 

def my_function():
  print("Hello from a function")

# ternaire
age = 42
majorite = "Mineur" if age < 18 else "Majeur"


# WTSAT
x1 = 32
x2 = 65
s.send(f"x1: {x1:.3f} ; x2: {x2:.3f}\n".encode())
# You can add a variable into parenthese just add f a the begening of your message
# .3f show the resulte with .3f after the commat
# Your serveur might be waiting for \n as the end of your message
# the message sent must be encoded
