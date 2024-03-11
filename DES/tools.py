#x = "001F3887797B0F83"
#key = "0E329232EA6D0D73"
a=[1,2,3,4,5]
b=[2,3,4,5,6]
def xor (arr1,arr2):
    res= ""
    for i in range (len(arr1)):
        if arr1[i] == arr2[i]:
            res=res + "0"
        else:
            res=res + "1"
    res_final = list(res)
    return res_final

def left_shift(half_key,shift):
    store = ""
    for i in range(0,int(shift)):
       for j in range(1, len(half_key)):
          store = store + half_key[j]
       store = store + half_key[0]   
       half_key = store
       store = ""
    return half_key