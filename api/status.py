
OK      = 0
ERROR   = 1

class Status:
    STAT_STR = ["OK", "ERROR"]

    def __init__(self, status, msg):
        if 0 < status < len(self.STAT_STR):
            self.status = status
        else:
            raise ValueError("Status codenot within range: %s" % status
        self.msg = msg

    def __str__(self):
        return "<Status: %s - %s>" % (self.STAT_STR[self.status], self.msg)
