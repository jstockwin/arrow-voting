from typing import List, Dict

from .common import get_preference_matrix, get_strongest_paths, validate_votes


def schulze(votes: List[Dict[str, int]]) -> List[List[str]]:
    # TODO: Test
    # TODO: Docstring
    validate_votes(votes)

    preferences = get_preference_matrix(votes)
    path_strengths = get_strongest_paths(preferences)
    candidates = list(path_strengths.keys())
    output = []

    while candidates:
        potential_winners = []
        for candidate in candidates:
            if all(
                path_strengths[candidate][other] >= path_strengths[other][candidate]
                for other in candidates
            ):
                potential_winners.append(candidate)
        output.append(potential_winners)
        for candidate in potential_winners:
            candidates.remove(candidate)

    return output
