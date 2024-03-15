
def tree0(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree1(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree2(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree3(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree4(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree5(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree6(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree7(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree8(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree9(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree10(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree11(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree12(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree13(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree14(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree15(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree16(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree17(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree18(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree19(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree20(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree21(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree22(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree23(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree24(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree25(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree26(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree27(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree28(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree29(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree30(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree31(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree32(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree33(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree34(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree35(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree36(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree37(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree38(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree39(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree40(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree41(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree42(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree43(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree44(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree45(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree46(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree47(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree48(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree49(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree50(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree51(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree52(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree53(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree54(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree55(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree56(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree57(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree58(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree59(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree60(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree61(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree62(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree63(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree64(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree65(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree66(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree67(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree68(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree69(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree70(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree71(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree72(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree73(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree74(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree75(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree76(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree77(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree78(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree79(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree80(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree81(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree82(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree83(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree84(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree85(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree86(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree87(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree88(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree89(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree90(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree91(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree92(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree93(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree94(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree95(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree96(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree97(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree98(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277

def tree99(tree_dict):
	if tree_dict['age'] == '56-64':
		return -2.1470705460342434
	elif tree_dict['age'] == '18-26':
		if tree_dict['smoker'] == 'yes':
			return -2.0643780252830832
		elif tree_dict['smoker'] == 'no':
			return 1.4659730902792725
	elif tree_dict['age'] == '26-41':
		if tree_dict['smoker'] == 'yes':
			return -2.0702071701884996
		elif tree_dict['smoker'] == 'no':
			return 1.457408035895379
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return -2.1116100474298003
		elif tree_dict['smoker'] == 'no':
			if tree_dict['children'] == 1.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.9676235272329503
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.5224264255735079
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.6923924233227127
				elif tree_dict['medical_history'] == 'No':
					return 0.4364800665781479
			elif tree_dict['children'] == 0.0:
				if tree_dict['medical_history'] == 'High Blood Pressure':
					return -0.7900540626418908
				elif tree_dict['medical_history'] == 'Diabetes':
					return -0.7404707680564008
				elif tree_dict['medical_history'] == 'Heart Disease':
					return -0.7469527946830258
				elif tree_dict['medical_history'] == 'No':
					return 0.18645903955113957
			elif tree_dict['children'] == 2.0:
				if tree_dict['sex'] == 'female':
					return -1.1988010327907646
				elif tree_dict['sex'] == 'male':
					return 0.0960121563889143
			elif tree_dict['children'] == 3.0:
				if tree_dict['bmi'] == '35 - 40':
					return -2.1470705460342776
				elif tree_dict['bmi'] == '25 - 30':
					return -1.4988678833716615
				elif tree_dict['bmi'] == '30 - 35':
					return -1.538152893230002
				elif tree_dict['bmi'] == '< 18.5':
					return 0
				elif tree_dict['bmi'] == '18.5 - 25':
					return -1.8791467788003962
				elif tree_dict['bmi'] == '40 - 54':
					return -1.1423564189072222
			elif tree_dict['children'] == 4.0:
				return -2.0174300135017544
			elif tree_dict['children'] == 5.0:
				return -2.147070546034277
