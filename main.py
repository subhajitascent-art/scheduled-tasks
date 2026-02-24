import smtplib
import random
import datetime as dt
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
TO_ADDR='paromita.ascent@gmail.com'
emails_sub='Inspirational Quote of '



dateob=dt.datetime.now()
day_of_week=dateob.weekday()
# print(day_of_week)
days_of_week={
    1:'Monday',
    2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'
}
if day_of_week==1:
    quotes=[]
    with open(file='./DailyQuotes/quotes.txt') as f1:
     quotes=f1.readlines()
    emails_sub += days_of_week[2]+'!'
    quote_of_day=random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as con:
        con.starttls()
        con.login(user=MY_EMAIL,password=MY_PASSWORD)
        con.sendmail(from_addr=USER_NAME,to_addrs=TO_ADDR,msg=f'Subject: {emails_sub}\n\n {quote_of_day}')


