#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.




from datetime import datetime
import pandas
import random
import smtplib

my_email = "saibuhasan22@gmail.com"
password = "trmg aupu wdbw wysh"  


today = datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/32_Send_Email_smtplib_&_Manage_Dates_datetime/Day-32_Send_Email_smtplib_&_Manage_Dates_datetime/00 Staged Learning with Code/007 Solution & Walkthrough for the Automated Birthday Wisher/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/32_Send_Email_smtplib_&_Manage_Dates_datetime/Day-32_Send_Email_smtplib_&_Manage_Dates_datetime/00 Staged Learning with Code/007 Solution & Walkthrough for the Automated Birthday Wisher/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birth Day!\n\n{contents}"
        )