from signal import signal, SIGINT

bar = chr(0x2501)
barsize = 40

class Progress:
    def __init__(self):
        self.trackedProgress = -1
        self.oldsignal = signal(SIGINT, self.clean)

    def update(self, percent):
        progressed = int(percent * barsize) # Tells us if the progress has changed
        if progressed != self.trackedProgress: # Decide if the progress needs to be updated
            self.trackedProgress = progressed
            total = int(percent * 100)
            unprogressed = barsize - progressed
            print("\r\033[?25l\033[92m" + bar * progressed + "\033[0m" + bar * unprogressed + f" {total}", end="")
        if progressed == barsize:
            print("\033[?25h")
            signal(SIGINT, self.oldsignal)

    def clean(self, sig, frame):
        print("\033[?25h")
        self.oldsignal(sig, frame)
