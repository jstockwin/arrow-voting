from unittest import TestCase

from arrow_voting import schulze


class SchulzeTestCase(TestCase):
    def test_schulze(self):
        # Example from wikipedia
        votes = (
            [{"A": 5, "C": 4, "B": 3, "E": 2, "D": 1}] * 5
            + [{"A": 5, "D": 4, "E": 3, "C": 2, "B": 1}] * 5
            + [{"B": 5, "E": 4, "D": 3, "A": 2, "C": 1}] * 8
            + [{"C": 5, "A": 4, "B": 3, "E": 2, "D": 1}] * 3
            + [{"C": 5, "A": 4, "E": 3, "B": 2, "D": 1}] * 7
            + [{"C": 5, "B": 4, "A": 3, "D": 2, "E": 1}] * 2
            + [{"D": 5, "C": 4, "E": 3, "B": 2, "A": 1}] * 7
            + [{"E": 5, "B": 4, "A": 3, "D": 2, "C": 1}] * 8
        )

        out = schulze(votes)

        self.assertListEqual(out, [["E"], ["A"], ["C"], ["B"], ["D"]])
