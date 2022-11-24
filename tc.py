# converter from frames, seconds to frames and the other way around

fps = 25
someframes = 15546239


def framestotc(someframes, fps):

    s, f = divmod(someframes, fps)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return '{1:02d}:{2:02d}:{3:02d}:{4:02d}'.format(d, h,m,s,f)






