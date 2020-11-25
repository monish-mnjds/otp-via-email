while True:
            def send_mail(subject,otp):
                try:    
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(cr.email1,cr.password)
                    OTP = 'Subject: {}\n\n{}'.format(subject,otp)
                    cr.email2 = input('\nEnter ur email id : ')   # e.g: receiver@gmail.com
                    server.sendmail('sender@gmail.com',cr.email2,OTP)
                    server.quit()
                    print("\nEmail has been sent...")
                except:
                    print('\nEmail failed to send....')
            subject = 'One-Time Password...'
            truth = secrets.SystemRandom()
            otp = str(truth.randrange(100000,999999))
            msg = 'Your One Time Password is : ' + otp
            send_mail(subject,msg)
            otpmail = input('\nEnter the 6 digit OTP : ')
            if otpmail == otp:
                print('Working Successfully.....')
            else:
                print('\nOTP may be wrong')
                toredo = input("\nTo Retry Press 'R' or E to exit: ")
                if toredo == 'r' or toredo == 'R':
                    continue
            break
