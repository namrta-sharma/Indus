# This program prints out the entire song "99 bottles of beer"
i = 100
while i <=100:
    i-=1
    print(i,"Bottles of beer on the wall", i, "bottles of beer.")
    print("Take one down, pass it around", i-1, "bottles of beer on the wall.")
    if i <= 1:
        break
    
