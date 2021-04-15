from faker import Faker
fake=Faker(['pt_PT', 'pl_PL'])
Faker.seed(1234)
f=open("numerki.txt","a", encoding="utf8")

for x in range(10000):
    f.write(str(fake.random_int(min=1, max=6, step=1)) + '\n')

f.close()
