#解码微信撤回的图片
b = bytearray(open('a.dat', 'rb').read())
for i in range(len(b)):
    b[i] ^= 0x3A
open('b.jpg', 'wb').write(b)
