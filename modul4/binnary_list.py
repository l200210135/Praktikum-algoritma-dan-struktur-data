def binSe(kumpulan,target):
    low = 0 # dimulai dari elem 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid]==target: ##jika target ada di tengah
            return True
        elif target < kumpulan[mid]: #mencari apakah kiri
            return True
        else:
            low = mid + 1 #apakah dikiri 

    return False
x=[3,1,2,4,5,6,7,8,9]
print(binSe(x,88))
print(binSe(x,3))
        