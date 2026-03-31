class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        freq = list(counts.values())

        max_f = max(freq)
        max_f_count = freq.count(max_f)

        formula = (max_f - 1) * (n + 1) + max_f_count
        return max(formula, len(tasks))

            