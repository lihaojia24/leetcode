from collections import defaultdict
from typing import List

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        score = defaultdict(int)
        for w in positive_feedback: score[w] = 3
        for w in negative_feedback: score[w] = -1
        students = [(-sum(score[w] for w in r.split()), i) for r, i in zip(report, student_id)]
        students.sort()
        return [i for _, i in students[:k]]