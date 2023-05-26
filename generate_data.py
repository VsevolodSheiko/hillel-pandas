from random import random

from factory import Factory
import pandas as pd
import factory


class EmployeeFactory(Factory):
    class Meta:
        model = dict

    first_name = factory.Faker("first_name")
    age = factory.Faker('random_int', min=18, max=65)
    job_title = factory.Faker('job')
    salary = factory.Faker('random_int', min=1000, max=3300)
    work_experience = factory.Faker('random_int', min=1, max=20)

num_rows = 50

employees = EmployeeFactory.create_batch(num_rows)

for employee in employees:
    if random() < 0.1:
        employee['salary'] = int("-" + str(employee['salary']))
    if random() < 0.1:
        employee['job_title'] = None


df = pd.DataFrame(employees)
df.to_csv("employees_csv.csv")

print(df)