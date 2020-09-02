import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Email:

    def sendEmail(self, data):

        mail_content = '''Hola,
        Aviso de creacion de contrato.
        Cliente : {}
        Muchas gracias
        '''.format(data['NOMBRE_ARRENDATARIO'])
        # The mail addresses and password
        sender_address = 'lafamiliaesgrande@gmail.com'
        sender_pass = 'Edwin1102'
        receiver_address = 'chefsantiagoperez@gmail.com'
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Contrato de arrendamiento'

        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'api/business/contrato_arrendamiento.pdf'

        try:
            with open(attach_file_name, 'rb') as fp: # Open the file as binary mode
                payload = MIMEBase('application', 'octate-stream')
                payload.set_payload(fp.read())
                encoders.encode_base64(payload) #encode the attachment
                # add payload header with filename
                payload.add_header('Content-Disposition', 'attachment', filename="contrato_arrendamiento.pdf")
            message.attach(payload)
            # Create SMTP session for sending the mail
            # session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            with smtplib.SMTP('smtp.gmail.com', 587) as s: #use gmail with port
                s.starttls() #enable security
                s.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                s.sendmail(sender_address, receiver_address, text)
                s.quit()
                print('Mail Sent')
        except:
            print("Error al enviar el email")
            raise