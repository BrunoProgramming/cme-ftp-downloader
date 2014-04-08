# This Python script will acquire the daily settlement file from
# the CME Group's FTP then un-archive it to a directory specified by
# the input parameters.
#
# This script is meant to be executed as a daily job via cron.
#
import os
from ftplib import FTP
import datetime

__author__ = 'Stewart Henderson'
host = "ftp.cmegroup.com"
remote_directory = '/settle'
now = datetime.datetime.now()
current_date = now.strftime('%Y%m%d')
local_directory = '/Users/stewart/dev/data/cme/' + current_date

if not os.path.exists(local_directory):
    os.makedirs(local_directory)
os.chdir(local_directory)

ftp = FTP(host)
ftp.login()
ftp.cwd(remote_directory)
files = ftp.nlst()

for file in files:
    if not file.endswith('.xml'):
        continue
    if current_date not in file:
        continue
    else:
        fhandle = open(file, 'wb')
        ftp.retrbinary('RETR ' + file, fhandle.write)
        fhandle.close()
    print files

