import board, displayio, random, time, terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label

lb = label.Label
display = board.DISPLAY
splash = displayio.Group()
display.show(splash)

random.seed(time.monotonic_ns())
data = []
for i in range(0, 95):
    data.append(random.randint(10, 100))

def showHistogram(myData, start = 0):
    splash = None
    splash = displayio.Group()
    color_bitmap = displayio.Bitmap(320, 240, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF
    bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
    splash.append(bg_sprite)
    last = start + 45
    if last > len(myData):
        last = len(myData) - 1
    minValue = 65535
    maxValue = -65535
    sumValues = 0
    for i in range(start, last):
        ix = i-start
        x = myData[i]
        if x>maxValue:
            maxValue = x
        if x<minValue:
            minValue = x
        sumValues += x
        px = 20+ix*3
        py = 120-x
        if ix%10 == 0:
            rect = Rect(px, py, 2, x, fill=0x00FFFF)
        else:
            rect = Rect(px, py, 2, x, fill=0x00FF00)
        splash.append(rect)
        #print(f"Drawing #{i}/{ix} = {x}: px: {px}, py: {py}")
    L0 = lb(terminalio.FONT, text=str(start))
    L0.color = 0
    L0.x = 18
    L0.y = 123
    splash.append(L0)
    L1 = lb(terminalio.FONT, text=str(start+10))
    L1.color = 0
    L1.x = 46
    L1.y = 123
    splash.append(L1)
    L2 = lb(terminalio.FONT, text=str(start+20))
    L2.color = 0
    L2.x = 76
    L2.y = 123
    splash.append(L2)
    L3 = lb(terminalio.FONT, text=str(start+30))
    L3.color = 0
    L3.x = 106
    L3.y = 123
    splash.append(L3)
    L4 = lb(terminalio.FONT, text=str(start+40))
    L4.color = 0
    L4.x = 136
    L4.y = 123
    splash.append(L4)
    average = "%0.1f" % (sumValues / 45)
    L5 = lb(terminalio.FONT, text=f"{start}->{last-1} Sum: {sumValues} Avg: {average}")
    L5.color = 0
    L5.x = 0
    L5.y = 7
    splash.append(L5)
    display.show(splash)

for i in range(0, 60):
    showHistogram(data, i)
    #time.sleep(0.2)
