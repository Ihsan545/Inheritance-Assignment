from class_definitions.employee import Employee


class HourlyEmployee(Employee): # Employee is base class
    """" class HourlyEmployee """

    # Constructor
    def __init__(self, _last_name, _first_name, _start_date, hourly_pay=0.0, ): # constructor
        super().__init__(_start_date, hourly_pay)
        self._last_name = _last_name
        self.first_name = _first_name
        self._start_date = _start_date
        self.hourly_pay = hourly_pay

    def give_raise(self, _hourly_pay):
        self.hourly_pay = _hourly_pay

    def display2(self):
        return f'{self._last_name},{self._last_name}\nhourly pay changed to ${self.hourly_pay}\nStart Date {self._start_date}'
