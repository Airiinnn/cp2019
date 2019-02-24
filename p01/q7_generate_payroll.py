name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
rate = float(input("Enter hourly pay rate: "))
cpfrate = float(input("Enter CPF contribution rate(%): "))

gross = hours * rate
cpf = cpfrate / 100 * gross
net = gross - cpf

payroll = """Payroll statement for {0:}
Number of hours worked in week: {1:}
Hourly pay rate: ${2:.2f}
Gross pay = ${3:.2f}
CPF contribution at {4:}% = ${5:.2f}
Net pay = ${6:.2f} """.format(name, hours, rate, gross, cpfrate, cpf, net)
              
print(payroll)
