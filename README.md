# BULK-PERSONALIZED-EMAIL-AUTOMATION
Recently, my father conducted an online webinar.
He needed my help with sending webinar links and personalized certificates to the attendees.
This motivated me to do this project .
This project will help you sending personalized mails at bulk , just follow the instructionsor reach out to me for any help.

## Dependencies
- ### Contacts.csv 
Contains the list of contacts whom you want to send mails 

- ### Doc.pdf 
Pdf attachment for the mail. You can also send personalized attachments to the recievers .Just append attachment names in the csv under a new heading filename, and do the following changes
```bash
for name, email, filename in reader: #line 30
  filename=filename #line 58
```

## Libraries
This project is build using following libraries 
 - smtplib
 - ssl
 - csv
 - email 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
pip install secure-smtplib
pip install mimelib
```
All other libraries are available by default in your ide.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## NEED HELP ?
Reach out to me at 

Linkedin : [Prakhar Srivastava](https://www.linkedin.com/in/prakhar-srivastava-14b660193/)

Mail : prakharsrivastava725@gmail.com
