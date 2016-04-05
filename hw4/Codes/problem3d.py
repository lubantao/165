import psycopg2 as dbapi
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()

cur.execute(''' select cast(CO2 as float)/cast(kwh as float) as co2perKwh
from (
(select yyyymm,value as CO2
from eia
where msn='TXEIEUS' and yyyymm in (select tdaydate from dayv2pub))A
Natural Join
(select yyyymm,value as kwh
from eia
where msn='ELETPUS' and yyyymm in (select tdaydate from dayv2pub))B)C
order by cast(yyyymm as float); ''')

con.commit()
unit = cur.fetchall()


cur.execute('''select housemonth
from(
(select tdaydate, sum(CO2) as housemonth
            from (select cast(trpmiles as float)/cast (epatmpg as float)*0.008887*30 AS CO2,tdaydate,houseid from ((select houseid,vehid,trpmiles,tdaydate from dayv2pub)S1 Natural Join (select houseid,vehid, epatmpg from vehv2pub) S2) S3
            where tdaydate in ('200804', '200806', '200809','200811',  '200904') and cast(trpmiles as float)>0 and cast(vehid as float)>0) M
            group by tdaydate)\

union

(select tdaydate,sum(CO2) as housemonth \
            from (select cast(trpmiles as float)/cast (epatmpg as float)*0.008887*30 AS CO2,tdaydate,houseid from ((select houseid,vehid,trpmiles,tdaydate from dayv2pub)S1 Natural Join (select houseid,vehid, epatmpg from vehv2pub) S2) S3 \
            where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '200903') and cast(trpmiles as float)>0 and cast(vehid as float)>0) M\
             group by tdaydate)

union

(select tdaydate,sum(CO2) as housemonth
            from (select cast(trpmiles as float)/cast (epatmpg as float)*0.008887*30 AS CO2,tdaydate,houseid from ((select houseid,vehid,trpmiles,tdaydate from dayv2pub)S1 Natural Join (select houseid,vehid, epatmpg from vehv2pub) S2) S3
            where tdaydate in ('200902') and cast(trpmiles as float)>0 and cast(vehid as float)>0) M
             group by tdaydate) ) T
order by cast(tdaydate as integer);
    ''')
con.commit()
oldtotal = cur.fetchall()

for i in range(1, 4):
      print ("When X is %d miles:"%(20*i))
      cur.execute('''
select  CO2
from

((select tdaydate, sum((cast(trpmiles as float)-%f)/cast(epatmpg as float))*0.008887*30 as CO2
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200804', '200806', '200809','200811',  '200904') and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)>%f and cast(trpmiles as float)>0
group by tdaydate)

union

(select tdaydate, sum((cast(trpmiles as float)-%f)/cast(epatmpg as float))*0.008887*31 as CO2
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '200903')  and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)>%f and cast(trpmiles as float)>0
group by tdaydate)

union

(select tdaydate, sum((cast(trpmiles as float)-%f)/cast(epatmpg as float))*0.008887*28 as CO2
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200902')  and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)>%f and cast(trpmiles as float)>0
group by tdaydate)) TT

order by cast(tdaydate as float);
'''%(i*20,i*20,i*20,i*20,i*20,i*20))

      con.commit()
      old = cur.fetchall()

      cur.execute('''
        select   KWh
from
((select tdaydate, sum(cast(trpmiles as float)/(cast(epatmpg as float)*0.090634441)*30) as KWh
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200804', '200806', '200809','200811',  '200904') and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)<%f and cast(trpmiles as float)>0
group by tdaydate)

union

(select tdaydate, sum(cast(trpmiles as float)/(cast(epatmpg as float)*0.090634441)*31) as KWh
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '200903') and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)<%f and cast(trpmiles as float)>0
group by tdaydate)

union

(select tdaydate, sum(cast(trpmiles as float)/(cast(epatmpg as float)*0.090634441)*28) as KWh
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200902') and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)<%f and cast(trpmiles as float)>0
group by tdaydate) ) NN

order by cast(tdaydate as integer);'''%(i*20,i*20,i*20))
      con.commit()
      new = cur.fetchall()

      cur.execute('''select  KWh
from
((select tdaydate, sum(%f/(cast(epatmpg as float)*0.090634441))*30 as KWh
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200804', '200806', '200809','200811',  '200904') and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)>=%f
group by tdaydate)

union

(select tdaydate, sum(%f/(cast(epatmpg as float)*0.090634441))*31 as KWh
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '200903') and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)>=%f
group by tdaydate)

union

(select tdaydate, sum(%f/(cast(epatmpg as float)*0.090634441))*28 as KWh
from ((select houseid,vehid,trpmiles,tdaydate
      from dayv2pub)S1
      Natural Join
      (select houseid,vehid, epatmpg
       from vehv2pub) S2) S3
where tdaydate in ('200902') and cast(trpmiles as float)>0 and cast(vehid as float)>0
      and cast(trpmiles as float)>=%f
group by tdaydate) ) NN

order by cast(tdaydate as integer);
        '''%(i*20, i*20,i*20,i*20,i*20,i*20))

      con.commit()
      new2 = cur.fetchall()

      for i in range(0,len(old)):

         temp= (oldtotal[i][0]-(new[i][0]*unit[i][0]+new2[i][0]*unit[i][0]+old[i][0]))/oldtotal[i][0]

         print(temp)


cur.close()
con.close()
