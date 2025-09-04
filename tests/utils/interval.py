class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        # Debug-friendly string
        return f"[{self.start}, {self.end}]"
