

# outer = "NBXORNVRHGSZGLUXFIRLHRGB GSRHRHLFIDLIOWMLD RZNZSZXPVI URMWXOZIRGBRM5WVKGSC7DRWGS"
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# trans = str.maketrans(alphabet, alphabet[::-1], ' ')
# print(outer.translate(trans))

# Output: MYCLIMEISTHATOFCURIOSITYTHISISOURWORLDNOWIAMAHACKERFINDCLARITYIN5DEPTHX7WIDTH


# cipher = "WEAWTHEROWAAHRETNOKTWDWWHEHWHISEEANKAEARIBITXTONI2SUFOAATON1LTRX8LHMO7"
# rows = 7
# cols = 5
# len = len(cipher)
# half = int(len/2)

# cipher1 = cipher[:half]
# cipher2 = cipher[half:len]


# for col in range(cols):
#         print(cipher1[col::cols])
# print()

# for col in range(cols):
#         print(cipher2[col::cols])
# print()


# X2A187
# inner = "6C770081B61E380BC4E6586B52D5EF4F3821E0CE644C31EEC90A5013C2EC4F6A0181C442791ECDE2447F1781EF4B6B52C3F5456D15C9F30A6C1DC6E25E7017D3A75A7D1DD1EB4F3805C8F3423807CFEE5B6D1781F441711ECDF4063811D4F5437707D2EE5E6152C0E94E381BCCE64D711CC0F343771C81F345381DD1E2587906C4A7437652D5EF4F3801CDEE473813D3E24B3810C4F35D7D17CFA75E701781E3437E14C8E45F740681E6447C52D5EF4F381BCCF7456B01C8E5467D5C"



# import requests

# request = requests.get('https://www.google.com/')
# if request.status_code == 200:
#         print(request.content) 


# def dynamic_args(*bob):
#         for arg in bob:
#                 print(arg, end = " ")
        
#         print()

# dynamic_args("Welcome", "To", "Python")


a = True
b = False

print("    A\t\t   B\t\t  A and B\t A or B\t\t not A")
print("  ", a, "\t ", a, "\t\t  ", a and a, "\t ", a or a, "\t\t ", not a)
print("  ", a, "\t ", b, "\t  ", a and b, "\t ", a or b, "\t\t ", not a)
print("  ", b, "\t ", a, "\t\t  ", b and a, "\t ", b or a, "\t\t ", not b)
print("  ", b, "\t ", a, "\t\t  ", b and b, "\t ", b or b, "\t ", not b)

# print()
# print()
# print()

# format = "  {}\t\t{}\t\t{}\t\t{}\t\t{}"
# print("   A\t\t  B\t  A & B\t\tA | B\tA ^ B")
# print(format.format(a, a, a and a, a | a, a & a))
# print(format.format(a, b, a and b, a | b, a & b))
# print(format.format(b, a, b and a, b | a, b & a))
# print(format.format(b, b, b and b, b | b, b & b))


# print()
# print(f'{"A":^10}\t{"B":^10}\t{"A & A":^10}\t{"A | A":^10}\t{"A ^ A":^10}')
# print(f'{str(a):^10}\t{a:^10}\t{a and a:^10}\t{a or a:^10}\t{not a:^10}')
# print(f'{a:^10}\t{b:^10}\t{a and b:^10}\t{a or b:^10}\t{not b:^10}')
# print(f'{b:^10}\t{a:^10}\t{b and a:^10}\t{b or a:^10}\t{not a:^10}')
# print(f'{b:^10}\t{b:^10}\t{b and b:^10}\t{b or b:^10}\t{not b:^10}')
