import time

class my_timer():
    def __init__(self):
        self.timer = None
        self.last_rezult = None

    def start_timer(self):
        if not self.timer:
            self.timer = time.time()
            return 1
        else:
            return 0

    def get_time(self):
        return int(time.time() - self.timer)

    def is_work(self):
        return True if self.timer != None else False

    def stop_timer(self):
        if self.timer:
            self.last_rezult = int(time.time() - self.timer)
            self.timer = None
            return self.last_rezult
        else:
            return 0

if __name__ == "__main__":
    timing = my_timer()
    print(timing.is_work())
    timing.start_timer()
    print(timing.is_work())
    timing.stop_timer()
    print(timing.is_work())
