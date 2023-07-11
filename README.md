# PDF to Email Converter

This Python script allows you to convert PDF files to JPEG images and send them as email attachments to multiple recipients. The script utilizes several libraries, including `subprocess`, `os`, `csv`, `smtplib`, `tkinter`, `email.mime`, `base64`, and `pdf2image`.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- The required libraries (`subprocess`, `os`, `csv`, `smtplib`, `tkinter`, `email.mime`, `base64`, and `pdf2image`)

## Usage

1. Update the script with your desired email server details and SMTP server.
2. Run the script using Python 3.x.
3. Enter the necessary information in the GUI window:
   - Sender Email: Enter the email address from which you want to send the emails.
   - CSV File Path: Browse and select the CSV file containing the recipient email addresses.
   - PDF File Path: Browse and select the PDF file to convert and send as an attachment.
   - Subject: Enter the subject for the email.
4. Click the "Send Emails" button to start the process.
5. The script will convert the PDF to JPEG images, attach them to individual emails, and send them to the recipients listed in the CSV file.
6. The progress will be displayed in the GUI window, showing the number of emails sent.
7. Once all emails are sent, a success message will be displayed.

Note: Make sure to adjust the SMTP server details and other settings based on your email provider's requirements.

## Limitations

- The script assumes that the first column of the CSV file contains the recipient email addresses.
- The script converts only the first page of the PDF file to a JPEG image.
- The script sends emails one by one and may take some time for a large number of recipients.
- The script provides a basic GUI interface, but further enhancements can be made based on specific requirements.

