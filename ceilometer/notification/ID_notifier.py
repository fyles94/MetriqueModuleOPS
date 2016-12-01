import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("devstackpfe2016@gmail.com ", "pfe2016rtfjd")
 
msg = "Alerte metrique"
server.sendmail("devstackpfe2016@gmail.com ", "jorganahsva@gmail.com", msg)
server.quit()
