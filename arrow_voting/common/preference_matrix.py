from typing import List, Dict

from collections import defaultdict


def get_preference_matrix(votes: List[Dict[str, int]]) -> Dict[str, Dict[str, int]]:
    # TODO: Test
    # TODO: Docstring
    matrix: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for vote in votes:
        for candidate_a, score_a in vote.items():
            for candidate_b, score_b in vote.items():
                if score_a > score_b:
                    matrix[candidate_a][candidate_b] += 1

    return matrix
