from faker import Faker
fake=Faker(['pt_PT', 'pl_PL'])
Faker.seed(1234)
f=open("snapshot.txt","a", encoding="utf8")

for x in range(1,46):
    f.write("update Airlines set " + "'Name' = "+ "'" + fake.company()+ "'" +','+ 'where ID =' + "'" + str(x)+ "'" +';\n')

for x in range(50000):
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='+40d', end_date='+60d')) + "'" +', '+ "'" + str(fake.date_between(start_date='+50d', end_date='+70d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='+100d', end_date='+120d')) + "'" +', '+ "'" + str(fake.date_between(start_date='+130d', end_date='+150d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='+200d', end_date='+210d')) + "'" +', '+ "'" + str(fake.date_between(start_date='+211d', end_date='+221d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='-190d', end_date='-170d')) + "'" +', '+ "'" + str(fake.date_between(start_date='-180d', end_date='-160d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='-90d', end_date='-70d')) + "'" +', '+ "'" + str(fake.date_between(start_date='-80d', end_date='-60d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')

for x in range(100):
    f.write("INSERT INTO Insurance VALUES ("+ "'" + fake.company() + "'" +', '+ "'" + fake.numerify(text='######') + "'"  + ')\n')

for x in range(10000):
    f.write("INSERT INTO Hotels VALUES ("+ "'" + fake['en_US'].city() + fake.random_element(elements=(' Hotel', ' Apartment', ' Motel')) + "'" +', '+ "'" + str(fake.random_int(min=0, max=100, step=1)) + "'" + ')\n')


f.close()