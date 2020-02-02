# Zachary Hayes - zjhayes@dmacc.edu

import unittest
import unittest.mock as mock
from format import average_scores


def test_average(self):
    with mock.patch('builtins.input', side_effect=[85, 90, 95]):
        assert average_scores.average() == 90


if __name__ == '__main__':
    unittest.main()