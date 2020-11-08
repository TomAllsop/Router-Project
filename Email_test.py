import smtplib
import datetime
import csv

def send_mail(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("ishlong144@gmail.com", "123abcLong")#username, password
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("ishlong144@gmail.com", "tallsop63@gmail.com", message)#my address, persons address, message
        server.sendmail("ishlong144@gmail.com", "tobyratkinson@gmail.com", message)#my address, persons address, message
        server.sendmail("ishlong144@gmail.com", "elj2001@hotmail.co.uk", message)#my address, persons address, message
        server.quit()
        print("Success, email has been sent")
    except:
        print("Email send: Fail")

today = datetime.datetime.now()
date = (today.strftime("%x")) + ("20")#change when the year changes
date = "13/11/2020"
print ("Today's date is ",date)

def csv_interpret():
    try:
        with open('Router.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Date"] == date:
                    week = "Week "+(row["Week"])
                    msg = (row["Shower"]+ " is cleaning the shower. "+row["Kitchen"]+" is cleaning the kitchen. "+row["Bathroom"]+" is cleaning the bathroom. "+row["Corridor"]+" is cleaning the corridor.\n\n\nKitchen includes; floor (mop and vacuum), sink, drying rack, counter tops, table, take bins out, clean bins, get rid of toaster crumbs, clean behind the sofa\nBathroom includes; bath tub, sink, toilet, floor (mop), mirror, window ledge, glass shower protector, shower head, shampoo bottle stand")
                    send_mail(week, msg)

    except:
        print("Not the day")


csv_interpret()

