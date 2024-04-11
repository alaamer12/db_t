class Employee:
    def __init__(self, _first=None, _last=None, _salary=None):
        self.first = _first
        self.last = _last
        self.salary = _salary

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.salary)
