def find_rank(user_rank):
	find_12, find_21 = user_rank.find('12'), user_rank.find('21')
	
	if find_12 == -1 or find_21 == -1:
		return 'No'
	
	if find_12 < find_21:
		user_rank=user_rank.replace('12','',1)
		if '21' in user_rank:
			return 'Yes'

	else:
		user_rank=user_rank.replace('21','',1)
		if '12' in user_rank:
			return 'Yes'
		
	return 'No'

def main():
	user_rank = input()
	print(find_rank(user_rank))

if __name__=='__main__':
	main()
