import smtplib
import random
import pandas as pd
import datetime as dt
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
SMTP_SERVER='smtp.gmail.com'

# read the CSV file

d1= pd.read_csv('./birthdays.csv')

#get today's date
today=dt.datetime.now()
today_month=today.month
today_date=today.day

today_birthday_person= d1[(d1['month']==today_month) & (d1['day']==today_date)]

if not today_birthday_person.empty:
    for index,row in today_birthday_person.iterrows():
        name=row['name']
        selected_ltr=f'./letter_templates/letter_{random.randint(1,3)}.txt'
        with open (file=selected_ltr ,mode='r') as lt1:
            text = lt1.read()
            nw_text=text.replace('[NAME]',name)
            # send the email
            with smtplib.SMTP(SMTP_SERVER,port=587) as con:
                con.starttls()
                con.login(MY_EMAIL,MY_PASSWORD)
                con.sendmail(
                    from_addr=MY_EMAIL,to_addrs=row['email'],
                    msg=f'Subject: Happy Birthday !! \n\n{nw_text}'
                )


