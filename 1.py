basicPay = int(input())
totalSalary = basicPay + (basicPay*(10/100)) + (basicPay*(5/100))
paybleSalary = totalSalary - (totalSalary*(2/100))

print("Payble Salary is :", paybleSalary)