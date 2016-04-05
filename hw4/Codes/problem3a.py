import psycopg2 as dbapi
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()

cur.execute ("select sum(individual) as tt \
 from(select count(distinct houseid) as individual \
  from ( select cast(trpmiles as float) as miles, personid, houseid from dayv2pub where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '20903') and cast(trpmiles as float)>0 ) A \
  group by houseid, personid) B;" )
con.commit()
day31=float(cur.fetchall()[0][0])

cur.execute (" select sum(individual) as tt \
 from(select count(distinct houseid) as individual \
  from ( select cast(trpmiles as float) as miles, personid, houseid from dayv2pub where tdaydate in ('200804', '200806', '200809','200811',  '200904') and cast(trpmiles as float)>0 ) A \
  group by houseid, personid) B;" )

con.commit()
day30=float(cur.fetchall()[0][0])

cur.execute (" select sum(individual) as tt \
 from(select count(distinct houseid) as individual \
  from ( select cast(trpmiles as float) as miles, personid, houseid from dayv2pub where tdaydate in ('200902') and cast(trpmiles as float)>0 ) A \
  group by houseid, personid) B;" )

con.commit()
day28=float(cur.fetchall()[0][0])


for i in range(1, 21):
     cur.execute ("select sum(individual) as tt \
                  from(select count(distinct houseid) as individual \
                  from ( select cast(trpmiles as float) as miles, personid, houseid from dayv2pub where tdaydate in ('200803', '200805', '200807','200808', '200810', '200812', '200901', '20903') and cast(trpmiles as float)>0 ) A \
                   group by houseid, personid \
                   having sum(miles)<%f) B;"%(i*5) )
     con.commit()
     temp1=float(cur.fetchall()[0][0])
     cur.execute ("select sum(individual) as tt \
                  from(select count(distinct houseid) as individual \
                  from ( select cast(trpmiles as float) as miles, personid, houseid from dayv2pub where tdaydate in ('200804', '200806', '200809','200811',  '200904') and cast(trpmiles as float)>0 ) A \
                   group by houseid, personid \
                   having sum(miles)<%f) B;"%(i*5) )
     con.commit()
     temp2=float(cur.fetchall()[0][0])
     cur.execute ("select sum(individual) as tt \
                  from(select count(distinct houseid) as individual \
                  from ( select cast(trpmiles as float) as miles, personid, houseid from dayv2pub where tdaydate in ('200902') and cast(trpmiles as float)>0 ) A \
                   group by houseid, personid \
                   having sum(miles)<%f) B;"%(i*5) )
     con.commit()
     temp3=float(cur.fetchall()[0][0])
     x = (temp1*31+temp2*30+temp3*28)/(31*day31+30*day30+28*day28)
     print(x)

cur.close()
con.close()
