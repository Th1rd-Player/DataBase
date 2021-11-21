import sqlite3
from fuzzywuzzy import fuzz

sqlite_connection = sqlite3.connect(r'D:\ULTRON\Files\0,001sys-rep\DataBase\test-base.db')
cur = sqlite_connection.cursor()
print("База данных создана и успешно подключена к SQLite")

sqlite_select_query = "select sqlite_version();"
cur.execute(sqlite_select_query)
record = cur.fetchall()
print("Версия базы данных SQLite: ", record)
cur.execute("SELECT * FROM com")
alias = cur.fetchall()
print(alias)






one_result = cur.execute("SELECT * from com;").fetchall()
'''
total_rows = str(total_rows)
total_rows = total_rows.split(",")[0]
total_rows = total_rows.split("(")[1]
nus = int(total_rows)






num = 0
asd = tuple([("система")])
while True:
    asd = tuple(asd+ alias[num])
    num += 1
    if nus == num:
        break
print(asd)
voice = input(":")

if voice.startswith(asd):
    print("1")
    cmd = voice

    for x in a:
        cmd = cmd.replace(x, "").strip()
        print("2")

    #for x in opts['tbr']:
    #    cmd = cmd.replace(x, "").strip()
    voice = cmd
    print(cmd, "help me please")
#for c,v in one_result:
#    print(c)
#    print(v)
'''
cmd = input("::):")
RC = {'id': '', 'percent': 0}
for c, v in one_result:
    print(c)
    vrt = fuzz.ratio(cmd, v)
    #print(v, ":",vrt)
    if vrt > RC['percent']:
        RC['id'] = c
        RC['percent'] = vrt


print(RC)

        
        
