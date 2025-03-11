import imaplib
import email
from email.message import Message
import datetime
import time
import loggerutility as logger
from flask import Flask,request
import json

class Email_Draft:
    def draft_email(self, email_config, email_details, response_content):
        try:
            with imaplib.IMAP4_SSL(host=email_config['host'], port=imaplib.IMAP4_SSL_PORT) as imap_ssl:
                imap_ssl.login(email_config['email'], email_config['password'])
                
                message = Message()
                message["From"] = email_config['email']
                message["To"] = email_details['sender']
                message["CC"] = email_details['cc']
                
                subject = email_details['subject']
                if not subject.startswith("Re:"):
                    subject = f"Re: {subject}"
                message["Subject"] = subject
                
                mail_details = f'{datetime.datetime.now().strftime("On %a, %b %d, %Y at %I:%M %p")} {email_details["sender"]} wrote:'
                message.set_payload(f"{response_content}\n\n{mail_details}\n\n{email_details['body']}")
                
                utf8_message = str(message).encode("utf-8")
                # print(f"utf8_message:: {utf8_message}")
                imap_ssl.append("[Gmail]/Drafts", '', imaplib.Time2Internaldate(time.time()), utf8_message)
                
                return True, utf8_message.decode("utf-8")
                
        except Exception as e:
            print(f"Error creating draft: {str(e)}")

    def draft_email_response(self, email_details):
        try:
            print("Creating draft email with the following details:")
            print(f"From: {email_details.get('from')}")
            print(f"To: {email_details.get('to')}")
            print(f"CC: {email_details.get('cc')}")
            print(f"Subject: {email_details.get('subject')}")
            print(f"Body: {email_details.get('body')}")

            return "Success", {
                "from": email_details['from'],
                "to": email_details['to'],
                "cc": email_details.get('cc', ""),
                "subject": email_details['subject'],
                "body": email_details['body']
            }

        except Exception as e:
            print(f"Error creating draft: {str(e)}")
            return "Failed", None

    def draft_mail(self, data):
        try:

            if "reciever_email_addr" in data and data["reciever_email_addr"] != None:
                reciever_email_addr = data["reciever_email_addr"]
                print(f"\nInside reciever_email_addr value:::\t{reciever_email_addr} \t{type(reciever_email_addr)}","0")

            if "receiver_email_pwd" in data and data["receiver_email_pwd"] != None:
                receiver_email_pwd = data["receiver_email_pwd"]
                print(f"\nInside receiver_email_pwd value:::\t{receiver_email_pwd} \t{type(receiver_email_pwd)}","0")

            if "host_name" in data and data["host_name"] != None:
                host_name = data["host_name"]
                print(f"\nInside host_name value:::\t{host_name} \t{type(host_name)}","0")
            
            if "sender_email_addr" in data and data["sender_email_addr"] != None:
                sender_email_addr = data["sender_email_addr"]
                print(f"\nInside sender_email_addr value:::\t{sender_email_addr} \t{type(sender_email_addr)}","0")

            if "cc_email_addr" in data and data["cc_email_addr"] != None:
                cc_email_addr = data["cc_email_addr"]
                print(f"\nInside cc_email_addr value:::\t{cc_email_addr} \t{type(cc_email_addr)}","0")

            if "subject" in data and data["subject"] != None:
                subject = data["subject"]
                print(f"\nInside subject value:::\t{subject} \t{type(subject)}","0")

            if "email_body" in data and data["email_body"] != None:
                email_body = data["email_body"]
                print(f"\nInside email_body value:::\t{email_body} \t{type(email_body)}","0")

            if "signature" in data and data["signature"] != None:
                signature = data["signature"]
                print(f"\nInside signature value:::\t{signature} \t{type(signature)}","0")
            

            email_config = {
                "email": data["reciever_email_addr"],
                "password": data["receiver_email_pwd"],
                "host": data["host_name"]
            }
            print(f"data::{data}")
            email_details = {
                "from": data["sender_email_addr"],
                "to":data["reciever_email_addr"],
                "cc": cc_email_addr,
                "subject": data["subject"],
                "body": data["email_body"],
                "signature": data["signature"]
            }

            success, draft_message = self.draft_email_response(email_details)
            
            if success == "Success":
                print(f"draft_message  {draft_message}")
                return draft_message

        except Exception as e:
            print(f"Error in Draft_Save: {str(e)}")
