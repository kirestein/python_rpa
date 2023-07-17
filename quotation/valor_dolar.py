import pyautogui as pg
from date_time import *
from quotation import *
from position import *

#? abrindo o Google Chrome
pg.hotkey('win', 'c') #! o hotkey permite executar mais de uma tecla de atalho no computador.dolar
pg.PAUSE = 2

pg.sleep(2)

# print(pg.position())
#? selecionando o perfil do chrome
position = [947, 661]
pg.click(position[0], position[1])

pg.sleep(2)
#* getting date and time
date = f'{day}/{month}/{year}'
time = f'{hour}:{minutes}:{seconds}'
print(date)
print(time)
pg.click(options[0], options[1])
pg.sleep(2)
pg.click(drive[0], drive[1])
pg.sleep(2)
pg.click(search[0], search[1])
pg.typewrite('dollar')
pg.sleep(2)
pg.press('down')
pg.press('enter')
pg.sleep(5)
pg.press('down')
pg.typewrite(date)
pg.press('tab')
pg.typewrite(time)
pg.press('tab')
pg.typewrite(str(value).replace('.', ','))

# pg.keyDown('win')
# pg.press('q')
# pg.keyUp('win')
