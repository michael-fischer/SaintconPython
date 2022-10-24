a = 0
b = 1
print(f'{"A":^10}\t{"B":^10}\t{"A & B":^10}\t{"A | B":^10}\t{"A ^ B":^10}')
print(f'{a:^10}\t{a:^10}\t{a & a:^10}\t{a | a:^10}\t{a ^ a:^10}')
print(f'{a:^10}\t{b:^10}\t{a & b:^10}\t{a | b:^10}\t{a ^ b:^10}')
print(f'{b:^10}\t{a:^10}\t{b & a:^10}\t{b | a:^10}\t{b ^ a:^10}')
print(f'{b:^10}\t{b:^10}\t{b & b:^10}\t{b | b:^10}\t{b ^ b:^10}')

#results
#    A               B             A & A           A | A           A ^ A   
#    0               0               0               0               0     
#    0               1               0               1               1     
#    1               0               0               1               1     
#    1               1               1               1               0 


a = 5
b = 6
print()
print(f'{"A":^10}\t{"B":^10}\t{"A & B":^10}\t{"A | B":^10}\t{"A ^ B":^10}')
print(f'{a:^10}\t{b:^10}\t{a & b:^10}\t{a | b:^10}\t{a ^ b:^10}')

#results
#    A               B             A & A           A | A           A ^ A   
#    0               0               0               0               0     
#    0               1               0               1               1     
#    1               0               0               1               1     
#    1               1               1               1               0 