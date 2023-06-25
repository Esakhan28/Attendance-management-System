from MyQR import myqr
import os
import base64

#create and read
f = open('students.txt','r')
lines = f.read().split('\n')
print(lines)

for i in range(0,len(lines)):
    data = lines[i].encode()
    name = base64.b64encode(data)
    version, level,qr_name = myqr.run(
    str(name),
    level = 'H',
    version = 1,

    #background

    picture='bg.jpg',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name= str(lines[i]+'.bmp'),
    save_dir= os.getcwd()
)
