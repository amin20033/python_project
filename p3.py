# Q3 Use list comprehensions to display employee salary data, such as - every employee is getting a 10% salary hike. 
# You must display: Employee Name Current Salary Updated Salary (after 10%)

class Employee:
    def __init__(self):
        self.employees=[]
    def add_employee(self):
        name=input("Enter Employee Name: ")
        salary=int(input("Enter Employee Salary: "))
        self.employees.append({"name":name,"salary":salary})
        return print("Employee Details added Successfully!!")
    def show_employee_details(self):
        updated_data = [(emp["name"], emp["salary"], int(emp["salary"] * 1.10))for emp in self.employees]
        count=1
        for x in updated_data:
            print(count,")","\n","Name:",x[0],"\n","Old Salary:",x[1],"\n","New Salary:",x[2])
            count+=1
         
employee=Employee()   
while True:
    print("Enter 1 to add new employee details")
    print("Enter 2 to see employee details")
    print("Enter others keys to exit")
    choice=int(input("Enter Your Choice: "))
    if choice == 1:
        employee.add_employee()
    elif choice==2:
        employee.show_employee_details()
    else :
        print("Exiting...")
        break
    
    


