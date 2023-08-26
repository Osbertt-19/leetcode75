from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


obj = RecentCounter()
param_1 = obj.ping(1)
param_1 = obj.ping(2)
param_1 = obj.ping(3000)
param_1 = obj.ping(4000)
print(obj.queue)
