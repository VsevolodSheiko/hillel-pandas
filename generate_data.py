from random import random

from factory import Factory
import pandas as pd
import factory


class StudentFactory(Factory):
    class Meta:
        model = dict

    first_name = factory.Faker("first_name")
    last_name = factory.Faker('last_name')
    gender = factory.Faker('random_element', elements=('M', 'F'))
    email = factory.Faker('email')
    mark_1 = factory.Faker('random_int', min=0, max=100)
    mark_2 = factory.Faker('random_int', min=0, max=100)
    mark_3 = factory.Faker('random_int', min=0, max=100)
    attendance = factory.Faker('random_int', min=0, max=100)
    height = factory.Faker('random_int', min=100, max=200)
    weight = factory.Faker('random_int', min=30, max=100)
    city = factory.Faker('random_element', elements=('Lviv', 'Kyiv', 'Kharkiv', 'Dnipro', 'Odesa'))


num_rows = 100

students = StudentFactory.create_batch(num_rows)

for student in students:
    if random() < 0.1:
        student['first_name'] = None
    if random() < 0.1:
        student['mark_3'] = None
    if random() < 0.1:
        student['city'] = None


df = pd.DataFrame(students)

# df.to_json('students_records.json', orient='records', indent=4)
# df.to_clipboard()
df.to_xml('students_records.xml')

print(df)