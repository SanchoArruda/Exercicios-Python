#criando um conjunto vazio

s = set()

#adicionando elementos ao conjunto

s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

s.remove(2)
print(s)

print("Existe {} elementos dentro do conjunto {}".format(len(s), s))