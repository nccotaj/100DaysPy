import datetime as dt
import smtplib, random
# now = dt.datetime.now()#output type is a string
# year = now.year 
# print(year) #output type is a int

# day_of_week = now.weekday()
# print(day_of_week) #0 = Mon, 1 = Tuesday, 3 = Wednesday, etc


# date_of_birth = dt.datetime(year=2002, month=4, day=27)
# print(date_of_birth)

my_email = "n8434109@gmail.com"
my_password = "Testemail1234!"

app_password = "gkyyoacmurxwodep"

receive_test = "nicktestctest@yahoo.com"

## -----Motivational Quote Sender---------##
with open("quotes.txt") as file:
    quotes_list = [line.strip() for line in file.readlines()]


todays_quote = random.choice(quotes_list)

day_of_week = dt.datetime.now().weekday()


if day_of_week == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)

        connection.sendmail(from_addr=my_email, to_addrs=receive_test, msg=f"Subject: Today's Quote \n\n{todays_quote}")