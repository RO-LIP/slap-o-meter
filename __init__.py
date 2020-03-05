import bhi160
import display
import leds
import utime

bhi = bhi160.BHI160Accelerometer()
disp = display.open()

highest = 0
while True:
	samples = bhi.read()
	if len(samples) == 0:
		utime.sleep(0.5)
		continue
	# print the latest sample
	disp.clear()
	#disp.print(str(samples[-1].x), posy=0, fg=[255, 255, 255])
	#disp.print(str(samples[-1].y), posy=20, fg=[255, 255, 255])
	#disp.print(str(samples[-1].z), posy=40, fg=[255, 255, 255])
	for val in samples:
		complete = abs(samples[-1].x + samples[-1].y + samples[-1].z)
		if complete > highest: highest = complete
	disp.print(str(highest), posy=40, fg=[255, 255, 255])
	disp.update()

	color = [0, 255, 0] if highest < 3 else [255, 0, 0]
	if highest > 1:
		leds.set(10, color)
	if highest > 1.5:
		leds.set(9, color)
	if highest > 2:
		leds.set(8, color)
	if highest > 2.5:
		leds.set(7, color)
	if highest > 3:
		leds.set(6, color)

	utime.sleep(1)
	leds.clear()
