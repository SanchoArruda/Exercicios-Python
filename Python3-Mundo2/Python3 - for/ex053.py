frase = str(input('Digite uma frase: ')).strip().upper() #strip= elimina os espaços antes e dps, upper= deixar a frase toda em maiuscula.

palavras = frase.split() #separa em um vetor, lista.
junto = ''.join(palavras) # juntei toda a lista em um str só
inverso = ''

for letra in range(len(junto) - 1, -1 , -1):  #fez o inverso da str, len() = retorna a quantidade de elementos, 
    inverso += junto[letra] #pega cada caracter na posicao letra e adiciona a inverso
print('O inverso de {} é: {}'.format(junto, inverso))

if inverso == junto: #faço a condição para ve se é o palindromo
    print('Esta frase é palindromo')
else:
    print('Essa frase não é palindromo')
