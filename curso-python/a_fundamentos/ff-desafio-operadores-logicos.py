#os trabalhos:

trabalho_terca = False
trabalho_quinta = False

'''
- confirmado os 2 trabalhos: TV 50 pol + sorvete.
- confirmado apenas 1 trabalho: TV 32 + sorvete.
- nenhum trabalho confirmado: fica em casa e tem mais saúde.
'''

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_quinta != trabalho_terca
sorvete = trabalho_terca or trabalho_quinta
mais_saude = not sorvete

print('TV 50:{}. TV 32:{}. Sorvete:{}. Mais saudável:{}.'.format(tv_50, tv_32, sorvete, mais_saude))
print('TV 50:{0}. TV 32:{1}. Sorvete:{2}. Mais saudável:{3}.'.format(tv_50, tv_32, sorvete, mais_saude))