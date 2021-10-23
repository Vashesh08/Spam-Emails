import smtplib
# from password import sender_password, sender_email
import email
import os
import imghdr
email_address = os.environ.get('GMAIL_EMAIL')
email_password = os.environ.get('GMAIL_PASSWORD')

message = email.message.EmailMessage()
message["From"] = email_address
message["Subject"] = "Email Subject : New Email From Vashesh J"
message.set_content("Hello, How are you Vashesh")
# message["Cc"] = ""
# message["Bcc"] = ""

with open("Calculator.png", 'rb') as image:
    image_data = image.read()
    # to add an image attachment
    # message.add_attachment(image_data, maintype='image', subtype=imghdr.what(None, image_data))
    # to add pdf attachment
    # message.add_attachment(image_data, maintype='application', subtype='pdf', filename="CrystalReportViewer1.pdf")
    # to add an image attachment
    message.add_attachment(image_data, maintype='application', subtype='png', filename="Calculator.png")

    with open("Book1.csv", 'r+') as book:
        source123 = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # source123 = smtplib.SMTP("smtp.gmail.com", 587)
        # source123.ehlo()
        # source123.starttls()
        # source123.ehlo()
        source123.login(email_address, email_password)
        # source123.login(sender_email, sender_password)

        for item in book:
            a, b = item.rstrip().split(',')
            message['To'] = b
            source123.send_message(message)
            print(" {} done".format(a))
            message.__delitem__('To')

        source123.quit()
