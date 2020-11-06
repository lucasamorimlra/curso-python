#tabela verdade AND
print(True and False)
print(True and True)
print(False and False)
print(False and True)
print('')

#tabela verdade OR
print(True or False)
print(True or True)
print(False or False)
print(False or True)
print('')

#tabela verdade XOR (OR "exclusivo" ). Na pratica, é sinal DIFERENTE
print(True != False)
print(True != True)
print(False != False)
print(False != True)
print('')

#operadores de negação (unários)
print(not True)
print(not False)
print(not not True)
print(not not not True)
print('')


#cuidado! não confundir operadores lógicos com operadores bit-a-bit
print(True & False)
print(True | False)
print(True ^ False)
print('')

#exemplo prático:

saldo = 1000
salario = 4000
despesas = 2000

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas

print(meta)