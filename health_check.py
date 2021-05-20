#!/usr/bin/env python3
import psutil, shutil
import emails
import os
import socket

def send_error_email(error):
    error_dict = {
        "high_cpu":"Error - CPU usage is over 80%",
        "low_disk":"Error - Available disk space is less than 20%",
        "low_mem":"Error - Available memory is less than 500MB",
        "no_res":"Error - localhost cannot be resolved to 127.0.0.1"
    }
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = error_dict[error]
    body = "Please check your system and resolve the issue as soon as possible."

    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

if psutil.cpu_percent(1) > 80:
    send_error_email("high_cpu")

local_disk_use = shutil.disk_usage("/")
if local_disk_use.used / local_disk_use.total > 80:
    send_error_email("low_disk")

if psutil.virtual_memory().available < 500* (1024 ** 2):
    send_error_email("low_mem")

if socket.gethostbyname("localhost") != "127.0.0.1":
    send_error_email("no_res")