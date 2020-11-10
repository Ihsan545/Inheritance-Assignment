from datetime import datetime
from class_definitions.salaried_employee import SalariedEmployee
from class_definitions.employee import Employee
from class_definitions.hourly_employee import HourlyEmployee
"""Driver"""

name= Employee('Anwary','Ihsan') # employee object
salary_chang = SalariedEmployee('Anwary','Ihsan',datetime.today(),40000)
hourly_pay= HourlyEmployee('Anwary','Ihsan',datetime.today(),10)
hourly_pay.give_raise('12')
salary_chang.change_salary('45,000')
print(salary_chang.display3())
print(hourly_pay.display2())
del (salary_chang,hourly_pay)
