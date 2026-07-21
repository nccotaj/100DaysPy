import smtplib

my_email = "n8434109@gmail.com"
my_password = "Testemail1234!"

app_password = "gkyyoacmurxwodep"

receive_test = "nicktestctest@yahoo.com"

#create connection object from SMTP class
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()  #Start transfport layer security, encrypts our email

# #login
# connection.login(user=my_email, password=app_password)

# #send email
# connection.sendmail(from_addr=my_email, to_addrs=receive_test, msg="Subject: Hello World \n\nBody of my email")
# connection.close()


#Better way to do it (dont have to use conneciton.close)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  #Start transfport layer security, encrypts our email

    #login
    connection.login(user=my_email, password=app_password)

    #send email
    connection.sendmail(from_addr=my_email, to_addrs=receive_test, msg="Subject: Hello World \n\nBody of my email")
    connection.close()