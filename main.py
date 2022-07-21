import time
print('{:-^60}'.format(''))
print('{:-^60}'.format(' BOMB TIMER '))
print('{:-^60}'.format(''))

timer = int(input('SELECIONE O TEMPO EM SEGUNDOS PARA DETONAÇÃO: '))
for i in range(timer, -1, -1):
    print(i)
    time.sleep(1)
print('Bye! Bye! BUM!!!')
