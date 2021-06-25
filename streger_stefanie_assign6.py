days = int(input("How many days did you collect gems? ")) #get number of days
total_gems = 0
for number in range(1, days + 1):
    daily_gems = int(input("Enter the number of gems collected on day {} ".format(number)))
    total_gems += daily_gems

print('Total gems collected:', total_gems)
print('Average gems collected per day:',
      format(total_gems / days, ',.2f'),
      sep='')