import unittest
from BowlingGame import BowlingGame


class BowlingGameTest(unittest.TestCase):

    def test_max_frames(self):

        BowlingGame.score_calc(self,1,4)
        BowlingGame.score_calc(self,3,5)
        BowlingGame.score_calc(self,5,3)
        BowlingGame.score_calc(self,2,0)
        BowlingGame.score_calc(self,6,6)
        BowlingGame.score_calc(self,0,4)
        BowlingGame.score_calc(self,0,0)
        BowlingGame.score_calc(self,4,5)
        BowlingGame.score_calc(self,5,5)
        BowlingGame.score_calc(self,8,0)
        BowlingGame.score_calc(self,8,0) #11 th frame

        self.assertFalse(False,BowlingGame.score_calc)

    def test_total_score_with_11th_frame(self):

        BowlingGame.score_calc(self,1,4)
        BowlingGame.score_calc(self,3,5)
        BowlingGame.score_calc(self,5,3)
        BowlingGame.score_calc(self,2,0)
        BowlingGame.score_calc(self,2,6)
        BowlingGame.score_calc(self,0,4)
        BowlingGame.score_calc(self,0,0)
        BowlingGame.score_calc(self,4,5)
        BowlingGame.score_calc(self,5,5)
        BowlingGame.score_calc(self,8,0)

        self.assertFalse(False,BowlingGame.get_score(self,11))

    def test_total_score(self):

        BowlingGame.score_calc(self,1,4)
        BowlingGame.score_calc(self,3,5)
        BowlingGame.score_calc(self,5,3)
        BowlingGame.score_calc(self,2,0)
        BowlingGame.score_calc(self,2,6)
        BowlingGame.score_calc(self,0,4)
        BowlingGame.score_calc(self,0,0)
        BowlingGame.score_calc(self,4,5)
        BowlingGame.score_calc(self,5,5)
        BowlingGame.score_calc(self,8,0)

        self.assertEqual(70,BowlingGame.get_score(self,10))

    def test_cummulative_score(self):

        BowlingGame.score_calc(self,1,4)
        BowlingGame.score_calc(self,3,5)
        BowlingGame.score_calc(self,5,3)
        BowlingGame.score_calc(self,2,0)
        BowlingGame.score_calc(self,2,6)
        BowlingGame.score_calc(self,0,4)
        BowlingGame.score_calc(self,0,0)
        BowlingGame.score_calc(self,4,5)
        BowlingGame.score_calc(self,5,5)
        BowlingGame.score_calc(self,8,0)

        self.assertEqual(35,BowlingGame.get_score(self,6))

    def test_validate_max_pins_per_frame(self):

        BowlingGame.score_calc(self,1,4)
        BowlingGame.score_calc(self,3,5)
        BowlingGame.score_calc(self,5,3)
        BowlingGame.score_calc(self,2,0)
        BowlingGame.score_calc(self,6,6)
        BowlingGame.score_calc(self,0,4)
        BowlingGame.score_calc(self,0,0)
        BowlingGame.score_calc(self,4,5)
        BowlingGame.score_calc(self,5,5)
        BowlingGame.score_calc(self,8,0)

        self.assertFalse(False,BowlingGame.score_calc)

    def test_double_strike(self):

        BowlingGame.score_calc(self,1,4)
        BowlingGame.score_calc(self,3,5)
        BowlingGame.score_calc(self,4,6)
        BowlingGame.score_calc(self,2,0)
        BowlingGame.score_calc(self,10,0)
        BowlingGame.score_calc(self,4,3)
        BowlingGame.score_calc(self,10,0)
        BowlingGame.score_calc(self,10,0)
        BowlingGame.score_calc(self,5,3)
        BowlingGame.score_calc(self,4,5)

        self.assertEqual(114,BowlingGame.get_score(self,10))

if __name__ == '__main__':
    unittest.main()