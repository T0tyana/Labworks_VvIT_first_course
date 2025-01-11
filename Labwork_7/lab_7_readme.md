# Лабораторная работа №7
## Задание
> 1. Создайте класс Employee с общими атрибутами, такими как name (имя), id (идентификационный номер) и методами, например, get_info(), который возвращает базовую информацию о сотруднике.
> 2. Создайте класс Manager с дополнительными атрибутами, такими как department (отдел) и методами, например, manage_project(), символизирующим управление проектами.
> 3. Создайте класс Technician с уникальными атрибутами, такими как specialization (специализация), и методами, например, perform_maintenance(), означающим выполнение технического обслуживания.
> 4. Создайте класс TechManager, который наследует как Manager, так и Technician. Этот класс должен комбинировать управленческие способности и технические навыки, например, иметь методы для управления проектами и выполнения технического обслуживания.
> 5. Добавьте метод add_employee(), который позволяет TechManager добавлять сотрудников в список подчинённых.
> 6. Реализуйте метод get_team_info(), который выводит информацию о всех подчинённых сотрудниках.
> 7. Создайте объекты каждого класса и демонстрируйте их функциональность.
```python
class Employee:
    def __init__(self, name, employee_id, **kwargs):
        self.name = name
        self.employee_id = employee_id

    def get_info(self):
        return f'Имя сотрудника: {self.name}\nID сотрудника: {self.employee_id}'

class Manager(Employee):
    def __init__(self,name, employee_id, department=None, **kwargs):
        super().__init__(name, employee_id, department=department, **kwargs)
        self.department = department

    def manage_project(self):
        return f'{self.name} руководит проектом в отделе {self.department}'

    #def get_info(self):
        #return f'{super().get_info()}'

class Technician(Employee):
    def __init__(self, name, employee_id, specialization=None, **kwargs):
        super().__init__(name, employee_id, specialization=specialization, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'{self.name} выполняет техническое обслуживаение в области {self.specialization}'

    #def get_info(self):
        #return f'{super().get_info()}'

class TechManager(Manager, Technician):
    def __init__(self, name, employee_id, department=None, specialization=None):
      super().__init__(employee_id, name, department=department, specialization=specialization)
        self.team = []

    def project(self):
        return f'{Manager.manage_project(self)}'

    def maintenance(self):
        return f'{Technician.perform_maintenance(self)}'

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        info = 'Информация о команде:\n______________________\n'
        for employee in self.team:
            info += employee.get_info()+'\n'+'______________________'+'\n'
        return info

    def get_info(self):
        return f'Имя сотрудника: {self.name}\nID сотрудника: {self.employee_id}'

Miky = Employee('Miky', 213031)
print(Miky.get_info())
print()

Chloe = Manager('Chloe', 102310, 'Business')
print(Chloe.manage_project())
print(Chloe.get_info())
print()

Kriss = Technician('Kriss', 102311, 'Networking')
print(Kriss.perform_maintenance())
print(Kriss.get_info())
print()

Alec = TechManager('Alec', 101002, 'IT', 'System Administration')
print(Alec.manage_project())
print(Alec.perform_maintenance())
print(Alec.get_info())
print()

Alec.add_employee(Miky)
Alec.add_employee(Chloe)
Alec.add_employee(Kriss)

print(Alec.get_team_info())
```
