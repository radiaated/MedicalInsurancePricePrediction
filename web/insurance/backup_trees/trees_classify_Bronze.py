
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
