def nhapso(a):
  if a.islower:
    return a
  else:
    return a.upper()
a=input("nhập 1 chữ cái : ")
if a.isalpha() and len(a)==1:
  print(nhapso(a))
else:
    print("vui lòng nhập 1 chữ cái")
