# background
Rect(0, 0, 400, 400)

# Draw the rest of the night sky!
### (HINT: The rings of Saturn are drawn using a circle with a fill of None and
#          a border!)
### Place Your Code Here ###
Oval(250,250,120,120, fill=gradient('black', 'grey', start='left'))
Oval(150,275,100,50, fill=gradient('black', 'grey', start='left'), opacity=90)
Oval(125,300,100,50, fill=gradient('black', 'grey', start='left'), opacity=90)
Oval(200,300,100,50, fill=gradient('black', 'grey', start='right'), opacity=90)
Line(100,200,275,125, fill=gradient('black','white',start='right'), lineWidth=3)
Oval(150,100,50,50, fill=gradient('crimson','lightSalmon',start='bottom-left'), opacity=70)
Oval(50,50,60,60, fill=gradient('peru','wheat'))
Oval(50,50,70,70, fill=None,border='white', opacity=30)
