#bowling_frames: x=frame number, [y=scores, index 0 = Pins knocked down in Roll 1, index 1 = Pins knocked down in Roll 2, index 2 = Frame Total]

class BowlingGame:
    def define_variables(self):
        global frame_number
        global bowling_frames
        global frame_score_index
        global roll_number

        frame_number=0
        bowling_frames = [[0 for x in range(11)] for y in range(3)]
        frame_score_index=2
        roll_number=0

    def score_calculator(self,pins_knocked):
        global roll_number
        global frame_number

        if (frame_number <= 10):

            bowling_frames[roll_number][frame_number] = pins_knocked

            if (roll_number < 1):    

                roll_number +=1
                return True
           
            elif (roll_number == 1):
                
                BowlingGame.compute_bonuses(self)

                bowling_frames[frame_score_index][frame_number] = bowling_frames[frame_score_index][frame_number-1] + bowling_frames[roll_number-1][frame_number] + bowling_frames[roll_number][frame_number]
                
                frame_number += 1
                roll_number = 0 # Reset Roll number 

            else:
                return False

        else:
            return False

    
    def compute_bonuses(self):

        if (bowling_frames[roll_number-1][frame_number-1] == 10): #Strike in previous frame 

            BowlingGame.compute_double_strike_bonus(self)

            bowling_frames[frame_score_index][frame_number-1] = bowling_frames[frame_score_index][frame_number-1] +  bowling_frames[roll_number-1][frame_number] + bowling_frames[roll_number][frame_number]

        elif (bowling_frames[roll_number-1][frame_number-1] + bowling_frames[roll_number][frame_number-1] == 10): #Spare in previous frame     
            
            bowling_frames[frame_score_index][frame_number-1] =  bowling_frames[frame_score_index][frame_number-1] +  bowling_frames[roll_number-1][frame_number]

    
    def compute_double_strike_bonus(self):

        if (bowling_frames[roll_number-1][frame_number-2] == 10):

            bowling_frames[frame_score_index][frame_number-2] =  bowling_frames[frame_score_index][frame_number-2] + bowling_frames[roll_number-1][frame_number]
            bowling_frames[frame_score_index][frame_number-1] = bowling_frames[frame_score_index][frame_number-2] +  bowling_frames[roll_number-1][frame_number-1]

    
    def fetch_framescore(self,frame):
        if (frame <= 10):
            return bowling_frames[frame_score_index][frame - 1]
        else:
            return False