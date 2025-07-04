# 005: Challenge1 - Send motivational quotes on via Email on mondays.


import smtplib
import datetime as dt
import random

my_email = "saibuhasan22@gmail.com"
password = "trmg aupu wdbw wysh"               # App Password key: 

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/32_Send_Email_smtplib_&_Manage_Dates_datetime/Day-32_Send_Email_smtplib_&_Manage_Dates_datetime/00 Staged Code/005 Challenge1 - Send Motivational quotes on Mondays via Email/quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation \n\n{quote}"
            # msg=f"Subject:Monday Motivation Quote\n\n{quote}"
        )