# Chapter 5 exercises from Zelle's python book. SaidakbarP 12/25/2019
s1 = "ni!"
print(s1.upper().ljust(4)*3)

msg = ""
for ch in "secret":
    msg = msg + chr(ord(ch)+1)
print(msg)

print("Hello {0}".format("Susan", "Computewell"))

print("{:7.5f}".format(2.3))

print("{1:3}".format(15))
