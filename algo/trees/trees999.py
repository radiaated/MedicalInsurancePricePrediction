
def tree1(tree_dict):
	if tree_dict['Outlook'] == 'Rainy':
		if tree_dict['Temp'] == 'Hot':
			return 27.5
		elif tree_dict['Temp'] == 'Mild':
			return 41.5
		elif tree_dict['Temp'] == 'Cool':
			return 38.0
	elif tree_dict['Outlook'] == 'Overcast':
		if tree_dict['Temp'] == 'Hot':
			return 45.0
		elif tree_dict['Temp'] == 'Mild':
			return 52.0
		elif tree_dict['Temp'] == 'Cool':
			return 43.0
	elif tree_dict['Outlook'] == 'Sunny':
		if tree_dict['Windy'] == False:
			return 45.5
		elif tree_dict['Windy'] == True:
			return 35.0
