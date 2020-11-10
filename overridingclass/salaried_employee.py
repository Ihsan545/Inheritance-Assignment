from class_definitions.employee import Employee


class SalariedEmployee(Employee): # Employee is base class
    '''Employee Class '''
    """Student derived class of Person base class"""

    def __init__(self, _last_name, _first_name, start_date, salary=0.0):  # constructor
        super().__init__(start_date, salary)
        self._last_name = _last_name
        self._first_name = _first_name
        self.start_date = start_date
        self.salary = salary

    def change_salary(self, sarary):
        self.salary = sarary

    def display3(self):
        return f'{self._last_name + "," + self._first_name}\nStart Date :{self.start_date}\nSalart changed to ${self.salary}'
