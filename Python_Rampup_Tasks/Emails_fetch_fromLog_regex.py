import re

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
with open('emailslogfile_practice_regex.txt', 'r') as file:
    text = file.read()

email_addresses = re.findall(pattern, text)
print("The number of emails in the text file: ",len(email_addresses))
for email in email_addresses:
    print(email)
