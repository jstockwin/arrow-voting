from typing import Dict, List

from collections import defaultdict


def get_strongest_paths(
    preferences: Dict[str, Dict[str, int]], candidates: List[str]
) -> Dict[str, Dict[str, int]]:
    # TODO: Test
    # TODO: Docstring
    path_strengths: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for can_a in candidates:
        for can_b in candidates:
            if can_a == can_b:
                continue

            if preferences[can_a][can_b] > preferences[can_b][can_a]:
                path_strengths[can_a][can_b] = preferences[can_a][can_b]

    for can_a in candidates:
        for can_b in candidates:
            if can_a == can_b:
                continue

            for can_c in candidates:
                if (can_a != can_c) and (can_b != can_c):
                    path_strengths[can_b][can_c] = max(
                        path_strengths[can_b][can_c],
                        min(path_strengths[can_b][can_a], path_strengths[can_a][can_c]),
                    )

    return path_strengths
