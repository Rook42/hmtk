import random
from multipledispatch import dispatch


class Character:

    # No arguments -- generate new character with all-random params at level 0.
    @dispatch()
    def __init__(self):
        self.seed = random.randint(0, 2 ** 32)
        self.scores = {}
        random.seed(self.seed)
        buildpoints = 40
        print(type(self.scores))
        self.scores = self.getScores()
        print(type(self.scores))
        # shopkeeper rule -- regenerate when no 13+ and more than 1 5- stat
        while all(stat < 13 for stat in self.scores.values()) or (
            2 <= len({k: v for k, v in self.scores.values() if v < 6})
        ):
            self.scores = self.getScores()
        buildpoints += 50  # no rearranged stats bonus

        # Get or generate ability scores

    def getScores(self):
            if self.scores:
                return self.scores
            
            scores = {}
            scoreNames = [
                "strength",
                "intelligence",
                "wisdom",
                "dexterity",
                "constitution",
                "looks",
            ]

            for score in scoreNames:
                scores[score] = (
                    random.randint(1, 6)
                    + random.randint(1, 6)
                    + random.randint(1, 6)
                    + round(random.random(), 2)
                )
            return scores
