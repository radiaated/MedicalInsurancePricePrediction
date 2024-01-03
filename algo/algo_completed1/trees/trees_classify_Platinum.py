
def tree0(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree1(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree2(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree3(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree4(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree5(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree6(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree7(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree8(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree9(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree10(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree11(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree12(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree13(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079

def tree14(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['bmi'] == '35 - 40':
			return 1.057854905946224
		elif tree_dict['bmi'] == '25 - 30':
			if tree_dict['age'] == '56-64':
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 'Diabetes':
					return -1.432038083016741
				elif tree_dict['medical_history'] == 'Heart Disease':
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 'No':
					return -5.470085640661534
			elif tree_dict['age'] == '18-26':
				return -7.046198113638069
			elif tree_dict['age'] == '26-41':
				return -7.875730994152036
			elif tree_dict['age'] == '41-56':
				if tree_dict['sex'] == 'female':
					return -7.491851416467388
				elif tree_dict['sex'] == 'male':
					return -4.35527437928788
		elif tree_dict['bmi'] == '30 - 35':
			return 0.6462438993889565
		elif tree_dict['bmi'] == '< 18.5':
			if tree_dict['region'] == 'northeast':
				return -7.345073930882083
			elif tree_dict['region'] == 'northwest':
				return 1.1454390814373805
			elif tree_dict['region'] == 'southwest':
				return -7.875730994152046
			elif tree_dict['region'] == 'southeast':
				return 0
		elif tree_dict['bmi'] == '18.5 - 25':
			return -7.225556574289769
		elif tree_dict['bmi'] == '40 - 54':
			return 1.0066518495052343
	elif tree_dict['smoker'] == 'no':
		return -7.688709299130079
