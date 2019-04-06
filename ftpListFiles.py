import ftplib
ftp = ftplib.FTP("")
ftp.login("","")
data = []
ftp.cwd('/public_html/')
ftp.dir(data.append)
ftp.quit()
for line in data:
    print "-", line
