import smtplib

conn = smtplib.SMTP('smtp-mail.outlook.com', 587)

# Port number for the smtp protocol is 587

# print(type(conn))

# Connecting to the server

print(conn.ehlo())

# Ensuring that any password sent is encrypted

print(conn.starttls())

print(conn.login('super11@outlook.com', 'ru_8sek'))

#Password is imaginary in this case. The email distribution works with the original password

conn.sendmail('super11@outlook.com', 'super11@outlook.com', 'Subject: So long...\n\nDear Saimun\n, \nHow is it going?\n\n - From Sophie')

conn.quit()