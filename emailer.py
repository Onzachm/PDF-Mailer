# Built by Chanzo Muema after a LOT of time was wasted sending an email.
import subprocess
import os

# Add the directory containing powershell.exe to the PATH
os.environ["PATH"] += os.pathsep + r"C:\Windows\System32\WindowsPowerShell\v1.0"
# Install Chocolatey
subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"])

# Install Poppler
subprocess.run(["choco", "install", "poppler"])


import csv
import smtplib
import tkinter as tk
from tkinter import filedialog
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import base64
from pdf2image import convert_from_path
from io import BytesIO

# function to convert a PDF to a JPEG image
def convert_pdf_to_jpg(pdf_file_path):
    pages = convert_from_path(pdf_file_path, dpi=200)
    buffer = BytesIO()
    pages[0].save(buffer, 'jpeg', quality=80)
    return buffer.getvalue()


# function to send the email
def send_email(sender_email, receiver_email, subject, image_data, index, total):
    # create a message object instance
    msg = MIMEMultipart()

    # create an HTML message body that includes the image inline
    image_data_base64 = base64.b64encode(image_data).decode('ascii')
    html = f'<html><body><img src="data:image/jpeg;base64,{image_data_base64}"></body></html>'
    msg.attach(MIMEText(html, 'html'))

    # setup the email message header
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # setup the SMTP server
    smtp_server = 'smtp.mr.corp'

    # create an SMTP session
    session = smtplib.SMTP(smtp_server)

    # send the message
    session.sendmail(sender_email, receiver_email, msg.as_string())

    # close the SMTP session
    session.quit()

    # update the GUI with the email address and counter
    success_label.config(text=f'Sent email {index+1} of {total}: {receiver_email}')

    print(f'Email {index+1} of {total} sent successfully to {receiver_email}')


# function to handle the button click event
def handle_button_click():
    # get the values from the input fields
    sender_email = sender_email_field.get()
    csv_file_path = csv_file_path_field.get()
    pdf_file_path = pdf_file_path_field.get()
    subject = subject_field.get()

    # read the receiver email addresses from the CSV file
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the header row
        rows = list(reader)
        total = len(rows)
        for i, row in enumerate(rows):
            receiver_email = row[0]

            # convert the PDF to a JPEG image
            image_data = convert_pdf_to_jpg(pdf_file_path)

            # send the email
            send_email(sender_email, receiver_email, subject, image_data, i, total)

    # show a success message
    success_label.config(text=f'{total} emails sent successfully')


# function to handle the browse button click event for the CSV file
def handle_csv_file_browse_button_click():
    csv_file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    csv_file_path_field.delete(0, tk.END)
    csv_file_path_field.insert(0, csv_file_path)

# function to handle the browse button click event for the PDF file
def handle_pdf_file_browse_button_click():
    pdf_file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    pdf_file_path_field.delete(0, tk.END)
    pdf_file_path_field.insert(0, pdf_file_path)

# create the GUI window
root = tk.Tk()
root.title('PDF to Email')

# create the input fields and labels
sender_email_label = tk.Label(root, text='Sender Email:')
sender_email_field = tk.Entry(root)
csv_file_path_label = tk.Label(root, text='CSV File Path:')
csv_file_path_field = tk.Entry(root)
csv_file_browse_button = tk.Button(root, text='Browse...', command=handle_csv_file_browse_button_click)
pdf_file_path_label = tk.Label(root, text='PDF File Path:')
pdf_file_path_field = tk.Entry(root)
pdf_file_browse_button = tk.Button(root, text='Browse...', command=handle_pdf_file_browse_button_click)
subject_label = tk.Label(root, text='Subject:')
subject_field = tk.Entry(root)

# create the button and success label
send_button = tk.Button(root, text='Send Emails', command=handle_button_click)
success_label = tk.Label(root)

# layout the GUI components using the grid layout manager
sender_email_label.grid(row=0, column=0, sticky='E')
sender_email_field.grid(row=0, column=1)
csv_file_path_label.grid(row=1, column=0, sticky='E')
csv_file_path_field.grid(row=1, column=1)
csv_file_browse_button.grid(row=1, column=2)
pdf_file_path_label.grid(row=2, column=0, sticky='E')
pdf_file_path_field.grid(row=2, column=1)
pdf_file_browse_button.grid(row=2, column=2)
subject_label.grid(row=3, column=0, sticky='E')
subject_field.grid(row=3, column=1)
send_button.grid(row=4, column=1)
success_label.grid(row=5, column=1)

# start the GUI event loop
root.mainloop()