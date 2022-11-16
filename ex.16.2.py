def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    # print(time.hour, time.minute, time.second)
    return time


class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


start = Time()
start.hour = 9
start.minute = 45
start.second = 00

start.print_time()

end = start.increment(2)
end.print_time()

time_as_int = Time()
time_as_int.hour = 00
time_as_int.minute = 1
time_as_int.second = 00

print(time_as_int.time_to_int())