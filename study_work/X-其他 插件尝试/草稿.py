from faker import Faker
Fk = Faker(locale="zh_CN")
print(Fk.sentence())
print(Fk.paragraph())
print(Fk.text())