from faker import Faker
import pandas as pd

fake = Faker('da_DK')


name = fake.name()
address = fake.address()
#generate random float between 0 and 1
randomfloat = fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=0.5, max_value=1.4)
#generate random float between 0.5 and 1.4
print(randomfloat)