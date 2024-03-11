
import conv, p, e, s, tools

rounds_keys = []

shifts = ['1', '1', '2', '2', '2', '2', '2', '2', '1', '2', '2', '2', '2', '2', '2', '1']

x = "52414D595741454C"
key = "1111111111111111"
perm_key = p.KeyPermutation(conv.hexadecimalToBinary(key))
left_key = perm_key[0: 28]
right_key = perm_key[28: 56]
for i in range(0,16):
    left_key = tools.left_shift(left_key,shifts[i])
    right_key = tools.left_shift(right_key,shifts[i])
    key_initial = left_key +right_key
    key_round = p.KeyPermutation2(key_initial)
    rounds_keys.append(key_round)

def data_encryption(plain_text):
    plain_text= conv.hexadecimalToBinary(plain_text)
    plain_text= p.intialpermutation(plain_text)
    left_data = plain_text[0:32]
    right_data = plain_text[32:64]
    round_res=[]
    for i in range(0,16):
        e_right = e.e_expand(right_data)
        first_xor= tools.xor(e_right,rounds_keys[i])
        intermediate1=s.sbox(first_xor)
        intermediate2=p.sboxpermutation(intermediate1)
        second_xor= tools.xor(intermediate2,left_data)
        round_res=right_data+second_xor
        left_data=round_res[0:32]
        right_data=round_res[32:64]
    final_round_swapped=round_res[32:64]+round_res[0:32]
    final_res=p.reversepermutaion(final_round_swapped)
    return final_res
print(conv.binaryToHexadecimal(data_encryption(x)))
#da02ce3a89ecac3b