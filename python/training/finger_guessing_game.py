import random



def game():
	shapelist =  ["stock","scissor","paper"]
	print("Please show you shape:")
	shape = input("User shape:")
	if shape == "stock" or shape == "scissor" or shape == "paper":
		i = random.randint(0,2)
		if (shape == "stock") and (shapelist[i] == "scissor"):
			print("User win!")
		if (shape == "scissor") and (shapelist[i] == "stock"):
			print("Computer win!")
		if (shape == "scissor") and (shapelist[i] == "paper"):
			print("User win!")
		if (shape == "paper") and (shapelist[i] == "scissor"):
			print("Computer win!")
		if (shape == "paper") and (shapelist[i] == "stock"):
			print("User win!")
		if (shape == "stock") and (shapelist[i] == "paper"):
			print("Computer win!")
		if(shape == shapelist[i]):
			print("TIE!")
		print("Computer shape:",shapelist[i])
	else:
		exit("Please input the right shape!")

game()