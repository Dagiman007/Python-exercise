from PriorityQueue import PriorityQueue
class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score  # Less is more


def main():
    tiger = Golfer('Tiger Woods', 61)
    phil = Golfer('Phil Mickelson', 72)
    hal = Golfer('Hal sutton', 69)

    pq = PriorityQueue()
    for g in [tiger, phil, hal]:
        pq.insert(g)

    pq.printQueue()
    print()
    while not pq.empty():
        print(pq.remove())


main()
