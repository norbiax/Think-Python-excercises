class Time:
    """Represents time of day
    Attributes: hour, minute, second
    """


def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def time_to_int(t):
    minutes = t.hour * 60 + t.minute
    seconds = minutes * 60 + t.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def mul_time(t, num):
    total = time_to_int(t) * num
    time = int_to_time(total)
    return time


def avg_time_per_kilometer(t, d):
    """Calculates the average time per kilometer

    :param t: race time
    :param d: distance in km
    :return: time/kilometer
    """

    avg_time = mul_time(t, (1 / d))
    return print('Avg time per 1km: %.2d:%.2d:%.2d' % (avg_time.hour, avg_time.minute, avg_time.second))


def main():
    time = Time()
    time.hour = 4
    time.minute = 0
    time.second = 0
    d = 8

    avg_time_per_kilometer(time, d)


if __name__ == '__main__':
    main()
