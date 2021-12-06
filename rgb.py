def rgb(r,g,b):
    if r > 255:
        r=255
    if g > 255:
        g=255
    if b > 255:
        b=255
    if r < 0:
        r=0
    if g < 0:
        g=0
    if b < 0:
        b=0
    res =""
    if len(format(r,'x').upper())<2:
        res+='0'
    res+=format(r,'x').upper()
    if len(format(g,'x').upper())<2:
        res+='0'
    format(g,'x').upper()
    res+=format(g,'x').upper()
    if len(format(b,'x').upper())<2:
        res+='0'
    res+=format(b,'x').upper()
    return res
