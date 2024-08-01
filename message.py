from twilio.rest import Client
import compare
import time
import smtplib
import getpass

comp = compare
num = 0
currTime = time.time()
while True:
    updates = comp.compare_csv()

    content = ''

    for update in updates:
        if not update[2]:
            num = update[1]
            if num > 1:
                content += update[0] + ' has ' + str(num) + ' new chapters!' + '\n' + str(update[3]) + '\n'
            else:
                content += update[0] + ' has 1 new chapter!' + '\n' + str(update[3]) + '\n'
        else:
            content += 'A new Manhua ' + update[0] + ' has just released!' + '\n' + str(update[3]) + '\n'

    if len(content) > 0:
        email = 'Subject: {}\n\n{}'.format('Manhua Update number' + str(num), content)
        num += 1
        s = smtplib.SMTP('smtp.outlook.com', 587)
        status_code, response = s.ehlo()
        print(f"[*] Echoing the server:  {status_code} {response}")
        status_code, response = s.starttls()
        print(f"[*] Echoing the server:  {status_code} {response}")
        s.login('testerpythoncode@outlook.com', 'thisis**sbfls')
        s.sendmail('testerpythoncode@outlook.com', 'connorebauer@gmail.com', email)
        s.quit()
    time.sleep(3 * 60)
