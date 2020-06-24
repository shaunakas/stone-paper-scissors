import random
print('-----Welcome to the Stone Paper Scissors-----')

you=0
cpu=0
rounds=0

def value():
		move=input('\nCan you beat CPU???\n1.Stone\n2.Paper\n3.Scissors\nSelect your move:')
		if move in ['1','2','3']:
			print('\nRound:',rounds+1)
			print(move)
		else:
			print('Enter a number')
			move=value()
			print(move)
		return move


for i in range(3):  #while loop should be used with a flag

	items=['stone','paper','scissors']
	move=value()


	ranvar=random.choice(items)
	#try:
	#move=int(move)	
	if move in ['1','2','3']:
		if move =='1':
			move='Stone'
			#print(move)
		elif move =='2':
			move='Paper'
			#print(move)
		elif move =='3':
			move='Scissors'
			#print(move)
		print(' YOU                       CPU\n',move,'------>> X <<------',ranvar.title())



		if (move=='Stone' and ranvar=='stone'):
			print('\nIts a Tie!Nobody gets point\n')
		elif (move=='Stone' and ranvar=='paper'):
			print('\n+++++>>>  Paper wrap Stone  <<<+++++\n---CPU gets a point---\n')
			cpu=cpu+1
		elif (move=='Stone' and ranvar=='scissors'):
			print('+++++>>>  Stone smashes Scissors  <<<\n---YOU get a point---\n')
			you=you+1
		elif (move=='Paper' and ranvar=='stone'):
			print('\n+++++>>>  Paper wrap Stone  <<<+++++\n---YOU gets a point---\n')
			you=you+1
		elif (move=='Paper' and ranvar=='paper'):
			print('\nIts a Tie!Nobody gets point\n')
		elif (move=='Paper' and ranvar=='scissors'):
			print('\n+++++>>>  Scissors cuts Paper  <<<+++++\n---CPU gets a point---\n')
			cpu=cpu+1
		elif (move=='Scissors' and ranvar=='stone'):
			print('+++++>>>  Stone smashes Scissors  <<<\n---CPU gets a point---\n')
			cpu=cpu+1
		elif (move=='Scissors' and ranvar=='paper'):
			print('\n+++++>>>  Scissors cuts Paper  <<<+++++\n---YOU get a point---\n')
			you=you+1
		elif (move=='Scissors' and ranvar=='scissors'):
			print('\nIts a Tie!Nobody gets point\n')	
		print('\n YOU  CPU\n',you,'  ',cpu)						
	else:
		print('Only Enter between 1,2 or 3')
		continue
	#except:
		#print('Print numbers only')
		##rounds=rounds-1
		#continue			

if you<cpu:
	print('\n\n----->>>   CPU WINS   <<<-----\n\n')
elif you>cpu:
	print('\n\n----->>>   YOU WIN   <<<-----\n\n')
elif you==cpu:
	print('\n\n----->>>   IT IS A TIE   <<<-----\n\n')				

