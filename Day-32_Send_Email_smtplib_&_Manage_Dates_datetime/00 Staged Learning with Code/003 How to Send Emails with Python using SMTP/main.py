# 003: How to Send Emails with Python using SMTP


import smtplib

my_email = "saibuhasan22@gmail.com"
password = "trmg aupu wdbw wysh"               # App Password key


with smtplib.SMTP("smtp.gmail.com", 587) as connection:         # port 587 is for TLS
    connection.starttls()               # TLS prevents encryption by attacker
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="soaebhasan04@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )  # msg must be in bytes, so we can use a string
    # connection.sendmail(from_addr=my_email, to_addrs="soaebhasan04    @yahoo.com", msg="Subject:Hello\n\nThis is the body of my email.".encode("utf-8"))