import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

# print(type(conn))

# Connecting to the server

print(conn.ehlo())

# Ensuring that any password sent is encrypted

print(conn.starttls())