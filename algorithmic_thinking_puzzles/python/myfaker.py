# pip install faker
from faker import Faker
fk = Faker()
print(fk.locales)
print(fk.factories)

print(fk.name())
print(fk.address())
print(fk.email())
print(fk.text())
print(fk.country())
print(fk.url())
print(fk.latitude(), fk.longitude())

number = fk.unique.random_int(10,20)
print(number)
numbers = [fk.unique.random_int(min=1,max=10) for i in range(5)]
print(numbers)
# assert len(numbers) == 20
print(len(numbers))