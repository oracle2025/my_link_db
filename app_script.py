#!/usr/bin/env python3
import mechanicalsoup
import os
import sqlite3

browser = mechanicalsoup.StatefulBrowser()
browser.open("http://oracle.bunfet.me/blog/")
for link in browser.get_current_page().select('a'):
    print(link.attrs['href'])

# os.system("git status")
DBNAME='dates.db'
DBEXPORTFILE='db_export.sql'

os.system("git pull --rebase -s recursive -X ours origin master")

os.unlink(DBNAME)
# rm -f ${DBNAME}

# Import db from git
# cat ${DBEXPORTFILE} | sqlite3 ${DBNAME}

# db = sqlite3.
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE stocks
                     # (date text, trans text, symbol text, qty real, price
#                      real)''')
# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print c.fetchone()


# Insert a row of data
c.execute("insert into links(link) values(\"{}\");".format(link))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# The trivial 'application' here simply writes the date to a file.
# DATE="$(date '+%Y-%m-%d %H:%M:%S')"
# echo $DATE
# echo "insert into links(link) values(\"{}\");".format() | sqlite3 ${DBNAME}

# Export db from sqlite
# echo ".dump" | sqlite3 ${DBNAME} > ${DBEXPORTFILE}


# Commit the change made.
# git commit -am 'Update from app_script.sh'

# Push the changes to the origin.
# git push -u origin gitdb-sqlite
