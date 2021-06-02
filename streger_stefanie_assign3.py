#Calculate the total weekly pay
hourly_wage = float(input('Enter the wage: $'))
total_weekly_hours = int(input('Enter the regular hours:'))
regular_weekly_pay = float(hourly_wage * total_weekly_hours)

#Calculate the overtime weekly pay
overtime_hours = float(input('Enter the overtime hours:'))
overtime_wage = float(hourly_wage * 1.5)
overtime_weekly_pay = float(overtime_hours * overtime_wage)

#Calculate the weekly pay with or without overtime
print("The total weekly pay is $", format(regular_weekly_pay + overtime_weekly_pay, '.2f'))