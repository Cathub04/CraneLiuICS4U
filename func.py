import threading


def add_zeroes(num, count):
    res = ""
    if len(num) < len(count):
        n = len(count) - len(num)
        for i in range(n):
            res += "0"
        return res + num
    else:
        return num


def set_timer(time_status, time):
    s_timer = threading.Timer(1, set_timer)
    s_timer.start()
    if time_status is not True:
        s_timer.cancel()
        return
    time += 1
    ms = add_zeroes(str(time % 60), "00")
    sec = add_zeroes(str(int(time / 60) % 60), "00")
    minute = add_zeroes(str(int(time / 60 / 60)), "00")

# END
