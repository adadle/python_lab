#coding=utf-8
"""
format year,month,day
"""

months=['January'
        ,'Feabruary'
        ,'March'
        ,'April'
        ,'May'
        ,'July'
        ,'June'
        ,'August'
        ,'September'
        ,'October'
        ,'November'
        ,'December'
    ]
year_input = raw_input("year: ")
month_input = raw_input("month: ")
day_input = raw_input("day: ")

month_int = int(month_input)
day_int = int(day_input)

endings = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']   

month_name = months[month_int-1]
ordinal = day_input + endings[day_int-1]

print month_name +' '+ ordinal +'. '+ year_input

