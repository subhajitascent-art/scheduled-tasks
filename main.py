import smtplib
import random
import datetime as dt
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

emails_sub='Inspirational Quote of '



dateob=dt.datetime.now()
day_of_week=dateob.weekday()
# print(day_of_week)
days_of_week={
    1:'Monday',
    2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'
}

quotes=[]
with open(file='./quotes.txt') as f1:
    quotes=f1.readlines()
emails_sub += days_of_week[day_of_week+1]+'!'
quote_of_day=random.choice(quotes)
with smtplib.SMTP("smtp.gmail.com", port=587) as con:
    con.starttls()
    con.login(user=MY_EMAIL,password=MY_PASSWORD)
    con.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f'Subject: {emails_sub}\n\n {quote_of_day}')





