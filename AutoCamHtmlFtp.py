from ftplib import FTP
import pygame,os, datetime, time, fileinput
import pygame.camera
from pygame.locals import *

print 'Starting DAQ'
#---------------------------Loop for Repeat--------------------------------
while True:
    print 'Grabing Data'
    #-----------------------Set Desktop Path-------------------------------
    desktop = os.path.join(os.path.join(os.path.expanduser('~')),'Desktop')
    os.chdir(desktop)

    #-----------------------Get Time Date----------------------------------
    _dateTime = str(datetime.datetime.now())

    #-----------------------Get Camera Image-------------------------------
    pygame.init()
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0],(640,480))
        cam.start()
        img = cam.get_image()
        pygame.image.save(img,"picFile.jpg")
        cam.stop()

    #-----------------------Build HTML File--------------------------------
    file = open("index.html","w")
    file.write('<!DOCTYPE html>')
    file.write('<html>')
    file.write('<head>')
    file.write('<style>')
    file.write('img {')
    file.write('display: block;')
    file.write('margin-left: auto;')
    file.write('margin-right: auto;')
    file.write('}')
    file.write('h2 {')
    file.write('width: 100%;')
    file.write('text-align:center;')
    file.write('}')
    file.write('</style>')
    file.write('</head>')
    file.write('<body>')
    file.write('<img src="picFile.jpg" alt="cam" style="width:50%;">')
    file.write('<h2>')
    file.write(_dateTime)
    file.write('</h2>')
    file.write('</body>')
    file.write('</html>')
    file.close()

    #-----------------------UpLoad Files To FTP----------------------------
    ftp = FTP("")
    ftp.login("","")
    ftp.cwd('/public_html/')
    fp = open('index.html','rb')
    ftp.storbinary('STOR %s' % os.path.basename('index.html'),fp,1024)
    fp = open('picFile.jpg','rb')
    ftp.storbinary('STOR %s' % os.path.basename('picFile.jpg'),fp,1024)
    ftp.quit()

    #-----------------------Sleep Wait-------------------------------------
    print 'New Data Ready'
    count = 900
    for i in range(900):
        time.sleep(1)
        count = count - 1
        msg = str(count) + ' Seconds until next DAQ'
        print msg
