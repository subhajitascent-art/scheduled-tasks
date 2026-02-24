import smtplib
import random
import datetime as dt

USER_NAME='subhajit.ascent@gmail.com'
TO_ADDR='paromita.ascent@gmail.com'
PASSWORD='rzwkgpjpszyzxixv'
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
        con.login(user=USER_NAME,password=PASSWORD)
        con.sendmail(from_addr=USER_NAME,to_addrs=TO_ADDR,msg=f'Subject: {emails_sub}\n\n {quote_of_day}')

