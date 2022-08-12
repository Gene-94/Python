salary = [{'Name':'Alice', 'Job':'Data Scientist', 'Salary':122000},
          {'Name':'Bob', 'Job':'Engineer', 'Salary':77000},
          {'Name':'Carl', 'Job':'Manager', 'Salary':119000}]

with open("test.csv", "w") as file:
    file.write(','.join(salary[0].keys()))
    file.write("\n")
    for _dict in salary:
        file.write(','.join(str(val) for val in _dict.values()))
        file.write("\n")