
def tree0(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree1(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree2(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree3(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree4(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree5(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree6(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree7(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree8(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree9(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree10(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree11(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree12(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree13(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872

def tree14(tree_dict):
	if tree_dict['age'] == 3.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.8635526087127285
				elif tree_dict['medical_history'] == 3.0:
					return -1.2717724918101427
				elif tree_dict['medical_history'] == 0.0:
					return -2.1366818934369998
				elif tree_dict['medical_history'] == 2.0:
					return 0.582471874484627
			elif tree_dict['bmi'] == 3.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 0.0:
				return 0
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return -1.419717521035789
				elif tree_dict['medical_history'] == 3.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 0.0:
					return -1.2717724918101425
				elif tree_dict['medical_history'] == 2.0:
					return 1.6871280927027874
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return 1.528506618069108
	elif tree_dict['age'] == 0.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.4553327256153157
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['children'] == 1.0:
					return 1.5278026766136297
				elif tree_dict['children'] == 0.0:
					return 0.7757867126728054
				elif tree_dict['children'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['children'] == 3.0:
					return 1.6871280927027876
				elif tree_dict['children'] == 4.0:
					return 1.6871280927027872
				elif tree_dict['children'] == 5.0:
					return 0
			elif tree_dict['bmi'] == 3.0:
				return -2.3969882070474546
			elif tree_dict['bmi'] == 0.0:
				return 1.6871280927027876
			elif tree_dict['bmi'] == 1.0:
				return 1.6871280927027879
			elif tree_dict['bmi'] == 5.0:
				return -2.4553327256153143
		elif tree_dict['smoker'] == 1.0:
			return -2.0550297800884034
	elif tree_dict['age'] == 1.0:
		if tree_dict['smoker'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				return -2.455332725615316
			elif tree_dict['bmi'] == 2.0:
				return 1.6416065452487443
			elif tree_dict['bmi'] == 3.0:
				return -2.3530497424469683
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 1.2728820108709773
				elif tree_dict['region'] == 2.0:
					return -2.4553327256153143
				elif tree_dict['region'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['region'] == 1.0:
					return 0
			elif tree_dict['bmi'] == 1.0:
				return 1.6400546743128104
			elif tree_dict['bmi'] == 5.0:
				return -2.455332725615315
		elif tree_dict['smoker'] == 1.0:
			return -2.0533350116314506
	elif tree_dict['age'] == 2.0:
		if tree_dict['children'] == 1.0:
			if tree_dict['medical_history'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.26315718640594
				elif tree_dict['region'] == 2.0:
					return 1.0498264283461562
				elif tree_dict['region'] == 0.0:
					return 0.004253385261058478
				elif tree_dict['region'] == 1.0:
					return -0.23615728723061713
			elif tree_dict['medical_history'] == 3.0:
				if tree_dict['bmi'] == 4.0:
					return -1.0745124528426138
				elif tree_dict['bmi'] == 2.0:
					return -0.74961356513139
				elif tree_dict['bmi'] == 3.0:
					return -0.01859106778113692
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3105407455829599
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['medical_history'] == 0.0:
				if tree_dict['region'] == 3.0:
					return 0.42959534428479257
				elif tree_dict['region'] == 2.0:
					return -0.4432803281465223
				elif tree_dict['region'] == 0.0:
					return -0.11394182830508309
				elif tree_dict['region'] == 1.0:
					return -0.7293073846494393
			elif tree_dict['medical_history'] == 2.0:
				if tree_dict['bmi'] == 4.0:
					return -0.8343697967082314
				elif tree_dict['bmi'] == 2.0:
					return -0.6665428267961345
				elif tree_dict['bmi'] == 3.0:
					return -1.6716239221497287
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.3063078199300868
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
		elif tree_dict['children'] == 0.0:
			if tree_dict['bmi'] == 4.0:
				if tree_dict['smoker'] == 0.0:
					return -2.455332725615315
				elif tree_dict['smoker'] == 1.0:
					return -0.8234542214293963
			elif tree_dict['bmi'] == 2.0:
				if tree_dict['region'] == 3.0:
					return 0.40153680425923866
				elif tree_dict['region'] == 2.0:
					return 0.3584142453177361
				elif tree_dict['region'] == 0.0:
					return -0.12519851531138224
				elif tree_dict['region'] == 1.0:
					return -0.9489833371360051
			elif tree_dict['bmi'] == 3.0:
				if tree_dict['smoker'] == 0.0:
					return -1.7021580313756601
				elif tree_dict['smoker'] == 1.0:
					return 0.30630781993008716
			elif tree_dict['bmi'] == 0.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 3.0:
					return 0
				elif tree_dict['medical_history'] == 0.0:
					return 1.6871280927027874
				elif tree_dict['medical_history'] == 2.0:
					return -2.455332725615315
			elif tree_dict['bmi'] == 1.0:
				if tree_dict['region'] == 3.0:
					return 0.306307819930087
				elif tree_dict['region'] == 2.0:
					return -0.5221843437335335
				elif tree_dict['region'] == 0.0:
					return -1.1608137198909074
				elif tree_dict['region'] == 1.0:
					return 0.7311755961678409
			elif tree_dict['bmi'] == 5.0:
				if tree_dict['smoker'] == 0.0:
					return -2.4553327256153143
				elif tree_dict['smoker'] == 1.0:
					return 0.18077870422347764
		elif tree_dict['children'] == 2.0:
			if tree_dict['sex'] == 1.0:
				if tree_dict['bmi'] == 4.0:
					return 0.27262927669172843
				elif tree_dict['bmi'] == 2.0:
					return 0.19843123611971974
				elif tree_dict['bmi'] == 3.0:
					return 0.7162388384094829
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 1.3419230245096128
				elif tree_dict['bmi'] == 5.0:
					return -1.3046491649713972
			elif tree_dict['sex'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -1.2717724918101434
				elif tree_dict['bmi'] == 2.0:
					return -0.9489833371360054
				elif tree_dict['bmi'] == 3.0:
					return -1.3931632850209303
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.4844781777072097
				elif tree_dict['bmi'] == 5.0:
					return -1.9375251233255513
		elif tree_dict['children'] == 3.0:
			if tree_dict['smoker'] == 0.0:
				if tree_dict['bmi'] == 4.0:
					return -2.455332725615314
				elif tree_dict['bmi'] == 2.0:
					return 0.8150310783200291
				elif tree_dict['bmi'] == 3.0:
					return -1.937525123325552
				elif tree_dict['bmi'] == 0.0:
					return 0
				elif tree_dict['bmi'] == 1.0:
					return 0.582471874484627
				elif tree_dict['bmi'] == 5.0:
					return -2.4553327256153143
			elif tree_dict['smoker'] == 1.0:
				if tree_dict['medical_history'] == 1.0:
					return 1.1819499441274097
				elif tree_dict['medical_history'] == 3.0:
					return 1.0953479758002014
				elif tree_dict['medical_history'] == 0.0:
					return 1.3269141085012148
				elif tree_dict['medical_history'] == 2.0:
					return 0.47295854250610275
		elif tree_dict['children'] == 4.0:
			return 1.5535003243699457
		elif tree_dict['children'] == 5.0:
			return 1.6871280927027872
