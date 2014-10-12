# Blog: guoj.org
# Github: github.com/guojing0
# Email: dev.guoj@gmail.com

import simplegui

total = 0
success = 0
current_time = 0

def format(t):
    m = t / 600
    s = t / 10 % 60
    f = t % 10
    return '%d:%02d.%d' % (m, s, f)

def start_btn():
    timer.start()

def stop_btn():
    global total, success, current_time
    if (timer.is_running()):
        total += 1
        if (current_time % 10 == 0):
            success += 1
    timer.stop()

def reset_btn():
    global total, success, current_time
    current_time = 0
    success = 0
    total = 0
    timer.stop()

def timer_handler():
    global current_time
    current_time += 1

def draw(canvas):
    canvas.draw_text(str(success) + '/' + str(total), [150, 20], 20, 'Red')
    canvas.draw_text(format(current_time), [50, 100], 40, 'White')

frame = simplegui.create_frame('Stopwatch', 200, 200)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
frame.add_button('Start', start_btn, 150)
frame.add_button('Stop', stop_btn, 150)
frame.add_button('Reset', reset_btn, 150)
frame.start()
