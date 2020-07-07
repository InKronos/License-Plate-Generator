import smtplib
import zipfile
import tempfile
import ssl
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart    
import os

def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths       

def send_file_zipped(zipfile_name, recipient, sender='i15.piorkowski@gmail.com'):
  
    zf = tempfile.TemporaryFile(prefix='mail', suffix='.zip')
    file_paths = get_all_file_paths(zipfile_name)
    zip =  zipfile.ZipFile(zf,'w') 
    for file in file_paths: 
        zip.write(file)  
    zip.close()
    zf.seek(0)
    # Create the message
    themsg = MIMEMultipart()
    themsg['Subject'] = 'Hight Flyers'
    themsg['To'] = recipient
    themsg['From'] = sender
    themsg.preamble = 'Hight Flyers rejestracje w załączniku'
    msg = MIMEBase('application', 'zip')
    msg.set_payload(zf.read())
    encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', 
                   filename=zipfile_name + '.zip')
    themsg.attach(msg)
    themsg = themsg.as_string()

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    password = input("Type your password and press enter:")
    # send the message
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender, password)
        server.sendmail(sender, recipient, themsg)