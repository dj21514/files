import pymysql



db = pymysql.connect("localhost","root","c1o0l0d8","EstusFlask" )
cursor = db.cursor()

cursor.execute("SELECT * FROM hospital")
hospital_data  = cursor.fetchall()
db.commit()

cursor.execute("SELECT * FROM diagnosis")
diagnosis_data = cursor.fetchall()
db.commit()


cursor.execute("SELECT * FROM patient")
patient_data   = cursor.fetchall()
db.commit()


for hospital in hospital_data:
  cursor.execute("INSERT INTO fact_table (hospital_id) VALUES (%d)" % hospital[0])

db.commit()

