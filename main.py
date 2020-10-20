import time
import random
import datetime

import vk_api

token = "TOKEN"
id_to = 61 # id беседы, у тебя может быть другим

times_send = [datetime.time(hour=3, minute=0), datetime.time(hour=13, minute=5)] # примерное время отправки(в часовом поясе хоста)
max_delay = 2 # максимальная рандомная задержка


def min_time_sleep(arr_time):
    time_now = datetime.datetime.now()
    min_time = 10**25

    for time_send in arr_time:
        sleep_sec = (time_send.hour - time_now.hour) * 3600 + (time_send.minute - time_now.minute) * 60
        if sleep_sec <= 0:
            sleep_sec += 24 * 3600
        if sleep_sec < min_time:
            min_time = sleep_sec

    return min_time


def log(data):
    with open("logs", "a") as write_logs:
        write_logs.write("\n" + data)
    print(data)


if __name__ == "__main__":
    session = vk_api.VkApi(token=token)
    vk = session.get_api()

    log("bot running at %s\n" % datetime.datetime.now())

    while True:
        delay = random.randint(0, max_delay) * 60
        time_sleep = min_time_sleep(times_send) + delay

        log("next send view: %ss \nnow: %s\n" % (time_sleep, datetime.datetime.now()))

        time.sleep(time_sleep)

        temperature = 36 + (random.randint(3, 6) / 10)
        message = "ФАМИЛИЯ %.1f" % temperature

        vk.messages.send(chat_id=id_to, message=message, random_id=0)

        log("message ----> %s" % message)
