from sorting import random_numbers


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, score):
        seeking = []
        for i in range(self.count()):
            if self.scores[i] == score:
                seeking.append(i)
        return seeking

    def get_sorted(self):
        scores_copy = list(self.scores)
        n = len(scores_copy)
        for i in range(n):
            for j in range(0, n - i - 1):
                if scores_copy[j] > scores_copy[j + 1]:
                    scores_copy[j], scores_copy[j + 1] = scores_copy[j + 1], scores_copy[j]
        return scores_copy

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / self.count()

    def best(self):
        if not self.scores:
            return None
        return self.get_sorted()[-1]

    def worst(self):
        if not self.scores:
            return None
        return self.get_sorted()[0]

    def pass_rate(self):
        if not self.scores:
            return 0.0
        passed = 0
        for score in self.scores:
            if score >= 50:
                passed += 1
        return passed / self.count()

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"

    def find_sorted(self, score):
        if self._sorted_scores is None:
            print("sorting...")
            self._sorted_scores = self.get_sorted()

        sscores = self._sorted_scores
        low = 0
        high = len(sscores) - 1

        while low <= high:
            mid = (low + high) // 2
            if sscores[mid] == score:
                return mid
            elif sscores[mid] < score:
                low = mid + 1
            else:
                high = mid - 1

        return None


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(f"Počet studentů: {results.count()}\n")

    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points – {results.get_grade(i)}")

    print(f"\nIndexy studentů se 100 body: {results.find(100)}")
    print(f"Seřazené výsledky: {results.get_sorted()}\n")

    print("--- Zkouška bonusových metod (5.7) ---")
    print(results)
    print(f"Nejlepší skóre: {results.best()}")
    print(f"Nejhorší skóre: {results.worst()}")
    print(f"Úspěšnost (pass rate): {results.pass_rate():.2f}\n")

    print("--- Zkouška cachování (5.8) ---")
    print(f"Hledám 91: {results.find_sorted(91)}")
    print(f"Hledám 50: {results.find_sorted(50)}")
    print(f"Hledám 77: {results.find_sorted(77)}\n")

    print("--- Test na náhodných datech ---")
    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results)
    print(f"Seřazené výsledky:\n{random_results.get_sorted()}")


if __name__ == "__main__":
    main()