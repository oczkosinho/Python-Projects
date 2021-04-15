from faker import Faker
fake=Faker(['pl_PL', 'en_US', 'cs_CZ', 'de_DE', 'en_GB', 'fr_FR', 'hu_HU','sk_SK','it_IT', 'es_ES'])
Faker.seed(1234)
f=open("excel hotel.txt","a", encoding="utf8")


for x in range(800):
    f.write(fake['en_US'].city() + fake.random_element(elements=(' Hotel', ' Apartment', ' Motel')) + ', '+ str(fake.random_int(min=0, max=400, step=1)) + ', '+ str(fake.random_int(min=1, max=5, step=1)) + ', '+ fake.street_name() + ', '+ str(fake.date_between(start_date='-200d', end_date='-40d')) + ', '+ str(fake.date_between(start_date='+50d', end_date='+300d')) + '\n')


f.close()
