from gpiozero import *
import _thread
from time import *
from flask import Flask
from flask_cors import CORS
import math

# switch1 = LED("GPIO2")
# switch2 = LED("GPIO3")
# switch3 = LED("GPIO4")
# switch4 = LED("GPIO5")
# switch5 = LED("GPIO6")
# switch6 = LED("GPIO7")
# switch7 = LED("GPIO8")
# switch8 = LED("GPIO9")

cnt = 0
switch = []

stars_switch = LED("GPIO2")
rainbow_switch = LED("GPIO3")
rainbow_ctl = PWMLED("GPIO14")
rainbow_sig = False
projection_switch = LED("GPIO8")
projection_power = LED("GPIO23")
projection_color = LED("GPIO24")
projection_rotate = LED("GPIO25")
photo_switch = LED("GPIO9")
heart_switch = LED("GPIO7")
love_switch = LED("GPIO6")
iloveu_switch = LED("GPIO5")
ball_switch = LED("GPIO4")

touchBtn = Button("GPIO17")

index = 1


def openSkyLed():
    sleep(0.1)

    projection_color.on()
    projection_power.on()
    projection_rotate.on()

    sleep(0.1)

    projection_power.off()
    sleep(0.1)
    projection_power.on()

    sleep(0.1)

    projection_color.off()
    sleep(0.1)
    projection_color.on()

    sleep(0.1)

    projection_color.off()
    sleep(0.1)
    projection_color.on()

    sleep(0.1)

    projection_color.off()
    sleep(0.1)
    projection_color.on()

    sleep(0.1)

    projection_rotate.off()
    sleep(0.1)
    projection_rotate.on()


def closeSkyLed():
    sleep(0.1)

    projection_color.on()
    projection_power.on()
    projection_rotate.on()

    sleep(0.1)
    projection_power.on()

    sleep(0.1)
    projection_power.off()
    sleep(0.1)
    projection_power.on()


def rainbowPWM():
    global rainbow_sig
    print("11111")
    print(rainbow_sig)
    while rainbow_sig:
        value = 1.0
        while rainbow_sig and (value > 0.01):
            sleep(0.01)
            # rainbow_ctl.value = math.sin(value)
            rainbow_ctl.value = value
            value -= 0.01
        sleep(1)
        while rainbow_sig and (value < 1):
            sleep(0.01)
            # rainbow_ctl.value = math.sin(value)
            rainbow_ctl.value = value
            value += 0.01
        sleep(1)


def check_button():
    global index
    while True:
        if touchBtn.is_pressed:
            # if index >= cnt:
            #     index = 1
            # else:
            #     index += 1
            while touchBtn.is_pressed:
                pass
        else:
            pass


def switch_led():
    global index
    # switch[0].on()
    # switch[1].on()
    #
    # switch[3].on()
    # switch[4].on()
    # switch[5].on()
    while True:
        if index == 0:
            sleep(1)
            continue
        switch[index - 1].on()
        sleep(1)
        switch[index - 1].off()
        sleep(1)
        print(index - 1)


# 创建两个线程
# try:
#
#     _thread.start_new_thread(check_button, ())
#     _thread.start_new_thread(switch_led, ())
# except:
#     print("Error: 无法启动线程")

# while 1:
#     pass

closeSkyLed()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# 关闭所有
@app.route('/closeall')
def closeall():
    global rainbow_sig
    projection_switch.off()
    stars_switch.off()
    sleep(0.5)
    rainbow_sig = False
    rainbow_switch.off()
    sleep(0.5)
    heart_switch.off()
    sleep(0.5)
    love_switch.off()
    sleep(0.5)
    iloveu_switch.off()
    sleep(0.5)
    ball_switch.off()
    sleep(0.5)
    photo_switch.off()
    sleep(0.5)
    closeSkyLed()

    return "ok", 200


# 打开所有
@app.route('/openall')
def openall():
    global rainbow_sig
    projection_switch.on()
    stars_switch.on()
    sleep(0.5)
    rainbow_sig = True
    rainbow_switch.on()
    _thread.start_new_thread(rainbowPWM, ())
    sleep(0.5)
    heart_switch.on()
    sleep(0.5)
    love_switch.on()
    sleep(0.5)
    iloveu_switch.on()
    sleep(0.5)
    ball_switch.on()
    sleep(0.5)
    photo_switch.on()
    sleep(0.5)
    openSkyLed()

    return "ok", 200


# 星星灯开关
@app.route('/switch/stars/<int:status>')
def stars(status=2):
    if status == 2:
        status = stars_switch.value ^ 1
        print(stars_switch.value)
        print(stars_switch.value ^ 1)
    if status == 0:
        stars_switch.off()
        return "0", 200
    else:
        stars_switch.on()
        return "1", 200


# 彩虹灯开关
@app.route('/switch/rainbow/<int:status>')
def rainbow(status=2):
    global rainbow_sig
    if status == 2:
        status = rainbow_switch.value ^ 1
    if status == 0:
        rainbow_sig = False
        rainbow_switch.off()
        return "0", 200
    else:
        rainbow_sig = True
        rainbow_switch.on()
        _thread.start_new_thread(rainbowPWM, ())
        return "1", 200


# 心形灯开关
@app.route('/switch/heart/<int:status>')
def heart(status=2):
    if status == 2:
        status = heart_switch.value ^ 1
    if status == 0:
        heart_switch.off()
        return "0", 200
    else:
        heart_switch.on()
        return "1", 200


# love灯开关
@app.route('/switch/love/<int:status>')
def love(status=2):
    if status == 2:
        status = love_switch.value ^ 1
    if status == 0:
        love_switch.off()
        return "0", 200
    else:
        love_switch.on()
        return "1", 200


# iloveu灯开关
@app.route('/switch/iloveu/<int:status>')
def iloveu(status=2):
    if status == 2:
        status = iloveu_switch.value ^ 1
    if status == 0:
        iloveu_switch.off()
        return "0", 200
    else:
        iloveu_switch.on()
        return "1", 200


# 棉球灯开关
@app.route('/switch/ball/<int:status>')
def ball(status=2):
    if status == 2:
        status = ball_switch.value ^ 1
    if status == 0:
        ball_switch.off()
        return "0", 200
    else:
        ball_switch.on()
        return "1", 200


# 投影灯开关
@app.route('/switch/projection/<int:status>')
def projection(status=2):
    if status == 2:
        status = projection_switch.value ^ 1

    if status == 0:
        projection_switch.off()
        closeSkyLed()
        return "0", 200
    else:
        projection_switch.on()
        openSkyLed()
        return "1", 200


# 照片灯开关
@app.route('/switch/photo/<int:status>')
def photo(status=2):
    if status == 2:
        status = photo_switch.value ^ 1
    if status == 0:
        photo_switch.off()
        return "0", 200
    else:
        photo_switch.on()
        return "1", 200
