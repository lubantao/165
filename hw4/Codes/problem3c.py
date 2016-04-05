import psycopg2 as dbapi
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()


cur.execute("select housemonth \
from( \
(select tdaydate,(sum(CO2)*117538000/(count(distinct houseid)))/(10^6 ) as housemonth \
            from (select cast(trpmiles as float)/cast (epatmpg as float)*0.008887*30 AS CO2,tdaydate,houseid from ((select houseid,vehid,trpmiles,tdaydate from dayv2pub)S1 Natural Join (select houseid,vehid, epatmpg from vehv2pub) S2) S3 \
            where tdaydate in ('200804', '200806', '200809','200811',  '200904') and cast(trpmiles as float)>0 and cast(vehid as float)>0) M \
            group by tdaydate)\
\
union\
\
(select tdaydate,(sum(CO2)*117538000/(count(distinct houseid)))/(10^6 ) as housemonth \
            from (select cast(trpmiles as float)/cast (epatmpg as float)*0.008887*30 AS CO2,tdaydate,houseid from ((select houseid,vehid,trpmiles,tdaydate from dayv2pub)S1 Natural Join (select houseid,vehid, epatmpg from vehv2pub) S2) S3 \
            where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '200903') and cast(trpmiles as float)>0 and cast(vehid as float)>0) M\
             group by tdaydate)\
\
union\
\
(select tdaydate,(sum(CO2)*117538000/(count(distinct houseid)))/(10^6 ) as housemonth \
            from (select cast(trpmiles as float)/cast (epatmpg as float)*0.008887*30 AS CO2,tdaydate,houseid from ((select houseid,vehid,trpmiles,tdaydate from dayv2pub)S1 Natural Join (select houseid,vehid, epatmpg from vehv2pub) S2) S3 \
            where tdaydate in ('200902') and cast(trpmiles as float)>0 and cast(vehid as float)>0) M\
             group by tdaydate) ) T \
order by cast(tdaydate as integer);\
\
   ")

con.commit()
result = cur.fetchall()

cur.execute(" select sum(cast(value as float)) from eia where yyyymm in (select tdaydate from dayv2pub) and msn='TEACEUS' group by yyyymm order by cast(yyyymm as integer); ")

con.commit()
total = cur.fetchall()

for i in range(0,len(result)):
      temp= result[i][0]/total[i][0]
      print(temp)


cur.close()
con.close()
