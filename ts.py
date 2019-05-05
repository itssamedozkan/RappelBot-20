string = "abcd"
try:
    i = int(string)
    print(i)
except ValueError:
    #Handle the exception
    i = 0

print(i)