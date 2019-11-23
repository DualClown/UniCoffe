import os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
# import RPi.GPIO as GPIO
import time
# import serial


# arduino = serial.Serial('/dev/ttyUSB0', 9600)


def save_picture(form_picture):
    random_hex = str(os.urandom(3))
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = '''To reset your password, visit the following link:
{}

If you did not make this request then simply ignore this email and no changes will be made.
'''.format(url_for('users.reset_token', token=token, _external=True))

    mail.send(msg)


def serve_coffee():
    # GPIO.setwarnings(False)
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(5, GPIO.OUT) # LED1
    # GPIO.setup(6, GPIO.OUT) # LED2
    # GPIO.setup(13, GPIO.OUT)
    # GPIO.setup(19, GPIO.OUT)
    # time.sleep(7)  # WAIT TIME FOT THE SERIAL MESSAGE DELAY
    # arduino.write('0'.encode()) # STAR THE SERVO RUTINE
    # time.sleep(2)  # WAIT TIME FOT THE SERIAL MESSAGE DELAY
    # GPIO.output(19, GPIO.HIGH)  # HEATER ON
    # GPIO.output(5, GPIO.HIGH)
    # GPIO.output(6, GPIO.HIGH)
    time.sleep(10)
    # GPIO.output(13, GPIO.HIGH)  # PUMP ON
    # GPIO.output(5, GPIO.LOW)
    # GPIO.output(6, GPIO.LOW)
    # GPIO.output(19, GPIO.LOW)  # HEATER OFF
    # time.sleep(3.7)
    # GPIO.output(13, GPIO.LOW)  # PUMP OFF
