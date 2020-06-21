#importing all the important libraries
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import csv

#configuring sender mail and password
SenderEmail = "buddingentrepreneur2505@gmail.com"
password = input("Type your password and press enter: ")

message = MIMEMultipart("alternative")

#Specifying subject of the mail
message["Subject"] = "Bulk Automated Mails"

#Configuring the smtp server
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

    #logging into the mail
    server.login(SenderEmail, password)
    #Opening the csv file containing contact details
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)

        #Extracting name and email one at a time
        for name, email in reader:

            # content of the mail
            # giving a placeholder for the name using {name}
            html = """\
			<html>
                <body>
                    <font face="verdana"
                      color="coral"> 
                        <p><h3>hi {name},<br>
                            How are you ?</h3><br>
                            <h2>THIS IS AN AUTOMATED MAIL USING PYTHON<br><br>
                            YOU CAN ADD HTML FILES TOO </h2><br><br>
                            <h4>CONTACT ME IF YOU ARE FACING ANY PROBLEM WITH THIS</h4><br><br>
                            <h2><a href="https://www.linkedin.com/in/prakhar-srivastava-14b660193/">PRAKHAR SRIVASTAVA</a><h2> 
                            <h4>ALWAYS READY TO HELP</h4>
                        </p>
                    </font> 
                </body>
            </html>
			"""

            #Converting into html and appending it into the message
            part1 = MIMEText(html, "html")
            message.attach(part1)

            #Attachment for the mail
            #this file name can be supplied using contact.csv to send personalized attachments
            filename = "Doc.pdf"  # In same directory as script

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                part2 = MIMEBase("application", "octet-stream")
                part2.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part2)

            # Add header as key/value pair to attachment part
            part2.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # appending attachment to message
            message.attach(part2)

            #sending mails
            #converting message to string and filling placeholder using .format
            server.sendmail(
                SenderEmail,
                email,
                message.as_string().format(name=name)
            )
