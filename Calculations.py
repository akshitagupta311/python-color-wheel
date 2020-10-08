import math;

def xy2polar(x,y):
    print("X is = ",x)
    print("Y is = ",y)
    r = math.sqrt((x*x)+(y*y))
    print(r)
    theta = math.atan2(y,x)
    print(theta)

def polar2xy(r,t):
    x = math.cos(t)*r
    y = math.sin(t)*r
    print(x)
    print(y)

def hexa2rgb(a):
    if a[:1]=="#":
        b = a[1:]
    
    else:
        b = a
        
    print(b)
    r = b[0:2]
    g = b[2:4]
    b = b[4:6]
    print(r,g,b)
    rgb = [int(r,16),int(g,16),int(b,16)]
    return (rgb)

def rgb2hexa(r,g,b):
    
    rHex = hex(r)[2:]
    gHex = hex(g)[2:]
    bHex = hex(b)[2:]
    
    if len(rHex) == 1:
        rHex = "0" + rHex
    if len(gHex) == 1:
        gHex = "0" + gHex
    if len(rHex) == 1:
        bHex = "0" + bHex

    hexa = ('#' + rHex + gHex + bHex)
    
    print(hexa)

def rgb2hsl(r,g,b):
    r1 = r/255
    g1 = g/255
    b1 = b/255

    cmax = max(r1,g1,b1)
    cmin = min(r1,g1,b1)
    delta = cmax - cmin

    if delta == 0:
        h = 0
    elif cmax == r1:
        h = 60 * ((((g1-b1)/delta)) % 6)
    elif cmax == g1:
        h = 60 * (((b1-r1)/delta) + 2)
    elif cmax == b1:
        h = 60 * (((r1-g1)/delta) + 4)

    l = (cmax + cmin)/2

    if delta == 0:
        s = 0
    else:
        s = delta/(1-(abs(2*l-1)))

def hsl2rgb(h,s,l):
    c = (1-(abs(2*l-1))*s)
    x = c * (1- abs((h/60) % 2 - 1))
    m = l - c/2

    if h >= 0 and h < 60:
        (r1,g1,b1) = (c,x,0)
    elif h >= 60 and h < 120:
        (r1,g1,b1) = (x,c,0)
    elif h >= 120 and h < 180:
        (r1,g1,b1) = (0,c,x)
    elif h >= 180 and h < 240:
        (r1,g1,b1) = (0,x,c)
    elif h >= 240 and h < 300:
        (r1,g1,b1) = (x,0,c)
    elif h >= 300 and h < 360:
        (r1,g1,b1) = (c,0,x)
    
    (r,g,b) = ((r1+m)*255,(g1+m)*255,(b1+m)*255)


# xy2polar(5,12)
# polar2xy(13,1.17)

# hexa2rgb("#ad3267")
# hexa2rgb("ffffff")
# hexa2rgb("00ff00")
# rgb2hexa(00,00,255)

# rgb2hsl(48,69,53)

# hsl2rgb(300,1,0.5)