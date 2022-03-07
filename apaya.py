from winsound import Beep
from time import sleep

g4 = 392
a4 = 440
b4 = 494
c5 = 524
d5 = 588
e5 = 660
f5 = 699
g5 = 784


duration = 1000

Beep(g4, duration//2)
Beep(g4, duration//2)
Beep(a4, duration//4*5)
Beep(g4, duration//2)
Beep(c5, duration//2)
Beep(b4, duration//4*5)

sleep(0.25)

Beep(g4, duration//2)
Beep(g4, duration//2)
Beep(a4, duration//4*5)
Beep(g4, duration//2)
Beep(d5, duration//2)
Beep(c5, duration//4*5)

sleep(0.25)

Beep(g4, duration//2)
Beep(g4, duration//2)
Beep(g5, duration//4*5)
Beep(e5, duration//2)
Beep(c5, duration//2)
Beep(b4, duration//4*5)
Beep(a4, duration//4*5)

sleep(0.25)

Beep(f5, duration//2)
Beep(f5, duration//2)
Beep(e5, duration//4*5)
Beep(c5, duration//4*5)
Beep(d5, duration//4*5)
Beep(c5, duration//4*5)
