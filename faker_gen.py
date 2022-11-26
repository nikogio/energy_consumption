from faker import Faker
import pandas as pd

fake = Faker('da_DK')


name = fake.name()
address = fake.address()
total_consumption = fake.random_int(min=0, max=1000)
hour1 = fake.random_int(min=0, max=1000)
hour2= fake.random_int(min=0, max=1000)
hour3= fake.random_int(min=0, max=1000)
hour4 = fake.random_int(min=0, max=1000)
hour5= fake.random_int(min=0, max=1000)
hour6= fake.random_int(min=0, max=1000)
hour7 = fake.random_int(min=0, max=1000)
hour8= fake.random_int(min=0, max=1000)
hour9= fake.random_int(min=0, max=1000)
hour10 = fake.random_int(min=0, max=1000)
hour13= fake.random_int(min=0, max=1000)
hour12= fake.random_int(min=0, max=1000)



hour14 = fake.random_int(min=0, max=1000)
hour15= fake.random_int(min=0, max=1000)
hour15= fake.random_int(min=0, max=1000)
hour16 = fake.random_int(min=0, max=1000)
hour17= fake.random_int(min=0, max=1000)
hour18= fake.random_int(min=0, max=1000)
hour19 = fake.random_int(min=0, max=1000)
hour20= fake.random_int(min=0, max=1000)
hour21= fake.random_int(min=0, max=1000)
hour22 = fake.random_int(min=0, max=1000)
hour23= fake.random_int(min=0, max=1000)
hour24= fake.random_int(min=0, max=1000)
sqm2 = fake.random_int(min=0, max=1000)
from_date = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None)
profiles = [fake.profile() for _ in range(10)]
pd.DataFrame(profiles).head()   