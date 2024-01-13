
def tree0(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree1(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree2(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree3(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree4(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree5(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree6(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree7(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree8(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree9(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree10(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree11(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree12(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree13(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079

def tree14(tree_dict):
	if tree_dict['smoker'] == 0.0:
		if tree_dict['bmi'] == 4.0:
			return 1.057854905946224
		elif tree_dict['bmi'] == 2.0:
			if tree_dict['age'] == 3.0:
				if tree_dict['medical_history'] == 1.0:
					return -0.14329950078968043
				elif tree_dict['medical_history'] == 3.0:
					return -1.432038083016741
				elif tree_dict['medical_history'] == 0.0:
					return 0.4515029217766557
				elif tree_dict['medical_history'] == 2.0:
					return -5.470085640661534
			elif tree_dict['age'] == 0.0:
				return -7.046198113638069
			elif tree_dict['age'] == 1.0:
				return -7.875730994152036
			elif tree_dict['age'] == 2.0:
				if tree_dict['sex'] == 1.0:
					return -7.491851416467388
				elif tree_dict['sex'] == 0.0:
					return -4.35527437928788
		elif tree_dict['bmi'] == 3.0:
			return 0.6462438993889565
		elif tree_dict['bmi'] == 0.0:
			if tree_dict['region'] == 3.0:
				return -7.345073930882083
			elif tree_dict['region'] == 2.0:
				return 1.1454390814373805
			elif tree_dict['region'] == 0.0:
				return -7.875730994152046
			elif tree_dict['region'] == 1.0:
				return 0
		elif tree_dict['bmi'] == 1.0:
			return -7.225556574289769
		elif tree_dict['bmi'] == 5.0:
			return 1.0066518495052343
	elif tree_dict['smoker'] == 1.0:
		return -7.688709299130079
