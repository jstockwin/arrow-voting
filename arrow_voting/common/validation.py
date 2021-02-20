from typing import List, Dict

from .exceptions import InvalidVotesError


def validate_votes(votes: List[Dict[str, int]]):
    # TODO: Test
    if not all(vote.keys() == votes[0].keys() for vote in votes[1:]):
        raise InvalidVotesError("All votes must have the same candidates.")
