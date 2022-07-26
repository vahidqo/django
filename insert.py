import psycopg2

con = psycopg2.connect(
    database='PMWorks_II',
    user='postgres',
    password='vahid',
    host='localhost'
    )

cur = con.cursor()

data=[[1,"در انتظار دستور برنامه ریزی","ST01",2],[2,"در حال انجام",ST02,2],[3,"انجام شده","ST03",1],
      [4,"رد شده توسط برنامه ریزی","ST04",3],[5,"لغو","ST05",3],[6,"نیاز به اصلاح گزارش","ST06",2],
      [7,"منتظر تأمین قطعه یدکی","ST07",2],[8,"منتظر تأمین نیروی انسانی","ST08",2],[9,"منتظر تأمین پیمانکار","ST09",2],
      [10,"منتظر اجازه واحد تولید","ST10",2],[11,"نیاز به تأیید سرپرست","ST11",2],[12,"رد توسط سرپرست","ST12",3],
      [13,"نیاز به تأیید درخواست کننده","ST13",2],[14,"تأیید توسط درخواست کننده _ بسته شده","ST14",1],[15,"عدم تأیید درخواست کننده","ST15",2]]

for i in range(len(data)):
    wfl = str(data[i][0])
    st = str(data[i][1])
    sn = str(data[i][2])
    sc = str(data[i][3])
    sql= 'insert into "PMWorks_II_status" ("id", "StatusName", "StatusCode", "StatusCondition") values ('+wfl+', '+st+', '+sn+', '+sc+')'
    cur.execute(sql)
    con.commit()

data=[[2,2],[3,13],[5,5],[7,2],[8,2],[9,2],[10,2]]

for i in range(len(data)):
    wfl = str(data[i][0])
    st = str(data[i][1])
    sql= 'insert into "PMWorks_II_wrworelationstatus" ("StatusWOID_id", "StstusWRID_id") values ('+wfl+', '+st+')'
    cur.execute(sql)
    con.commit()


data=[[1,"صدور و گردش تأییدات درخواست کار"],
      [2,"تأیید برنامه ریزی"],
      [3,"گردش تأییدات درخواست کار انجام شده"],
      [4,"صدور دستورکار، ثبت و تأییدات گزارش دستورکار"]] 

for i in range(len(data)):
    wfl = str(data[i][0])
    st = str(data[i][1])
    sql= 'insert into "PMWorks_II_workflowlevel" ("id", "WorkflowLevelName") values ('+wfl+', '+st+')'
    cur.execute(sql)
    con.commit()


data=[[1,11,0],[1,1,10],[2,4,10],[3,13,0],[3,14,10],
      [3,15,10],[4,2,0],[4,5,1],[4,7,1],[4,8,1],
      [4,9,1],[4,10,1],[4,3,10]]

for i in range(len(data)):
    wfl = str(data[i][0])
    st = str(data[i][1])
    wp = str(data[i][2])
    sql= 'insert into "PMWorks_II_workflowlevelstatus" ("WorkflowLevelID_id", "StatusID_id", "WorkflowLevelStatusPeriority") values ('+wfl+', '+st+', '+wp+')'
    cur.execute(sql)
    con.commit()


data = [[1,1],[1,12],[2,4],[7,5],[7,7],
        [7,8],[7,9],[7,10],[7,3],[8,5],
        [8,7],[8,8],[8,9],[8,10],[8,3],
        [9,5],[9,7],[9,8],[9,9],[9,10],
        [9,3],[10,5],[10,7],[10,8],[10,9],
        [10,10],[10,3],[11,5],[11,7],[11,8],
        [11,9],[11,10],[11,3],[12,5],[12,7],
        [12,8],[12,9],[12,10],[12,3],[4,14],
        [4,15]]

for i in range(len(data)):
    wfl = str(data[i][0])
    st = str(data[i][1])
    sql= 'insert into "PMWorks_II_workflowlevelstatusshow" ("WorkflowLevelStatusID_id", "StatusID_id") values ('+wfl+', '+st+')'
    cur.execute(sql)
    con.commit()




print(" insert done! ")

cur.close()

con.close()
