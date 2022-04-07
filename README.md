# powerball_pro
# Aurthor: yalem bakala

•	The Powerball game in this assignment works differently from the real one like Mega Millions to get more chances to get favorite results. 
•	The Powerball game includes two parts. 
o	Part one includes 5 numbers. These five numbers are white ball numbers, which are drawn randomly from 20 numbers from 1 to 20 inclusively - (1,2,3, 4, 5, … , 17,18,19, 20). 
o	Part two only has one number, the Powerball number, which is obtained randomly from 10 numbers (1,2,3,4, 5,6,7,8, 9,10). 
•	When your program/page is run or reloaded/refreshed, it would display today’s Powerball winning numbers, your lucky numbers, and display the result based on your lucky numbers against Today’s Powerball winning numbers. 

•	Correct White Balls and the Powerball: Jackpot $324,000,000
•	5 Correct White Balls, but no Powerball: $1,000,000
•	4 Correct White Balls and the Powerball: $10,000
•	4 Correct White Balls, but no Powerball: $100
•	3 Correct White Balls and the Powerball: $100
•	3 Correct White Balls, but no Powerball: $7
•	2 Correct White Balls and the Powerball: $7
•	1 Correct White Ball and the Powerball: $4
•	No White Balls, Just the Powerball: $4
•	All Other situations – display “try again!”

class Draw(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  check_win(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)