from openpyxl import Workbook
from faker import Faker
wb=Workbook()
ws=wb.active
fake=Faker()
for i in range(1,1000001):
    ws.cell(row=i,column=1).value=fake.name()
wb.save("1millionmen")