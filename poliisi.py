#!/usr/bin/python3
import blessed
import time
import math
import os
t = blessed.Terminal()
light = "▬▬▬"
flash = ""
light2 = "\\ | /"
indent = 0
maxi = os.get_terminal_size()[0]
speed = 7
flash_on = True

def police_car():
    return f"""{'=' * maxi}
{flash}
{' ' * indent} __{light}{t.navy}_____{t.normal}_______________{light}____
{' ' * indent}/{t.on_white}     {t.navy}█████{t.normal}{t.on_white}   _________     {t.normal}{t.on_blue}|    \\{t.normal}
{' ' * indent}|{t.on_white}     {t.navy}█████{t.normal}{t.on_white}  {t.normal}{t.on_black}|         |{t.on_white}    {t.normal}{t.on_blue}|     \\{t.normal}
{' ' * indent}|{t.on_white}     {t.navy}█████{t.normal}{t.on_white}  {t.normal}{t.on_black}|_________|{t.on_white}    {t.normal}{t.on_blue}|_____{t.navy}_{t.normal}{t.on_blue}\\{t.normal}{t.navy}__{t.normal}_
{' ' * indent}|{t.on_white}     {t.navy}█████{t.normal}{t.on_white}   {t.navy}    POLIISI         {t.navy}████{t.normal}{t.on_white} {t.normal}{t.on_white}\\{t.normal}
{' ' * indent}|{t.on_white}     {t.navy}█{t.on_navy}{t.white}112{t.navy}█{t.normal}{t.on_white}                       {t.navy}████{t.normal}{t.on_white}  |{t.normal}
{' ' * indent}\\{t.on_white}_____{t.navy}█████{t.normal}{t.on_white}_______________________{t.navy}████{t.normal}{t.on_white}_/{t.normal}
{'- ' * math.floor(indent/2)}- {t.on_black}\\__/{t.normal}- - - - - - - - - - - - - {t.on_black}\\__/{t.normal}{'- ' * (math.floor((maxi-indent)/2)-20)}







{'=' * maxi}"""

for i in range(maxi):
    light = "▬▬▬"
    flash = ""
    light2 = "\\ | /"
    indent += speed
    if indent >= maxi-42:
        indent = 0
    policecar = police_car()
    x = ''.join([line for line in policecar.split('\n') if "▬▬▬" in line])
    x = [len(x) for x in x.split("▬▬▬")]
    if flash_on:
        light2 = t.navy + "\\ | /" + t.normal
        flash = f"{' ' * (x[0]-1)}{light2}{' ' * (x[1]-23)}{light2}{t.normal}"
        light = f"{t.navy}{t.on_navy}▬▬▬{t.normal}"
        flash_on = False
    else:
        flash_on = True
    policecar = police_car()
    print(policecar)
    time.sleep(0.3)
    os.system("clear")
