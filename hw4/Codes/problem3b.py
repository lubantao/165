import psycopg2 as dbapi
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()

for i in range(1, 21):
     cur.execute ("select sum(trip*31)\
from(\
    select distinct  *  from ( \
        ( select houseid, vehid, tdaydate,cast(trpmiles as float) as trip \
          from dayv2pub \
          where cast(trpmiles as float) <%f and cast(trpmiles as float) >0 and cast(vehid as float) >=1) M natural join vehv2pub) N ) P \
where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '20903');  \
"%(i*5) )
     con.commit()
     bottom1=float(cur.fetchall()[0][0])

     cur.execute ("select sum(trip*31*cast(epatmpg as float)) \
from( \
    select distinct  *  from (  \
        ( select houseid, vehid, tdaydate,cast(trpmiles as float) as trip  \
          from dayv2pub  \
          where cast(trpmiles as float) <%f and cast(trpmiles as float) >0 and cast(vehid as float) >=1) M natural join vehv2pub) N ) P \
where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '20903'); "%(i*5) )
     con.commit()
     top1=float(cur.fetchall()[0][0])

     cur.execute ("select sum(trip*30) \
from( \
    select distinct  *  from (  \
        ( select houseid, vehid, tdaydate,cast(trpmiles as float) as trip  \
          from dayv2pub  \
          where cast(trpmiles as float) <%f and cast(trpmiles as float) >0 and cast(vehid as float) >=1) M natural join vehv2pub) N ) P \
where tdaydate in ('200804', '200806', '200809','200811',  '200904');"%(i*5) )
     con.commit()
     bottom2=float(cur.fetchall()[0][0])

     cur.execute ("select sum(trip*30*cast(epatmpg as float)) \
from( \
    select distinct  *  from (  \
        ( select houseid, vehid, tdaydate,cast(trpmiles as float) as trip  \
          from dayv2pub  \
          where cast(trpmiles as float) <%f and cast(trpmiles as float) >0 and cast(vehid as float) >=1) M natural join vehv2pub) N ) P \
where tdaydate in ('200804', '200806', '200809','200811',  '200904'); \
"%(i*5) )
     con.commit()
     top2=float(cur.fetchall()[0][0])

     cur.execute ("select sum(trip*28) \
from( \
    select distinct  *  from (  \
        ( select houseid, vehid, tdaydate,cast(trpmiles as float) as trip  \
          from dayv2pub  \
          where cast(trpmiles as float) <%f and cast(trpmiles as float) >0 and cast(vehid as float) >=1) M natural join vehv2pub) N ) P \
where tdaydate in ('200902');"%(i*5) )
     con.commit()
     bottom3=float(cur.fetchall()[0][0])

     cur.execute ("select sum(trip*28*cast(epatmpg as float)) \
from( \
    select distinct  *  from (  \
        ( select houseid, vehid, tdaydate,cast(trpmiles as float) as trip  \
          from dayv2pub  \
          where cast(trpmiles as float) <%f and cast(trpmiles as float) >0 and cast(vehid as float) >=1) M natural join vehv2pub) N ) P \
where tdaydate in ('200902');"%(i*5) )
     con.commit()
     top3=float(cur.fetchall()[0][0])

     x = (top1+top2+top3)/(bottom1+bottom2+bottom3)
     print(x)


cur.close()
con.close()
