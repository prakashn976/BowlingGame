bowling_frames = [[0 for x in range(10)] for y in range(3)]
Roll1_pins=0
Roll2_pins=0
frame_number=0

#x=frames, [y=scores 0=Roll 1 pin values, 1= Roll 2 pin values, 2= commulative score]

class BowlingGame:
     
    def score_calc(self,Roll1_pins, Roll2_pins):
        global frame_number

        if (frame_number <= 9):
            if (Roll1_pins+Roll2_pins <= 10):
                
                bowling_frames[0][frame_number] = Roll1_pins
                bowling_frames[1][frame_number] = Roll2_pins

                BowlingGame.Check_Bonus(self, Roll1_pins,Roll2_pins)

                bowling_frames[2][frame_number] = bowling_frames[2][frame_number-1] + Roll1_pins + Roll2_pins

                frame_number += 1

            else:
                return False

        else:
            return False

    def Check_Bonus(self,Roll1_pins,Roll2_pins):

        if (bowling_frames[0][frame_number-1] == 10): #Strike

                BowlingGame.check_double_strike(self,Roll1_pins,Roll2_pins)

                bowling_frames[2][frame_number-1] = bowling_frames[2][frame_number-1] +  Roll1_pins + Roll2_pins

        elif (bowling_frames[0][frame_number-1] + bowling_frames[1][frame_number-1] == 10): #Spare      
            
            bowling_frames[2][frame_number-1] =  bowling_frames[2][frame_number-1] +  Roll1_pins


    def check_double_strike(self,Roll1_pins,Roll2_pins):

        if (bowling_frames[0][frame_number-2] == 10):

            bowling_frames[2][frame_number-2] =  bowling_frames[2][frame_number-2] + Roll1_pins + Roll2_pins
            bowling_frames[2][frame_number-1] = bowling_frames[2][frame_number-2] +  bowling_frames[0][frame_number-1]

    def get_score(self,frame):
        if (frame <= 10):
            return bowling_frames[2][frame - 1]
        else:
            return False