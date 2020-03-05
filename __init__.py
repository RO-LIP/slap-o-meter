import bhi160
import buttons
import display
import leds
import utime

# init
bhi = bhi160.BHI160Accelerometer(sample_rate=4)
disp = display.open()
leds.clear()
highest = 0

while True:
	# reset if button pressed
	pressed = buttons.read(buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT)
	if pressed & buttons.BOTTOM_LEFT != 0: highest = 0

	# read accel
	samples = bhi.read()
	if len(samples) == 0:
		utime.sleep(0.25)
		continue

	for val in samples:
		complete = abs(val.x) + abs(val.y) + abs(val.z) - 1
		if complete > highest: highest = complete

	# update display
	disp.clear()
	disp.print("Slap force:", posy=0, fg=[255, 255, 255])
	disp.print("<- reset", posy=60, fg=[255, 0, 0])
	disp.print(str(highest), posy=20, posx=20, fg=[255, 255, 255])
	disp.update()

	# Update LEDs
	color = [0, 255, 0] if highest < 3 else [255, 0, 0]
	for i in range(0, 11):
		if highest*2 < i: color = [0, 0, 0] 
		leds.prep(10 - i, color)
	leds.update()

	utime.sleep(0.25)
