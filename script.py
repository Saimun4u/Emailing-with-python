import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

# Port number for the smtp protocol is 587

# print(type(conn))

# Connecting to the server

print(conn.ehlo())

# Ensuring that any password sent is encrypted

print(conn.starttls())

print(conn.login('saimun4u@gmail.com', 'xmtp_su8'))

#Password is imaginary in this case.

conn.sendmail('saimun4u@gmail.com', 'saimun4u@gmail.com', 'Subject: So long...\n\nDear Saimun\n, \nHow is it going?\n\n - From Sophie')

conn.quit()