class RecentCounter:

    def __init__(self):
        self.request = []
        

    def ping(self, t: int) -> int:
        self.request.append(t)
        prev = t - 3000
        left_index = bisect_left(self.request,prev)
        return len(self.request) - left_index
