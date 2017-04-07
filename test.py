# -*- coding: utf-8 -*- 

import datetime

if __name__ == "__main__":
    now = str(datetime.datetime.today())
    out = open("nowtime.txt","w")
    out.write(now)
    out.close()
