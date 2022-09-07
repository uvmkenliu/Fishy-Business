from flask import Flask, render_template, request
import json
#import mysql.connector
#import RPi.GPIO as GPIO
import time

app = Flask(__name__)


"""
GPIO.setmode(GPIO.BCM)

#horizontal motor setup
HORIZ_POWER = ?
HORIZ_GROUND = ?
HORIZ_ENA = 4
HORIZ_RIGHT = 14
HORIZ_LEFT = 15

GPIO.setup(HORIZ_RIGHT, GPIO.OUT)
GPIO.setup(HORIZ_LEFT, GPIO.OUT)
GPIO.setup(HORIZ_ENA, GPIO.OUT)

GPIO.output(HORIZ_RIGHT, GPIO.LOW)
GPIO.output(HORIZ_LEFT, GPIO.LOW)

horiz_PWM = GPIO.PWM(HORIZ_ENA, 100)
horiz_PWM.start(0)

#vertical motor setup
VERT_POWER = ?
VERT_GROUND = ?
VERT_ENA = 17
VERT_UP = 27
VERT_DOWN = 18

GPIO.setup(VERT_UP, GPIO.OUT)
GPIO.setup(VERT_DOWN, GPIO.OUT)
GPIO.setup(VERT_ENA, GPIO.OUT)

GPIO.output(VERT_UP, GPIO.LOW)
GPIO.output(VERT_DOWN, GPIO.LOW)

vert_PWM = GPIO.PWM(VERT_ENA, 100)
vert_PWM.start(0)

#string motor setup
STRING_POWER = ?
STRING_GROUND = ?
STRING_ENA = ?
STRING_UP = ?
STRING_DOWN = ?

GPIO.setup(STRING_UP, GPIO.OUT)
GPIO.setup(STRING_DOWN, GPIO.OUT)
GPIO.setup(STRING_ENA, GPIO.OUT)

GPIO.output(STRING_UP, GPIO.LOW)
GPIO.output(STRING_DOWN, GPIO.LOW)

string_PWM = GPIO.PWM(STRING_ENA, 100)
string_PWM.start(0)

DIR_FORWARD = 0
DIR_BACKWARD= 1

def motorStop():
    GPIO.output(HORIZ_RIGHT, GPIO.LOW)
    GPIO.output(HORIZ_LEFT, GPIO.LOW)
    GPIO.output(HORIZ_ENA, GPIO.LOW)
    GPIO.output(VERT_UP, GPIO.LOW)
    GPIO.output(VERT_DOWN, GPIO.LOW)
    GPIO.output(VERT_ENA, GPIO.LOW)
    GPIO.output(STRING_UP, GPIO.LOW)
    GPIO.output(STRING_DOWN, GPIO.LOW)
    GPIO.output(STRING_ENA, GPIO.LOW)

    GPIO.cleanup()

def motorHorizontal(direction):
    if direction == DIR_FORWARD:
        GPIO.output(HORIZ_RIGHT, GPIO.HIGH)
        GPIO.output(HORIZ_LEFT, GPIO.LOW)
        horiz_PWM.start(100)
        horiz_PWM.ChangeDutyCycle(speed)  Might not use this
    elif direction == DIR_BACKWARDS:
        GPIO.output(HORIZ_RIGHT, GPIO.LOW)
        GPIO.output(HORIZ_LEFT, GPIO.HIGH)
        horiz_PWM.start(0)
        horiz_PWM.ChangeDutyCycle(speed) might not use this

def motorVertical(direction):
    if direction == DIR_FORWARD:
        GPIO.output(VERT_UP, GPIO.HIGH)
        GPIO.output(VERT_DOWN, GPIO.LOW)
        vert_PWM.start(100)
        vert_PWM.ChangeDutyCycle(speed)  Might not use this
    elif direction == DIR_BACKWARDS:
        GPIO.output(VERT_UP, GPIO.LOW)
        GPIO.output(VERT_DOWN, GPIO.HIGH)
        vert_PWM.start(0)
        vert_PWM.ChangeDutyCycle(speed) might not use this
"""


#main route
#================================
#startup
@app.route("/", methods=["GET"])
def homeStartup():
    return render_template("index.html", title="index", name="Ty Allembert")
#Index
@app.route("/index.html", methods=["GET"])
def homeIndex():
    return render_template("index.html", title="index", name="Ty Allembert")
#Leaderboard
@app.route("/leaderboard.html", methods=["GET"])
def homeLeaderboard():
    """database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )
    cursor = database.cursor()

    # Your query to return records with ID 20 through 30 [inclusive]
    # from the test_data table
    query = "SELECT * FROM finalProject;"

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    database.close()"""
    return render_template("leaderboard.html", title="Leaderboard", name="Ty Allembert")
#How to play
@app.route("/howToPlay.html", methods=["GET"])
def homeHowTo():
    return render_template("howToPlay.html", title="How to Play", name="Ty Allembert")
#================================

#Motors
#================================
#stop motor
@app.route("/stop_motor", methods=["POST"])
def stop_motor():
    print("stopped")
    #make arm go up
    #motorStop()
    return "stopped"
#vertical arm up
@app.route("/vertical_up", methods=["POST"])
def vertical_up():
    print("up")
    #make arm go up
    #motorVertical(1)
    return "up"

#vertical arm down
@app.route("/vertical_down", methods=["POST"])
def vertical_down():
    print("down")
    #make arm go down
    #motorVertical(0)
    return "down"

#horizontal spin right
@app.route("/horizontal_right", methods=["POST"])
def horizontal_right():
    print("right")
    #make motor spin right
    #motorHorizontal(1);
    return "right"

#horizontal spin left
@app.route("/horizontal_left", methods=["POST"])
def horizontal_left():
    print("left")
    #make motor spin left
    #motorHorizontal(0)
    return "left"

#========String Motor==========
#String up
@app.route("/string_up", methods=["POST"])
def string_up():
    print("String up")
    #make motor spin left
    #string_PWM.ChangeDutyCycle(10)
    #GPIO.cleanup()
    return "String up"
    
#String down
@app.route("/string_down", methods=["POST"])
def string_down():
    print("String down")
    #make motor spin left
    #hstring_PWM.ChangeDutyCycle(10)
    #GPIO.cleanup()
    return "String down"