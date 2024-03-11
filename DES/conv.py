#x = "001F3887797B0F83"
#key = "0E329232EA6D0D73"
#0000111000110010100100100011001011101010011011010000110101110011
#----------------- binary to hexadicimal ----------------------#

def binaryToHexadecimal(num):
    #to convert from binary to hexadecimal group each 4-bits then convert to hexadecimal digit
    result = ""
    #make an empty string called intermediate to store each 4-bits within
    intermediate = ""
    #make a variable called counter to count the number of added characters to intermediate
    counter = 0
    #make sure that the string can be grouped to 3-bits
    #if not, fill the string with 0s at the beginning
    if len(num)%4 != 0:
        num = "0"*(4-(len(num)%4)) + num
    #loop through the number string and store each binary character to intermediate string
    for i in range(len(num)-1, -1, -1):
        intermediate += num[i]
        counter += 1
        #when the number of added characters reaches 4, convert them to hexadecimal digit
        if counter == 4:
            #reverse the intermediate string first
            intermediate = intermediate[::-1]
            digit = 0
            #length of intermediate is always 4; therefore, instead of len(intermediate) replace it with 4
            #convert to hexadecimal digit
            for j in range(3, -1, -1):
                if intermediate[j] == '1':
                    digit += 2**(3-j)
            if digit <= 9:
                result += str(digit)
            else:
                digit = chr(ord('A')+digit-10)
                #add the value of the hexadecimal digit to the result string
                result += digit
            #after converting,  set counter to 0 and intermediate to be empty to repeat the cycle
            counter = 0
            intermediate = ""
    #reverse result string
    result = result[::-1]
    return result 

#----------------- hexadecimal to binary ----------------------#

def hexadecimalToBinary(num):
    result = ""
    #loop through the entire string and convert each hexadecimal number to binary form of 4-bits
    #no need to loop starting from the end
    for i in range(len(num)):
        #get the value of the hexadecimal digit
        if num[i] >= "0" and num[i] <= "9":
            digit = int(num[i])
        else:
            digit = ord(num[i])-ord('A')+10
        #make a binary_num variable to store the binary form of each digit
        binary_num = ""
        while digit > 0:
            #add the string value of the remainder of dividing the hexadecimal digit with 2
            binary_num += str(digit%2)
            #do floor division to the digit to get the value of the digit without remainder
            digit //= 2
        #reverse the binary_num string
        binary_num = binary_num[::-1]
        #when the binary number is represented by less than 4-bits, add 0s to the left of the number
        if len(binary_num) < 4:
            binary_num = "0"*(4-len(binary_num))+binary_num
        #add the value of the binary number to the result string
        result += binary_num
    return result

#--------------------------- Binary to Decimal -------------------------#

def binaryToDecimal(num):
    result = 0
    #loop through the number string and when finding 1, add value of 2 raised to the power of its length of the string minus the index to result
    for i in range(len(num)-1, -1, -1):
        if num[i] == '1':
            result += 2**(len(num)-1-i)
    return result

#-------------------------- Decimal to binary ---------------------------#

def decimalToBinary(num):
    #assign empty string value for result
    result = ""
    #convert the string of the number into integer value to do operations
    num_int = int(num)
    while num_int > 0:
        #get the remainder of dividing the number by 2 to convert to binary form
        num_digit = num_int%2
        result += str(num_digit)
        #do floor division to the number to get the number without remainders
        num_int = num_int//2
    #reverse the result string
    result = result[::-1]
    return result