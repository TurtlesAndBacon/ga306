print('Lets paint us a wall!')
print('How wide is the wall? Enter width as a number ONLY.')
width = int(input())
print('How high is the wall? Enter height as a number ONLY.')
height = int(input())
print('How much does a gallon of paint cost? Enter cost as a rounded dollar ammount ONLY.')
cpg = int(input())
wallArea = int(width * height)
galNeeded = int(wallArea / 400)
moneyNeeded = int(cpg * galNeeded)
print('Alrighty, looks like we will need ' + str(galNeeded) + ' gallons of paint for this wall, which will cost $' + str(moneyNeeded) + '!')
