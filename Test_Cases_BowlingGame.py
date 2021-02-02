import unittest
from BowlingGame import BowlingGame


class BowlingGameTest(unittest.TestCase):

    def test_maximumframesallowedas10(self):

        BowlingGame.define_variables(self)

        BowlingGame.score_calculator(self,1)
        BowlingGame.score_calculator(self,4)

        BowlingGame.score_calculator(self,3)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,5)
        BowlingGame.score_calculator(self,3)

        BowlingGame.score_calculator(self,2)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,2)
        BowlingGame.score_calculator(self,6)

        BowlingGame.score_calculator(self,0)
        BowlingGame.score_calculator(self,4)

        BowlingGame.score_calculator(self,0)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,4)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,5)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,8)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,8)

        self.assertFalse(False,BowlingGame.score_calculator)

    def test_totalscore_as10thframescore(self):
        BowlingGame.define_variables(self)

        BowlingGame.score_calculator(self,1)
        BowlingGame.score_calculator(self,4)

        BowlingGame.score_calculator(self,3)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,5)
        BowlingGame.score_calculator(self,3)

        BowlingGame.score_calculator(self,2)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,2)
        BowlingGame.score_calculator(self,6)

        BowlingGame.score_calculator(self,0)
        BowlingGame.score_calculator(self,4)

        BowlingGame.score_calculator(self,0)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,4)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,5)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,8)
        BowlingGame.score_calculator(self,0)

        self.assertEqual(70,BowlingGame.fetch_framescore(self,10))

    def test_framescore_withspare(self):

        BowlingGame.define_variables(self)

        BowlingGame.score_calculator(self,1)
        BowlingGame.score_calculator(self,4)

        BowlingGame.score_calculator(self,3)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,4)
        BowlingGame.score_calculator(self,6)

        BowlingGame.score_calculator(self,2)
        BowlingGame.score_calculator(self,0)

        self.assertEqual(27,BowlingGame.fetch_framescore(self,4))

        
    def test_framescore_withsinglestrike(self):

        BowlingGame.define_variables(self)

        BowlingGame.score_calculator(self,1)
        BowlingGame.score_calculator(self,4)

        BowlingGame.score_calculator(self,3)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,4)
        BowlingGame.score_calculator(self,6)

        BowlingGame.score_calculator(self,2)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,10)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,4)
        BowlingGame.score_calculator(self,3)

        self.assertEqual(51,BowlingGame.fetch_framescore(self,6))


    def test_totalscore_withdoublestrike(self):

        BowlingGame.define_variables(self)

        BowlingGame.score_calculator(self,1)
        BowlingGame.score_calculator(self,4)

        BowlingGame.score_calculator(self,3)
        BowlingGame.score_calculator(self,5)

        BowlingGame.score_calculator(self,4)
        BowlingGame.score_calculator(self,6)

        BowlingGame.score_calculator(self,2)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,10)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,4)
        BowlingGame.score_calculator(self,3)

        BowlingGame.score_calculator(self,10)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,10)
        BowlingGame.score_calculator(self,0)

        BowlingGame.score_calculator(self,5)
        BowlingGame.score_calculator(self,3)

        BowlingGame.score_calculator(self,4)
        BowlingGame.score_calculator(self,5)
    
        self.assertEqual(111,BowlingGame.fetch_framescore(self,10))

    def test_update_triple_strike_for_frame_total_score(self):

        BowlingGame.define_variables(self)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)
        
        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)
        
        self.assertEqual(30, BowlingGame.fetch_framescore(self,1))

    def test_update_spare_at_tenth_frame(self):

        BowlingGame.define_variables(self)

        BowlingGame.score_calculator(self, 1)
        BowlingGame.score_calculator(self, 4)

        BowlingGame.score_calculator(self, 3)
        BowlingGame.score_calculator(self, 5)

        BowlingGame.score_calculator(self, 4)
        BowlingGame.score_calculator(self, 6)

        BowlingGame.score_calculator(self, 2)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 4)
        BowlingGame.score_calculator(self, 3)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 5)
        BowlingGame.score_calculator(self, 3)

        BowlingGame.score_calculator(self, 7)
        BowlingGame.score_calculator(self, 3)

        BowlingGame.score_calculator(self, 10) 
        BowlingGame.score_calculator(self, 0)

        self.assertEqual(122, BowlingGame.fetch_framescore(self,10))

  
    def test_update_strike_at_tenth_frame(self):

        BowlingGame.define_variables(self)

        BowlingGame.score_calculator(self, 1)
        BowlingGame.score_calculator(self, 4)

        BowlingGame.score_calculator(self, 3)
        BowlingGame.score_calculator(self, 5)

        BowlingGame.score_calculator(self, 4)
        BowlingGame.score_calculator(self, 6)

        BowlingGame.score_calculator(self, 2)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 4)
        BowlingGame.score_calculator(self, 3)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 5)
        BowlingGame.score_calculator(self, 3)

        BowlingGame.score_calculator(self, 10)
        BowlingGame.score_calculator(self, 0)

        BowlingGame.score_calculator(self, 5)
        BowlingGame.score_calculator(self, 5)
        
        self.assertEqual(122, BowlingGame.fetch_framescore(self,10))

if __name__ == '__main__':
    unittest.main()