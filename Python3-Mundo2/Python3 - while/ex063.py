n = int(input('Escreva um numero para ve a sequencia de fibonacci: '))

t1 = 0
t2 = 1

print('{} -> {}'.format(t1,t2), end='')

count = 3
while count <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')    # 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13
    t1 = t2                               #             t1-t2-t3
    t2 = t3
    count += 1
print(' -> FIM')
    


