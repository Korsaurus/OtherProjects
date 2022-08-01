import smtplib
import random
import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()
time_of_day = now.time()

MY_EMAIL = "gregsemailspammer@gmail.com"
MY_PASSWORD = "roknczcknneicabc"

if day_of_week == 4:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        chosen_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="grkorsos@gmail.com",
            msg=f"Subject:Time For Motivation\n\n{chosen_quote}\nGet Motivated, son."
        )
