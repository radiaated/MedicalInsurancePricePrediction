
def tree0(tree_dict):
	if tree_dict['Outlook'] == 'sunny':
		if tree_dict['Humidity'] == 'high':
			return -2.8000000000000007
		elif tree_dict['Humidity'] == 'normal':
			return 1.5555555555555556
	elif tree_dict['Outlook'] == 'overcast':
		return 1.5555555555555556
	elif tree_dict['Outlook'] == 'rain':
		if tree_dict['Windy'] == 'weak':
			return 1.5555555555555554
		elif tree_dict['Windy'] == 'strong':
			return -2.8000000000000003

def tree1(tree_dict):
	return 0.300007649461104

def tree2(tree_dict):
	return 0.03800156005579871

def tree3(tree_dict):
	return 0.0038811187549828477

def tree4(tree_dict):
	return 0.00038889688633996145
