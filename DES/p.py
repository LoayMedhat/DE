#--------KEY PERMUTATION 1-------------#

#x = "001F3887797B0F83"
#key = "0E329232EA6D0D73"

def KeyPermutation(keybin):
    permutatedkey = [] 
    keyp = [57, 49, 41, 33, 25, 17, 9,
              1, 58, 50, 42, 34, 26, 18,
              10, 2, 59, 51, 43, 35, 27,
              19, 11, 3, 60, 52, 44, 36,
              63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
              14, 6, 61, 53, 45, 37, 29,
              21, 13, 5, 28, 20, 12, 4]
    for i in range(0,56):
        permutatedkey.append(keybin[keyp[i]-1])
    return permutatedkey


#--------KEY PERMUTATION 2-------------#

def KeyPermutation2(keybin2):
    permutatedkey2 = []
    keyp2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
    for i in range(0,48):
        permutatedkey2.append(keybin2[keyp2[i]-1])

    return permutatedkey2

#------------------------------------------DATA----------------------------------------------#

#-------- DATA INITIAL PERMUTATION -------------#



def intialpermutation(databin):
    permutateddata = []
    datap = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]
    for i in range(0,64):
        permutateddata.append(databin[datap[i]-1])

    return permutateddata

#-------- DATA SBOX PERMUTATION -------------#



def sboxpermutation(databin):
    permutatedsboxdata = []
    datap = [16, 7, 20, 21, 29, 12, 28, 17, 1, 
             15, 23, 26, 5, 18, 31, 10, 2, 8, 
             24, 14, 32, 27, 3, 9, 19, 13, 30, 
             6, 22, 11, 4, 25]
    for i in range(0,32):
        permutatedsboxdata.append(databin[datap[i]-1])

    return permutatedsboxdata
#-------- REVERSE PERMUTATION -------------#



def reversepermutaion(databin):
    reversepermutateddata = []
    datap = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]
             
    for i in range(0,64):
        reversepermutateddata.append(databin[datap[i]-1])

    return reversepermutateddata
