#!/usr/bin/env python3

import os, datetime, reports, emails

current_date = datetime.datetime.now().strftime("%B %d, %Y")

def main():
    """Process the fruit descriptions into a string for creating the report"""
    content = ""
    datapath = "supplier-data/descriptions/"
    files = os.listdir(datapath)
    for file in files:
        if file[-4:] == ".txt":
            with open(datapath + file, "r") as doc:
                lines = doc.readlines()
                fruit_name = lines[0]
                fruit_weight = lines[1]
                content += "name: "+fruit_name+"<br/>"+"weight: "+fruit_weight+"<br/><br/>"

    """Generate the report based on the processed data"""
    attach_path = "/tmp/processed.pdf"
    title = "Process Updated on "+current_date
    reports.generate(attach_path,title,content)

    """Send an email of that report"""
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, attach_path)
    emails.send_email(message)

if __name__ == "__main__":
    main()