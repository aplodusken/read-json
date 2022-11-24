def frames_to_timecode(frames, fps=24):
    s, f = divmod(frames, fps)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return '{1:02d}:{2:02d}:{3:02d}:{4:02d}'.format(d, h,m,s,f)