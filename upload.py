from ftplib import FTP
import os, fileinput
ftp = FTP("")
ftp.login("","")
ftp.cwd('/public_html/')
fp = open('line.html','rb')
ftp.storbinary('STOR %s' % os.path.basename('line.html'),fp,1024)
ftp.quit()
