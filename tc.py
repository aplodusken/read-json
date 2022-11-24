# converter from frames, seconds to frames and the other way around

FPS = 25
someframes = 2373

secs = someframes // FPS

mins = secs // 60

hours = mins // 60
print("SECS = " + str(secs) + "\nMINS = " + str(mins))

