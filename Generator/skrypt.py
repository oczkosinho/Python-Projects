from faker import Faker
fake=Faker(['pl_PL', 'en_US', 'cs_CZ', 'de_DE', 'en_GB', 'fr_FR', 'hu_HU','sk_SK','it_IT', 'es_ES'])
Faker.seed(1234)

f=open("insert.txt","w", encoding="utf8")

for x in range(100):
    f.write("INSERT INTO Airlines VALUES ("+ "'" + fake.company() + ' Airlines' +"'" + ')\n')

for x in range(100):
    f.write("INSERT INTO Insurance VALUES ("+ "'" + fake.company() + "'" + ')\n')

for x in range(40):
    f.write("INSERT INTO Destination VALUES (" + "'" + 'Spain' + "'" + ', ' + "'" + fake['es_ES'].city() + "'" + ', ' + "'" + str(fake.pyint(min_value=50, max_value=1000, step=1)) + "'" + ')\n')
    f.write("INSERT INTO Destination VALUES (" + "'" + 'Czech Republic' + "'" + ', ' + "'" + fake['cs_CZ'].city() + "'" + ', ' + "'" + str(fake.pyint(min_value=50, max_value=1000, step=1)) + "'" + ')\n')
    f.write("INSERT INTO Destination VALUES (" + "'" + 'Deutschland' + "'" + ', ' + "'" + fake['de_DE'].city() + "'" + ', ' + "'" + str(fake.pyint(min_value=50, max_value=1000, step=1)) + "'" + ')\n')
    f.write("INSERT INTO Destination VALUES (" + "'" + 'Great Britain' + "'" + ', ' + "'" + fake['en_GB'].city() + "'" + ', ' + "'" + str(fake.pyint(min_value=50, max_value=1000, step=1)) + "'" + ')\n')
    f.write("INSERT INTO Destination VALUES (" + "'" + 'France' + "'" + ', ' + "'" + fake['fr_FR'].city() + "'" + ', ' + "'" + str(fake.pyint(min_value=50, max_value=1000, step=1)) + "'" + ')\n')
    f.write("INSERT INTO Destination VALUES (" + "'" + 'Hungary' + "'" + ', ' + "'" + fake['hu_HU'].city() + "'" + ', ' + "'" + str(fake.pyint(min_value=50, max_value=1000, step=1)) + "'" + ')\n')
    f.write("INSERT INTO Destination VALUES (" + "'" + 'Slovakia' + "'" + ', ' + "'" + fake['sk_SK'].city() + "'" + ', ' + "'" + str(fake.pyint(min_value=50, max_value=1000, step=1)) + "'" + ')\n')
    f.write("INSERT INTO Destination VALUES (" + "'" + 'Italy' + "'" + ', ' + "'" + fake['it_IT'].city() + "'" + ', ' + "'" + str(fake.pyint(min_value=50, max_value=1000, step=1)) + "'" + ')\n')

for x in range(10000):
    f.write("INSERT INTO Hotels VALUES ("+ "'" + fake['en_US'].city() + fake.random_element(elements=(' Hotel', ' Apartment', ' Motel')) + "'" +', '+ "'" + str(fake.random_int(min=0, max=100, step=1)) + "'" + ')\n')

for x in range(10000):
    f.write("INSERT INTO Personnel VALUES ("+ "'" + fake.random_element(elements=('Tour Guide', 'Resident', 'Animator')) + "'" +', '+ "'" + fake.first_name() + "'" +', '+ "'" + fake.last_name() + "'" +', '+ "'" + str(fake.pyint(min_value=1, max_value=10000, step=1)) + "'" + ')\n')

for x in range(10000):
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='+40d', end_date='+60d')) + "'" +', '+ "'" + str(fake.date_between(start_date='+50d', end_date='+70d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='+100d', end_date='+120d')) + "'" +', '+ "'" + str(fake.date_between(start_date='+130d', end_date='+150d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='+200d', end_date='+210d')) + "'" +', '+ "'" + str(fake.date_between(start_date='+211d', end_date='+221d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='-190d', end_date='-170d')) + "'" +', '+ "'" + str(fake.date_between(start_date='-180d', end_date='-160d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')
    f.write("INSERT INTO Offers VALUES ("+ "'" + str(fake.date_between(start_date='-90d', end_date='-70d')) + "'" +', '+ "'" + str(fake.date_between(start_date='-80d', end_date='-60d')) + "'" +', '+ "'" + str(fake.random_int(min=1200, max=10000, step=100)) + "'" +', '+ "'" + str(fake.random_int(min=10, max=1000, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'"  +', '+ "'" + str(fake.random_int(min=1, max=100, step=1)) + "'" +', '+ "'" + str(fake.random_int(min=100000, max=999999, step=1)) + "'" +')\n')

for x in range(10000):
    f.write("INSERT INTO Facultative_Trips VALUES ("+ "'" + fake.color_name()  + ' Trip' "'" +', '+ + str(fake.pyint(min_value=10, max_value=66, step=1)) + "'" +', '+ "'" + fake.phone_number() + "'" + ')\n')

for x in range(10000):
    f.write("INSERT INTO Have VALUES ("+ "'" + str(fake.pyint(min_value=1, max_value=10000, step=1)) + "'" +', '+ "'" + str(fake.pyint(min_value=1, max_value=10000, step=1)) + "'" + ')\n')

f.close()
