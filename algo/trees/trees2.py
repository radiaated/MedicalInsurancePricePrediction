
def tree_0(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['coverage_level'] == 'Premium':
			return 5283.409611138668
		elif tree_dict['coverage_level'] == 'Standard':
			return 2234.9147048274926
		elif tree_dict['coverage_level'] == 'Basic':
			return 250.82102404218634
	elif tree_dict['smoker'] == 'no':
		if tree_dict['coverage_level'] == 'Premium':
			return 129.41707079402948
		elif tree_dict['coverage_level'] == 'Standard':
			return -2810.854578391044
		elif tree_dict['coverage_level'] == 'Basic':
			return -4859.050724198506

def tree_1(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['coverage_level'] == 'Premium':
			return 4755.068650024802
		elif tree_dict['coverage_level'] == 'Standard':
			return 2011.4232343447427
		elif tree_dict['coverage_level'] == 'Basic':
			return 225.7389216379666
	elif tree_dict['smoker'] == 'no':
		if tree_dict['coverage_level'] == 'Premium':
			return 116.47536371462517
		elif tree_dict['coverage_level'] == 'Standard':
			return -2529.769120551939
		elif tree_dict['coverage_level'] == 'Basic':
			return -4373.145651778657

def tree_2(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['medical_history'] == 'Diabetes':
			return 1498.1639845301634
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 222.2835986071216
		elif tree_dict['medical_history'] == 'Heart disease':
			return 4474.28387953781
	elif tree_dict['smoker'] == 'no':
		if tree_dict['medical_history'] == 'Diabetes':
			return -2819.330364915338
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -3707.469866797592
		elif tree_dict['medical_history'] == 'Heart disease':
			return 285.00039623405854

def tree_3(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['coverage_level'] == 'Premium':
			return 4070.1566939713575
		elif tree_dict['coverage_level'] == 'Standard':
			return 1602.1062513068905
		elif tree_dict['coverage_level'] == 'Basic':
			return -2.675511572202564
	elif tree_dict['smoker'] == 'no':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -3513.8597808145446
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 437.9078269591341
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -2498.2928329378287

def tree_4(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -21.72942093520846
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 3881.9983310189346
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 1099.4971233505125
	elif tree_dict['smoker'] == 'no':
		if tree_dict['coverage_level'] == 'Premium':
			return 504.3036157627261
		elif tree_dict['coverage_level'] == 'Standard':
			return -1882.2275843279513
		elif tree_dict['coverage_level'] == 'Basic':
			return -3540.843522988578

def tree_5(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['smoker'] == 'yes':
			return 981.7791114553816
		elif tree_dict['smoker'] == 'no':
			return -2176.6986319233665
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -3087.3762214598682
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 464.31547617770866
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -2109.979813021715
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['smoker'] == 'yes':
			return 3669.75239802524
		elif tree_dict['smoker'] == 'no':
			return 610.2801550542224

def tree_6(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 598.0035499983277
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 4004.7526029164937
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 1455.873354046826
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1650.2052625731865
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1693.1228734550718
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -777.6202420936316
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -3207.5634758593656
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 470.9370373109364
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -2345.049515976447

def tree_7(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['smoker'] == 'yes':
			return 869.9662267320391
		elif tree_dict['smoker'] == 'no':
			return -1951.6049960398338
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['smoker'] == 'yes':
			return 26.732049830210194
		elif tree_dict['smoker'] == 'no':
			return -2817.8257609205466
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['smoker'] == 'yes':
			return 3297.242496747718
		elif tree_dict['smoker'] == 'no':
			return 550.4047548802093

def tree_8(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 537.2593241253261
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 3594.1015291614012
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 1313.8534270555513
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1484.85227749886
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1520.7271926117855
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -694.5501723141069
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -2883.7394354498665
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 416.8386866702187
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -2102.2604135424417

def tree_9(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['smoker'] == 'yes':
			return 770.717845362574
		elif tree_dict['smoker'] == 'no':
			return -1749.7782614665987
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['smoker'] == 'yes':
			return 32.27064032160077
		elif tree_dict['smoker'] == 'no':
			return -2533.7924472130626
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['smoker'] == 'yes':
			return 2962.566714334802
		elif tree_dict['smoker'] == 'no':
			return 496.39029953174906

def tree_10(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 482.68623201395303
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 3225.609920952378
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 1185.700089930556
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['medical_history'] == 'Diabetes':
			return -600.5213594956768
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -1335.4246231067316
		elif tree_dict['medical_history'] == 'Heart disease':
			return 1408.2306524572864
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -2592.619404012961
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 368.8261589530374
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -1884.6300644012517

def tree_11(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['coverage_level'] == 'Premium':
			return 2576.05455547014
		elif tree_dict['coverage_level'] == 'Standard':
			return 948.4565978559843
		elif tree_dict['coverage_level'] == 'Basic':
			return -85.49058940336033
	elif tree_dict['smoker'] == 'no':
		if tree_dict['medical_history'] == 'Diabetes':
			return -1552.2549264380218
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -2242.027920856806
		elif tree_dict['medical_history'] == 'Heart disease':
			return 393.155393021401

def tree_12(tree_dict):
	if tree_dict['family_medical_history'] == 'High blood pressure':
		if tree_dict['coverage_level'] == 'Premium':
			return 362.9205422369981
		elif tree_dict['coverage_level'] == 'Standard':
			return -1308.8206801237172
		elif tree_dict['coverage_level'] == 'Basic':
			return -2272.2096612377563
	elif tree_dict['family_medical_history'] == 'Heart disease':
		if tree_dict['medical_history'] == 'Diabetes':
			return 1173.1843593165067
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 302.0017311751723
		elif tree_dict['medical_history'] == 'Heart disease':
			return 2946.8801790799926
	elif tree_dict['family_medical_history'] == 'Diabetes':
		if tree_dict['coverage_level'] == 'Premium':
			return 995.3832816234245
		elif tree_dict['coverage_level'] == 'Standard':
			return -590.400784075205
		elif tree_dict['coverage_level'] == 'Basic':
			return -1633.023570533673

def tree_13(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['medical_history'] == 'Diabetes':
			return 583.2377135057359
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 12.208159262129508
		elif tree_dict['medical_history'] == 'Heart disease':
			return 2440.173678390796
	elif tree_dict['smoker'] == 'no':
		if tree_dict['coverage_level'] == 'Premium':
			return 308.95726375144636
		elif tree_dict['coverage_level'] == 'Standard':
			return -1125.3757883594699
		elif tree_dict['coverage_level'] == 'Basic':
			return -2155.5217572377464

def tree_14(tree_dict):
	if tree_dict['family_medical_history'] == 'High blood pressure':
		if tree_dict['medical_history'] == 'Diabetes':
			return -1413.7139454096277
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -1873.6907490957678
		elif tree_dict['medical_history'] == 'Heart disease':
			return 374.3306202426689
	elif tree_dict['family_medical_history'] == 'Heart disease':
		if tree_dict['medical_history'] == 'Diabetes':
			return 1078.8930543152874
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 320.54654838781806
		elif tree_dict['medical_history'] == 'Heart disease':
			return 2572.4933862038033
	elif tree_dict['family_medical_history'] == 'Diabetes':
		if tree_dict['smoker'] == 'yes':
			return 594.2142010975141
		elif tree_dict['smoker'] == 'no':
			return -1281.823357824322

def tree_15(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['medical_history'] == 'Diabetes':
			return 871.9292916646656
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 286.20494991612725
		elif tree_dict['medical_history'] == 'Heart disease':
			return 2471.76274460679
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1076.0937535789167
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1111.9629310998296
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -483.89233982158265
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['medical_history'] == 'Diabetes':
			return -1421.2682975500072
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -1889.0513172643955
		elif tree_dict['medical_history'] == 'Heart disease':
			return 234.8642366947369

def tree_16(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 40.641699628676314
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 2008.0280678801937
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 544.2849254484858
	elif tree_dict['smoker'] == 'no':
		if tree_dict['medical_history'] == 'Diabetes':
			return -1199.5954589008027
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -1718.7068976507223
		elif tree_dict['medical_history'] == 'Heart disease':
			return 277.8133892668502

def tree_17(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['coverage_level'] == 'Premium':
			return 2154.3913650574186
		elif tree_dict['coverage_level'] == 'Standard':
			return 983.700976320349
		elif tree_dict['coverage_level'] == 'Basic':
			return 29.409849127559927
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -228.10164442427623
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1692.1881495164268
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 194.82860390574157
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['coverage_level'] == 'Premium':
			return 683.9967146400724
		elif tree_dict['coverage_level'] == 'Standard':
			return -669.9264105324943
		elif tree_dict['coverage_level'] == 'Basic':
			return -1462.5760260305924
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1933.5920709843442
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 96.74111063953536
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -1373.5149548552756

def tree_18(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 1985.9271517308462
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return 400.5499947050652
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 943.8566746584822
		elif tree_dict['exercise_frequency'] == 'Never':
			return -154.35396555091745
	elif tree_dict['smoker'] == 'no':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1625.7644128211107
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 307.527504845569
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -1031.514725107882

def tree_19(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1074.248222318455
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 791.8466806770512
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -609.9702737525564
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['coverage_level'] == 'Premium':
			return 260.0274895366455
		elif tree_dict['coverage_level'] == 'Standard':
			return -891.4001861330061
		elif tree_dict['coverage_level'] == 'Basic':
			return -1603.9590965202474
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['coverage_level'] == 'Premium':
			return 2096.967548371034
		elif tree_dict['coverage_level'] == 'Standard':
			return 964.9876910914112
		elif tree_dict['coverage_level'] == 'Basic':
			return 198.50507060774365

def tree_20(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['medical_history'] == 'Diabetes':
			return 618.2144346066426
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 224.9746090795938
		elif tree_dict['medical_history'] == 'Heart disease':
			return 1917.0186880566591
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 1560.239640809729
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return 213.74720752220702
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 632.3517771044993
		elif tree_dict['exercise_frequency'] == 'Never':
			return -340.04857626513086
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1246.6552591461439
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 586.6440130020798
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -751.3126900286533
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['coverage_level'] == 'Premium':
			return 7.741686407219407
		elif tree_dict['coverage_level'] == 'Standard':
			return -1058.1564073583083
		elif tree_dict['coverage_level'] == 'Basic':
			return -1737.2627742400016

def tree_21(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['coverage_level'] == 'Premium':
			return 2056.091305821247
		elif tree_dict['coverage_level'] == 'Standard':
			return 950.280444570316
		elif tree_dict['coverage_level'] == 'Basic':
			return 254.13070250470548
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1053.8798169997076
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 658.8857986355268
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -614.212496244667
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['smoker'] == 'yes':
			return 843.6657221773631
		elif tree_dict['smoker'] == 'no':
			return -693.9837709518075
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1569.1503483670867
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 149.6533104553229
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -1223.0699671915631

def tree_22(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['medical_history'] == 'Diabetes':
			return 373.98783895630396
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 31.5214938073418
		elif tree_dict['medical_history'] == 'Heart disease':
			return 1653.2508519746043
	elif tree_dict['smoker'] == 'no':
		if tree_dict['coverage_level'] == 'Premium':
			return 211.4322350495414
		elif tree_dict['coverage_level'] == 'Standard':
			return -767.7908846081426
		elif tree_dict['coverage_level'] == 'Basic':
			return -1457.1890390063936

def tree_23(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['coverage_level'] == 'Premium':
			return 1683.6723896944236
		elif tree_dict['coverage_level'] == 'Standard':
			return 789.8704317521815
		elif tree_dict['coverage_level'] == 'Basic':
			return 55.96500122544848
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -149.28644458940806
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1326.1724228209441
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 166.27799355028608
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['medical_history'] == 'Diabetes':
			return -567.7405368379226
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -1206.0214002835157
		elif tree_dict['medical_history'] == 'Heart disease':
			return 479.3712867195711
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1524.6148143151822
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 52.742997608954944
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -1081.1153809657512

def tree_24(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['medical_history'] == 'Diabetes':
			return 676.1625210393273
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 372.08191464928353
		elif tree_dict['medical_history'] == 'Heart disease':
			return 1847.7202674315115
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -913.8385801800107
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 542.6399541730888
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -540.0069671456972
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -608.6451495105698
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1050.7237059879503
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -183.43342254654405
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['smoker'] == 'yes':
			return -86.5046169354994
		elif tree_dict['smoker'] == 'no':
			return -1447.3633640095547

def tree_25(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['smoker'] == 'yes':
			return 1475.1879496072797
		elif tree_dict['smoker'] == 'no':
			return 188.9430395274534
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['occupation'] == 'White collar':
			return 704.8184059025044
		elif tree_dict['occupation'] == 'Blue collar':
			return 284.5407399910337
		elif tree_dict['occupation'] == 'Student':
			return -509.3422404125392
		elif tree_dict['occupation'] == 'Unemployed':
			return -856.1100064463798
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['medical_history'] == 'Diabetes':
			return -1032.119881256205
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -1244.7663732175579
		elif tree_dict['medical_history'] == 'Heart disease':
			return 166.51774725132776

def tree_26(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 104.26309490114052
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1564.8120026321694
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 544.1160298165573
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['coverage_level'] == 'Premium':
			return 1197.966755206016
		elif tree_dict['coverage_level'] == 'Standard':
			return 256.08666599193117
		elif tree_dict['coverage_level'] == 'Basic':
			return -223.58677930483603
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -998.1507151551579
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 487.7655635583766
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -595.7940085845723
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['medical_history'] == 'Diabetes':
			return -1000.187375733732
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -1269.7411184301436
		elif tree_dict['medical_history'] == 'Heart disease':
			return 129.15072969986016

def tree_27(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 1429.22716006911
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return 334.7880212599486
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 653.4565747441821
		elif tree_dict['exercise_frequency'] == 'Never':
			return -88.64680041410124
	elif tree_dict['smoker'] == 'no':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 312.8050673152878
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -841.5648329630721
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -521.7451534839685
		elif tree_dict['exercise_frequency'] == 'Never':
			return -1276.4008115689085

def tree_28(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['coverage_level'] == 'Premium':
			return 569.1922435964088
		elif tree_dict['coverage_level'] == 'Standard':
			return -315.9348999453087
		elif tree_dict['coverage_level'] == 'Basic':
			return -903.7172781856902
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['smoker'] == 'yes':
			return 11.526470931819127
		elif tree_dict['smoker'] == 'no':
			return -1110.185492224603
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['coverage_level'] == 'Premium':
			return 1510.8336437185571
		elif tree_dict['coverage_level'] == 'Standard':
			return 717.4344059668852
		elif tree_dict['coverage_level'] == 'Basic':
			return 145.2923568078932

def tree_29(tree_dict):
	if tree_dict['family_medical_history'] == 'High blood pressure':
		if tree_dict['gender'] == 'male':
			return 6.344388771952936
		elif tree_dict['gender'] == 'female':
			return -1090.9923767120836
	elif tree_dict['family_medical_history'] == 'Heart disease':
		if tree_dict['coverage_level'] == 'Premium':
			return 1522.8352445679059
		elif tree_dict['coverage_level'] == 'Standard':
			return 651.5864040076992
		elif tree_dict['coverage_level'] == 'Basic':
			return 159.3505887913267
	elif tree_dict['family_medical_history'] == 'Diabetes':
		if tree_dict['medical_history'] == 'Diabetes':
			return -423.17289194938405
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -747.6279636479989
		elif tree_dict['medical_history'] == 'Heart disease':
			return 558.4496776139111

def tree_30(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['gender'] == 'male':
			return 1164.029403526235
		elif tree_dict['gender'] == 'female':
			return 135.12371734801746
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['smoker'] == 'yes':
			return 869.974630271489
		elif tree_dict['smoker'] == 'no':
			return -134.12256060590616
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 472.10060004327056
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -652.6689787493734
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -230.02488095782107
		elif tree_dict['exercise_frequency'] == 'Never':
			return -924.9007126404181
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1168.5555651843129
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 44.56803100459923
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -826.0870897553344

def tree_31(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['bmi'] == '35 - 40':
			return 1030.7667360495861
		elif tree_dict['bmi'] == '25 - 30':
			return 430.0693570986816
		elif tree_dict['bmi'] == '40 - 54':
			return 1328.8991325956083
		elif tree_dict['bmi'] == '30 - 35':
			return 618.9429657287288
		elif tree_dict['bmi'] == '18.5 - 25':
			return -18.46897725521578
		elif tree_dict['bmi'] == '< 18.5':
			return 140.904555361451
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['smoker'] == 'yes':
			return 279.88953652819964
		elif tree_dict['smoker'] == 'no':
			return -723.7791095310542
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -449.8031096923001
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 790.1291628765249
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -124.85064907016235
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -1110.7124698702623
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 120.62004731876387
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -846.3610844718039

def tree_32(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['bmi'] == '35 - 40':
			return 1039.6049893680854
		elif tree_dict['bmi'] == '25 - 30':
			return 340.01694501881934
		elif tree_dict['bmi'] == '40 - 54':
			return 1154.6769155792751
		elif tree_dict['bmi'] == '30 - 35':
			return 515.9675169481923
		elif tree_dict['bmi'] == '18.5 - 25':
			return 15.437352129998741
		elif tree_dict['bmi'] == '< 18.5':
			return -446.61820684659256
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['medical_history'] == 'Diabetes':
			return -275.48862282881987
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -577.7524265561054
		elif tree_dict['medical_history'] == 'Heart disease':
			return 615.9043177777501
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['occupation'] == 'White collar':
			return 66.27427960373004
		elif tree_dict['occupation'] == 'Blue collar':
			return -188.33727196651938
		elif tree_dict['occupation'] == 'Student':
			return -883.4696685449063
		elif tree_dict['occupation'] == 'Unemployed':
			return -1121.9612132598932

def tree_33(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['medical_history'] == 'Diabetes':
			return 258.1541486986615
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 27.112968477583255
		elif tree_dict['medical_history'] == 'Heart disease':
			return 1125.5660691590883
	elif tree_dict['smoker'] == 'no':
		if tree_dict['gender'] == 'male':
			return 4.409400365530971
		elif tree_dict['gender'] == 'female':
			return -942.4680059622181

def tree_34(tree_dict):
	if tree_dict['family_medical_history'] == 'High blood pressure':
		if tree_dict['bmi'] == '35 - 40':
			return -230.98821415959023
		elif tree_dict['bmi'] == '25 - 30':
			return -854.4853538557228
		elif tree_dict['bmi'] == '40 - 54':
			return 111.44685259060343
		elif tree_dict['bmi'] == '30 - 35':
			return -568.0133671275313
		elif tree_dict['bmi'] == '18.5 - 25':
			return -1077.4216380939893
		elif tree_dict['bmi'] == '< 18.5':
			return -1100.8931460734732
	elif tree_dict['family_medical_history'] == 'Heart disease':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 1399.2865118490906
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return 403.33056724388354
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 709.5693270398746
		elif tree_dict['exercise_frequency'] == 'Never':
			return 108.86852120001967
	elif tree_dict['family_medical_history'] == 'Diabetes':
		if tree_dict['bmi'] == '35 - 40':
			return 222.90928658030077
		elif tree_dict['bmi'] == '25 - 30':
			return -663.9445222559478
		elif tree_dict['bmi'] == '40 - 54':
			return 329.8233245348344
		elif tree_dict['bmi'] == '30 - 35':
			return -310.7703629153137
		elif tree_dict['bmi'] == '18.5 - 25':
			return -798.6687205943718
		elif tree_dict['bmi'] == '< 18.5':
			return -850.5860319311126

def tree_35(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['medical_history'] == 'Diabetes':
			return 348.7167751977786
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 135.3732834715509
		elif tree_dict['medical_history'] == 'Heart disease':
			return 1171.2225719732883
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['medical_history'] == 'Diabetes':
			return 140.91029942239342
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -149.14548774282562
		elif tree_dict['medical_history'] == 'Heart disease':
			return 932.5853105468098
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['coverage_level'] == 'Premium':
			return 344.70576536564147
		elif tree_dict['coverage_level'] == 'Standard':
			return -373.776537544457
		elif tree_dict['coverage_level'] == 'Basic':
			return -792.4986385885419
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['gender'] == 'male':
			return -121.88858034696098
		elif tree_dict['gender'] == 'female':
			return -999.9885952661318

def tree_36(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 154.390108687952
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1176.1792284457629
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 412.5981095036824
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['gender'] == 'male':
			return 399.7502173697946
		elif tree_dict['gender'] == 'female':
			return -520.4715677962542
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 206.38332225056988
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -679.7245106951306
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -390.99710278854735
		elif tree_dict['exercise_frequency'] == 'Never':
			return -994.5357983233732

def tree_37(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['gender'] == 'male':
			return 256.282088419601
		elif tree_dict['gender'] == 'female':
			return -584.2815058319403
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['smoker'] == 'yes':
			return 47.195937011291896
		elif tree_dict['smoker'] == 'no':
			return -867.852123684981
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['gender'] == 'male':
			return 1019.4709774386247
		elif tree_dict['gender'] == 'female':
			return 164.5509795536858

def tree_38(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 215.5259087912876
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1218.4212172058471
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 496.4929755457773
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -588.3422149398492
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 348.4850425264918
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -368.31761266723146
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['bmi'] == '35 - 40':
			return 327.79563991273375
		elif tree_dict['bmi'] == '25 - 30':
			return -312.14716034470763
		elif tree_dict['bmi'] == '40 - 54':
			return 537.5711735191753
		elif tree_dict['bmi'] == '30 - 35':
			return -115.66759123503486
		elif tree_dict['bmi'] == '18.5 - 25':
			return -479.93215696552073
		elif tree_dict['bmi'] == '< 18.5':
			return -723.7597742152126
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -908.6895634534432
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 92.25230524538253
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -695.5943000861088

def tree_39(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['occupation'] == 'White collar':
			return 902.5199975874754
		elif tree_dict['occupation'] == 'Blue collar':
			return 652.9045202473255
		elif tree_dict['occupation'] == 'Student':
			return 173.18358141551548
		elif tree_dict['occupation'] == 'Unemployed':
			return -100.0959915234468
	elif tree_dict['smoker'] == 'no':
		if tree_dict['occupation'] == 'White collar':
			return 88.23856802855141
		elif tree_dict['occupation'] == 'Blue collar':
			return -102.64051509206973
		elif tree_dict['occupation'] == 'Student':
			return -698.4537786112636
		elif tree_dict['occupation'] == 'Unemployed':
			return -879.6445198613585

def tree_40(tree_dict):
	if tree_dict['bmi'] == '35 - 40':
		if tree_dict['coverage_level'] == 'Premium':
			return 812.5572006159629
		elif tree_dict['coverage_level'] == 'Standard':
			return 193.23505499617454
		elif tree_dict['coverage_level'] == 'Basic':
			return -227.7513002330766
	elif tree_dict['bmi'] == '25 - 30':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -703.4226363635373
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 336.5923052346863
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -545.709867670953
	elif tree_dict['bmi'] == '40 - 54':
		if tree_dict['gender'] == 'male':
			return 865.6479311109067
		elif tree_dict['gender'] == 'female':
			return 50.89126400654569
	elif tree_dict['bmi'] == '30 - 35':
		if tree_dict['medical_history'] == 'Diabetes':
			return -260.3385190563262
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -576.3158415957802
		elif tree_dict['medical_history'] == 'Heart disease':
			return 403.866008240283
	elif tree_dict['bmi'] == '18.5 - 25':
		if tree_dict['coverage_level'] == 'Premium':
			return 1.8843646543332468
		elif tree_dict['coverage_level'] == 'Standard':
			return -584.9818108407552
		elif tree_dict['coverage_level'] == 'Basic':
			return -1064.668241252477
	elif tree_dict['bmi'] == '< 18.5':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 12.544722835321409
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -961.6609363493873
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -635.2764052637034
		elif tree_dict['exercise_frequency'] == 'Never':
			return -1014.5253062410135

def tree_41(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['coverage_level'] == 'Premium':
			return 371.3807326292405
		elif tree_dict['coverage_level'] == 'Standard':
			return -208.7172524861881
		elif tree_dict['coverage_level'] == 'Basic':
			return -596.3079204153461
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['gender'] == 'male':
			return 21.893859033320812
		elif tree_dict['gender'] == 'female':
			return -763.8981022915482
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['gender'] == 'male':
			return 887.1789750156187
		elif tree_dict['gender'] == 'female':
			return 152.59677335284013

def tree_42(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 191.73437384106944
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 1086.71871534949
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 439.32753752822384
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['bmi'] == '35 - 40':
			return 49.805750527301704
		elif tree_dict['bmi'] == '25 - 30':
			return -343.015671509229
		elif tree_dict['bmi'] == '40 - 54':
			return 216.51902058709842
		elif tree_dict['bmi'] == '30 - 35':
			return -258.5239853826167
		elif tree_dict['bmi'] == '18.5 - 25':
			return -718.546052725746
		elif tree_dict['bmi'] == '< 18.5':
			return -870.1473230117898
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -342.24220121542254
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 599.1290806342469
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -87.62124267434979
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['smoker'] == 'yes':
			return -38.00246573954694
		elif tree_dict['smoker'] == 'no':
			return -833.5064832132421

def tree_43(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 78.84297193986282
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 959.1282117793711
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 347.3539852214194
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['coverage_level'] == 'Premium':
			return 737.3921855849109
		elif tree_dict['coverage_level'] == 'Standard':
			return 152.62404298296963
		elif tree_dict['coverage_level'] == 'Basic':
			return -170.5909089954682
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['smoker'] == 'yes':
			return 142.88823395876966
		elif tree_dict['smoker'] == 'no':
			return -613.2291672196284
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['smoker'] == 'yes':
			return -97.39846606329404
		elif tree_dict['smoker'] == 'no':
			return -773.0327282425491

def tree_44(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['children'] == 0:
			return -25.50891716949588
		elif tree_dict['children'] == 2:
			return 415.10047200940375
		elif tree_dict['children'] == 1:
			return 237.89990810394448
		elif tree_dict['children'] == 5:
			return 1039.4473289716743
		elif tree_dict['children'] == 3:
			return 444.5831013636678
		elif tree_dict['children'] == 4:
			return 693.6069367434341
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -411.9786713203369
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 419.36615595960103
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -196.69124800571325
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['bmi'] == '35 - 40':
			return -197.2759851279068
		elif tree_dict['bmi'] == '25 - 30':
			return -646.7169413660683
		elif tree_dict['bmi'] == '40 - 54':
			return 49.087115817862056
		elif tree_dict['bmi'] == '30 - 35':
			return -505.65643064945004
		elif tree_dict['bmi'] == '18.5 - 25':
			return -912.8978555664125
		elif tree_dict['bmi'] == '< 18.5':
			return -756.6120012681502

def tree_45(tree_dict):
	if tree_dict['gender'] == 'male':
		if tree_dict['region'] == 'southwest':
			return 18.945548686154478
		elif tree_dict['region'] == 'southeast':
			return 391.2067981045524
		elif tree_dict['region'] == 'northwest':
			return 95.79767303999996
		elif tree_dict['region'] == 'northeast':
			return 876.5334074045343
	elif tree_dict['gender'] == 'female':
		if tree_dict['medical_history'] == 'Diabetes':
			return -498.9505003332172
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -686.0876891103529
		elif tree_dict['medical_history'] == 'Heart disease':
			return 136.19999562205075

def tree_46(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['occupation'] == 'White collar':
			return 749.918063917416
		elif tree_dict['occupation'] == 'Blue collar':
			return 544.0308177030406
		elif tree_dict['occupation'] == 'Student':
			return 128.78401409240675
		elif tree_dict['occupation'] == 'Unemployed':
			return -88.4068155175773
	elif tree_dict['smoker'] == 'no':
		if tree_dict['bmi'] == '35 - 40':
			return -183.4207750901996
		elif tree_dict['bmi'] == '25 - 30':
			return -608.343278526981
		elif tree_dict['bmi'] == '40 - 54':
			return 89.26468928759849
		elif tree_dict['bmi'] == '30 - 35':
			return -413.1614840536941
		elif tree_dict['bmi'] == '18.5 - 25':
			return -761.1119669674978
		elif tree_dict['bmi'] == '< 18.5':
			return -822.806953477987

def tree_47(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['bmi'] == '35 - 40':
			return 648.8160835231986
		elif tree_dict['bmi'] == '25 - 30':
			return 301.47822659628366
		elif tree_dict['bmi'] == '40 - 54':
			return 865.4939510153099
		elif tree_dict['bmi'] == '30 - 35':
			return 436.1358817756752
		elif tree_dict['bmi'] == '18.5 - 25':
			return -1.3138331832400985
		elif tree_dict['bmi'] == '< 18.5':
			return -52.74071661433178
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -480.9863550526051
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 282.2174369116865
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -304.68511183718925
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['children'] == 0:
			return -434.3152796307729
		elif tree_dict['children'] == 2:
			return -19.026330117296464
		elif tree_dict['children'] == 1:
			return -272.4677386704004
		elif tree_dict['children'] == 5:
			return 476.65106749562136
		elif tree_dict['children'] == 3:
			return 160.42250611775677
		elif tree_dict['children'] == 4:
			return 416.32718144691955
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -736.7192300447042
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 90.82452298626276
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -553.5768003341203

def tree_48(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['gender'] == 'male':
			return 196.79210336247107
		elif tree_dict['gender'] == 'female':
			return -448.6420039829437
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['occupation'] == 'White collar':
			return 122.15126914443604
		elif tree_dict['occupation'] == 'Blue collar':
			return -105.78662430659585
		elif tree_dict['occupation'] == 'Student':
			return -583.2721022470976
		elif tree_dict['occupation'] == 'Unemployed':
			return -647.1551285143523
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['children'] == 0:
			return -22.20875536875816
		elif tree_dict['children'] == 2:
			return 344.85976827359644
		elif tree_dict['children'] == 1:
			return 179.84832238733432
		elif tree_dict['children'] == 5:
			return 915.9839802601099
		elif tree_dict['children'] == 3:
			return 502.7751191759754
		elif tree_dict['children'] == 4:
			return 680.0153814039305

def tree_49(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 107.58492654157742
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 855.3854850415347
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 295.80793003242314
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['smoker'] == 'yes':
			return 260.8872355587674
		elif tree_dict['smoker'] == 'no':
			return -361.3380483382476
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -652.813129586287
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 81.71738546229491
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -464.3320040079625

def tree_50(tree_dict):
	if tree_dict['bmi'] == '35 - 40':
		if tree_dict['children'] == 0:
			return -199.06803049184177
		elif tree_dict['children'] == 2:
			return 3.0451982288927835
		elif tree_dict['children'] == 1:
			return -144.60569941523602
		elif tree_dict['children'] == 5:
			return 767.1697300354274
		elif tree_dict['children'] == 3:
			return 251.81259649943118
		elif tree_dict['children'] == 4:
			return 358.9878356823698
	elif tree_dict['bmi'] == '25 - 30':
		if tree_dict['children'] == 0:
			return -626.9906299087486
		elif tree_dict['children'] == 2:
			return -396.1707800199444
		elif tree_dict['children'] == 1:
			return -482.3817358405689
		elif tree_dict['children'] == 5:
			return 341.1327997531024
		elif tree_dict['children'] == 3:
			return -89.90475652378404
		elif tree_dict['children'] == 4:
			return -49.38075678588753
	elif tree_dict['bmi'] == '40 - 54':
		if tree_dict['age'] == '26-41':
			return 133.68989529147356
		elif tree_dict['age'] == '41-56':
			return 591.9473063153654
		elif tree_dict['age'] == '>56':
			return 714.6714799519076
		elif tree_dict['age'] == '18-26':
			return -130.84024929961797
	elif tree_dict['bmi'] == '30 - 35':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 389.0002862107341
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -201.72254559924747
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -71.73027702261594
		elif tree_dict['exercise_frequency'] == 'Never':
			return -473.6754627248453
	elif tree_dict['bmi'] == '18.5 - 25':
		if tree_dict['medical_history'] == 'Diabetes':
			return -532.4313718336099
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -717.1206338631728
		elif tree_dict['medical_history'] == 'Heart disease':
			return 10.394966241644775
	elif tree_dict['bmi'] == '< 18.5':
		if tree_dict['region'] == 'southwest':
			return -849.7285005050439
		elif tree_dict['region'] == 'southeast':
			return -641.2422382947047
		elif tree_dict['region'] == 'northwest':
			return -653.9062054863841
		elif tree_dict['region'] == 'northeast':
			return 20.624301944044735

def tree_51(tree_dict):
	if tree_dict['gender'] == 'male':
		if tree_dict['region'] == 'southwest':
			return 8.097188002075047
		elif tree_dict['region'] == 'southeast':
			return 336.212710901237
		elif tree_dict['region'] == 'northwest':
			return 78.43176540745388
		elif tree_dict['region'] == 'northeast':
			return 770.8962971251536
	elif tree_dict['gender'] == 'female':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -569.0231753751809
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 104.25466800384447
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -434.75847468163613

def tree_52(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 835.6043200744709
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return 157.135927674704
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 404.4766628380003
		elif tree_dict['exercise_frequency'] == 'Never':
			return 44.5668392784874
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['bmi'] == '35 - 40':
			return 333.49851024114434
		elif tree_dict['bmi'] == '25 - 30':
			return 37.81310815239162
		elif tree_dict['bmi'] == '40 - 54':
			return 515.4882740681454
		elif tree_dict['bmi'] == '30 - 35':
			return 83.77047482034979
		elif tree_dict['bmi'] == '18.5 - 25':
			return -224.65452084962774
		elif tree_dict['bmi'] == '< 18.5':
			return -416.4765999737397
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -484.52754667269124
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 221.7464085015988
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -301.80149506261944
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 105.18724393092974
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -426.72025050706486
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -288.5624726150532
		elif tree_dict['exercise_frequency'] == 'Never':
			return -745.151985344502

def tree_53(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['children'] == 0:
			return -96.10938202147594
		elif tree_dict['children'] == 2:
			return 217.1829073563049
		elif tree_dict['children'] == 1:
			return 34.78327594080906
		elif tree_dict['children'] == 5:
			return 738.0668029547817
		elif tree_dict['children'] == 3:
			return 356.8923431634761
		elif tree_dict['children'] == 4:
			return 517.519046192433
	elif tree_dict['smoker'] == 'no':
		if tree_dict['medical_history'] == 'Diabetes':
			return -399.3932467251619
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -559.6465114764162
		elif tree_dict['medical_history'] == 'Heart disease':
			return 104.00417062875363

def tree_54(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['region'] == 'southwest':
			return 129.60314687140243
		elif tree_dict['region'] == 'southeast':
			return 368.64777979113546
		elif tree_dict['region'] == 'northwest':
			return 157.67027008752743
		elif tree_dict['region'] == 'northeast':
			return 825.5249778268658
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -328.5050538135151
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 330.93771519043736
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -157.17163141177943
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['gender'] == 'male':
			return -28.810605870990063
		elif tree_dict['gender'] == 'female':
			return -582.6892255447937

def tree_55(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['age'] == '26-41':
			return 224.34149622786737
		elif tree_dict['age'] == '41-56':
			return 543.5112847340284
		elif tree_dict['age'] == '>56':
			return 823.6309840136813
		elif tree_dict['age'] == '18-26':
			return -0.8133786305924129
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['medical_history'] == 'Diabetes':
			return -230.34610124866302
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -422.9397200819274
		elif tree_dict['medical_history'] == 'Heart disease':
			return 224.74121515191823
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -227.23543131125953
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 427.88295831845136
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -60.046849716883536
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['region'] == 'southwest':
			return -554.624850395188
		elif tree_dict['region'] == 'southeast':
			return -355.47594503791936
		elif tree_dict['region'] == 'northwest':
			return -517.8890949891345
		elif tree_dict['region'] == 'northeast':
			return 151.52137014121467

def tree_56(tree_dict):
	if tree_dict['bmi'] == '35 - 40':
		if tree_dict['smoker'] == 'yes':
			return 415.24539936500514
		elif tree_dict['smoker'] == 'no':
			return -160.66841637789375
	elif tree_dict['bmi'] == '25 - 30':
		if tree_dict['smoker'] == 'yes':
			return 110.8668213516166
		elif tree_dict['smoker'] == 'no':
			return -472.62028975999885
	elif tree_dict['bmi'] == '40 - 54':
		if tree_dict['age'] == '26-41':
			return 124.30171810423342
		elif tree_dict['age'] == '41-56':
			return 508.25371643144376
		elif tree_dict['age'] == '>56':
			return 625.4902550158877
		elif tree_dict['age'] == '18-26':
			return -108.03499675389811
	elif tree_dict['bmi'] == '30 - 35':
		if tree_dict['children'] == 0:
			return -484.07561749390464
		elif tree_dict['children'] == 2:
			return -151.9677187041104
		elif tree_dict['children'] == 1:
			return -314.73253884595175
		elif tree_dict['children'] == 5:
			return 331.2032859572309
		elif tree_dict['children'] == 3:
			return 43.226472190599
		elif tree_dict['children'] == 4:
			return 179.26676068904285
	elif tree_dict['bmi'] == '18.5 - 25':
		if tree_dict['occupation'] == 'White collar':
			return -28.65341938951788
		elif tree_dict['occupation'] == 'Blue collar':
			return -201.50630938438707
		elif tree_dict['occupation'] == 'Student':
			return -587.8114812695985
		elif tree_dict['occupation'] == 'Unemployed':
			return -636.4134159569411
	elif tree_dict['bmi'] == '< 18.5':
		if tree_dict['age'] == '26-41':
			return -522.7389212382761
		elif tree_dict['age'] == '41-56':
			return -403.34571334256566
		elif tree_dict['age'] == '>56':
			return -98.75497789523567
		elif tree_dict['age'] == '18-26':
			return -1052.8490769350265

def tree_57(tree_dict):
	if tree_dict['gender'] == 'male':
		if tree_dict['children'] == 0:
			return -101.74365481717467
		elif tree_dict['children'] == 2:
			return 171.19109786865226
		elif tree_dict['children'] == 1:
			return 29.710565415834257
		elif tree_dict['children'] == 5:
			return 699.4603373355329
		elif tree_dict['children'] == 3:
			return 320.8069909525197
		elif tree_dict['children'] == 4:
			return 467.348461001687
	elif tree_dict['gender'] == 'female':
		if tree_dict['age'] == '26-41':
			return -426.77141500951006
		elif tree_dict['age'] == '41-56':
			return -116.69191764516788
		elif tree_dict['age'] == '>56':
			return 79.61474166447991
		elif tree_dict['age'] == '18-26':
			return -632.9216304845202

def tree_58(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['occupation'] == 'White collar':
			return 211.43968392195447
		elif tree_dict['occupation'] == 'Blue collar':
			return 75.3682851869798
		elif tree_dict['occupation'] == 'Student':
			return -226.25799141733168
		elif tree_dict['occupation'] == 'Unemployed':
			return -442.0938926548652
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 151.9736365797498
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -380.4809125578276
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -218.9512661422932
		elif tree_dict['exercise_frequency'] == 'Never':
			return -523.2840190640633
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['region'] == 'southwest':
			return 83.97675605370162
		elif tree_dict['region'] == 'southeast':
			return 355.47114135451324
		elif tree_dict['region'] == 'northwest':
			return 166.6227945413661
		elif tree_dict['region'] == 'northeast':
			return 773.7606824489089

def tree_59(tree_dict):
	if tree_dict['family_medical_history'] == 'High blood pressure':
		if tree_dict['smoker'] == 'yes':
			return 25.047781742967146
		elif tree_dict['smoker'] == 'no':
			return -518.4531391060104
	elif tree_dict['family_medical_history'] == 'Heart disease':
		if tree_dict['region'] == 'southwest':
			return 54.99376698553091
		elif tree_dict['region'] == 'southeast':
			return 373.46216308420657
		elif tree_dict['region'] == 'northwest':
			return 179.04235224167917
		elif tree_dict['region'] == 'northeast':
			return 782.7840546986932
	elif tree_dict['family_medical_history'] == 'Diabetes':
		if tree_dict['region'] == 'southwest':
			return -326.8898399937063
		elif tree_dict['region'] == 'southeast':
			return -95.56044249636504
		elif tree_dict['region'] == 'northwest':
			return -290.8592145931556
		elif tree_dict['region'] == 'northeast':
			return 302.67034141502484

def tree_60(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['children'] == 0:
			return -26.963020474992813
		elif tree_dict['children'] == 2:
			return 300.9368999339098
		elif tree_dict['children'] == 1:
			return 158.2779730042014
		elif tree_dict['children'] == 5:
			return 730.1636961014423
		elif tree_dict['children'] == 3:
			return 327.0001631369552
		elif tree_dict['children'] == 4:
			return 518.6035478818188
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['children'] == 0:
			return -404.26248033603287
		elif tree_dict['children'] == 2:
			return -125.27491425249771
		elif tree_dict['children'] == 1:
			return -274.1720646107781
		elif tree_dict['children'] == 5:
			return 343.9160355558055
		elif tree_dict['children'] == 3:
			return 90.63809811972081
		elif tree_dict['children'] == 4:
			return 166.46200539732052
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['children'] == 0:
			return -629.5574510767552
		elif tree_dict['children'] == 2:
			return -375.8886770198425
		elif tree_dict['children'] == 1:
			return -479.0135951040595
		elif tree_dict['children'] == 5:
			return 68.59784519057858
		elif tree_dict['children'] == 3:
			return -197.32563892186423
		elif tree_dict['children'] == 4:
			return -63.04701853189676

def tree_61(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['bmi'] == '35 - 40':
			return 412.27041118168785
		elif tree_dict['bmi'] == '25 - 30':
			return 131.62468792784009
		elif tree_dict['bmi'] == '40 - 54':
			return 622.0550873438054
		elif tree_dict['bmi'] == '30 - 35':
			return 262.2901769088614
		elif tree_dict['bmi'] == '18.5 - 25':
			return -35.999404661747825
		elif tree_dict['bmi'] == '< 18.5':
			return -271.2543216061375
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -76.95579511191139
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 468.7678048737934
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 49.139338280060706
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['gender'] == 'male':
			return 107.37902478318256
		elif tree_dict['gender'] == 'female':
			return -392.68205224026804
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['bmi'] == '35 - 40':
			return -104.04335637668888
		elif tree_dict['bmi'] == '25 - 30':
			return -560.7252644061329
		elif tree_dict['bmi'] == '40 - 54':
			return -45.077372400035244
		elif tree_dict['bmi'] == '30 - 35':
			return -375.8154273614821
		elif tree_dict['bmi'] == '18.5 - 25':
			return -562.5036670231586
		elif tree_dict['bmi'] == '< 18.5':
			return -627.0730931264367

def tree_62(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['gender'] == 'male':
			return 468.11253581507714
		elif tree_dict['gender'] == 'female':
			return -1.6489717021770602
	elif tree_dict['smoker'] == 'no':
		if tree_dict['children'] == 0:
			return -599.2783083351063
		elif tree_dict['children'] == 2:
			return -310.1643814905322
		elif tree_dict['children'] == 1:
			return -436.82357088618033
		elif tree_dict['children'] == 5:
			return 118.41547612336932
		elif tree_dict['children'] == 3:
			return -161.60879952931487
		elif tree_dict['children'] == 4:
			return -47.37700095240332

def tree_63(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 112.69361276076725
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 703.3005056178082
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 278.96922353654793
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['age'] == '26-41':
			return -294.690718014241
		elif tree_dict['age'] == '41-56':
			return 21.070452748607263
		elif tree_dict['age'] == '>56':
			return 210.91781926207932
		elif tree_dict['age'] == '18-26':
			return -462.13113779353574
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['region'] == 'southwest':
			return -199.09685075316025
		elif tree_dict['region'] == 'southeast':
			return 24.915041293263002
		elif tree_dict['region'] == 'northwest':
			return -90.99121402015149
		elif tree_dict['region'] == 'northeast':
			return 430.7987456563778
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['age'] == '26-41':
			return -430.4195603020403
		elif tree_dict['age'] == '41-56':
			return -116.71504927869756
		elif tree_dict['age'] == '>56':
			return 27.61300432516391
		elif tree_dict['age'] == '18-26':
			return -637.4455953305253

def tree_64(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['bmi'] == '35 - 40':
			return -24.233682814919177
		elif tree_dict['bmi'] == '25 - 30':
			return -260.89342698316057
		elif tree_dict['bmi'] == '40 - 54':
			return 185.35451729922153
		elif tree_dict['bmi'] == '30 - 35':
			return -124.99500137444586
		elif tree_dict['bmi'] == '18.5 - 25':
			return -395.11409787297373
		elif tree_dict['bmi'] == '< 18.5':
			return -599.2171582031241
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['region'] == 'southwest':
			return -424.6695049013493
		elif tree_dict['region'] == 'southeast':
			return -255.99368232615151
		elif tree_dict['region'] == 'northwest':
			return -357.5028550436388
		elif tree_dict['region'] == 'northeast':
			return 162.38140543714155
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['age'] == '26-41':
			return 161.11379864398808
		elif tree_dict['age'] == '41-56':
			return 454.6336337015067
		elif tree_dict['age'] == '>56':
			return 622.6509570764977
		elif tree_dict['age'] == '18-26':
			return -72.20537960102438

def tree_65(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 85.49536911466791
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 608.7336293124009
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 208.3810755967825
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['bmi'] == '35 - 40':
			return 88.22003833774639
		elif tree_dict['bmi'] == '25 - 30':
			return -188.09189180650176
		elif tree_dict['bmi'] == '40 - 54':
			return 231.5265532356844
		elif tree_dict['bmi'] == '30 - 35':
			return -106.81580596216848
		elif tree_dict['bmi'] == '18.5 - 25':
			return -331.49607814416606
		elif tree_dict['bmi'] == '< 18.5':
			return -565.6223044484074
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['region'] == 'southwest':
			return -432.88550962977973
		elif tree_dict['region'] == 'southeast':
			return -299.2943284435808
		elif tree_dict['region'] == 'northwest':
			return -391.9021250342231
		elif tree_dict['region'] == 'northeast':
			return 115.2615514203128

def tree_66(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['region'] == 'southwest':
			return 52.73298843213849
		elif tree_dict['region'] == 'southeast':
			return 288.0274698825559
		elif tree_dict['region'] == 'northwest':
			return 119.25828434409969
		elif tree_dict['region'] == 'northeast':
			return 632.9280212050928
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['gender'] == 'male':
			return 358.38396327285415
		elif tree_dict['gender'] == 'female':
			return -92.41935736944336
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['bmi'] == '35 - 40':
			return -89.86273160974025
		elif tree_dict['bmi'] == '25 - 30':
			return -211.04211255567262
		elif tree_dict['bmi'] == '40 - 54':
			return 137.47954552873793
		elif tree_dict['bmi'] == '30 - 35':
			return -192.33321323740637
		elif tree_dict['bmi'] == '18.5 - 25':
			return -469.1194593665803
		elif tree_dict['bmi'] == '< 18.5':
			return -507.8791673259726
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['age'] == '26-41':
			return -425.79563762912926
		elif tree_dict['age'] == '41-56':
			return -111.89617757563909
		elif tree_dict['age'] == '>56':
			return -6.432344886012083
		elif tree_dict['age'] == '18-26':
			return -568.4096076167175

def tree_67(tree_dict):
	if tree_dict['children'] == 0:
		if tree_dict['smoker'] == 'yes':
			return -80.36624625223311
		elif tree_dict['smoker'] == 'no':
			return -539.6120157845597
	elif tree_dict['children'] == 2:
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 302.1879085137312
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -146.56728127871892
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 3.965289836170698
		elif tree_dict['exercise_frequency'] == 'Never':
			return -397.85519260105923
	elif tree_dict['children'] == 1:
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -409.8094873846047
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 116.47095112473322
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -284.58152639028316
	elif tree_dict['children'] == 5:
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 678.9853023007145
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return 248.06628051806626
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 297.24132152677316
		elif tree_dict['exercise_frequency'] == 'Never':
			return 62.25129079691772
	elif tree_dict['children'] == 3:
		if tree_dict['age'] == '26-41':
			return -92.93932050637258
		elif tree_dict['age'] == '41-56':
			return 139.74120429998018
		elif tree_dict['age'] == '>56':
			return 369.54065428807706
		elif tree_dict['age'] == '18-26':
			return -318.69489242502397
	elif tree_dict['children'] == 4:
		if tree_dict['bmi'] == '35 - 40':
			return 246.38911371236406
		elif tree_dict['bmi'] == '25 - 30':
			return -31.829275522121822
		elif tree_dict['bmi'] == '40 - 54':
			return 470.764778111202
		elif tree_dict['bmi'] == '30 - 35':
			return 143.75424745871945
		elif tree_dict['bmi'] == '18.5 - 25':
			return -150.33065104373364
		elif tree_dict['bmi'] == '< 18.5':
			return -275.25919602614863

def tree_68(tree_dict):
	if tree_dict['gender'] == 'male':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -14.185214746285597
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 511.05471138840096
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 131.96671646418602
	elif tree_dict['gender'] == 'female':
		if tree_dict['smoker'] == 'yes':
			return -2.3237366873870795
		elif tree_dict['smoker'] == 'no':
			return -411.84258487551944

def tree_69(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['age'] == '26-41':
			return -230.39722219378027
		elif tree_dict['age'] == '41-56':
			return 52.339418378100504
		elif tree_dict['age'] == '>56':
			return 170.44118578679596
		elif tree_dict['age'] == '18-26':
			return -386.28309150992925
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['occupation'] == 'White collar':
			return 84.87255869673226
		elif tree_dict['occupation'] == 'Blue collar':
			return -89.2036756332986
		elif tree_dict['occupation'] == 'Student':
			return -363.5204666935766
		elif tree_dict['occupation'] == 'Unemployed':
			return -405.38899196238935
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['bmi'] == '35 - 40':
			return 387.78730630619657
		elif tree_dict['bmi'] == '25 - 30':
			return 103.45278825330274
		elif tree_dict['bmi'] == '40 - 54':
			return 553.3110740101412
		elif tree_dict['bmi'] == '30 - 35':
			return 209.90793487119427
		elif tree_dict['bmi'] == '18.5 - 25':
			return -3.4859465842189237
		elif tree_dict['bmi'] == '< 18.5':
			return -141.1840580843197

def tree_70(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['region'] == 'southwest':
			return 99.52693786548221
		elif tree_dict['region'] == 'southeast':
			return 346.2450731617592
		elif tree_dict['region'] == 'northwest':
			return 145.2036222373813
		elif tree_dict['region'] == 'northeast':
			return 658.0522443694318
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['smoker'] == 'yes':
			return 103.56438092672188
		elif tree_dict['smoker'] == 'no':
			return -302.6683784763589
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['bmi'] == '35 - 40':
			return 137.24984995917146
		elif tree_dict['bmi'] == '25 - 30':
			return -129.78494063409784
		elif tree_dict['bmi'] == '40 - 54':
			return 266.4440601434542
		elif tree_dict['bmi'] == '30 - 35':
			return -22.01564903684251
		elif tree_dict['bmi'] == '18.5 - 25':
			return -210.6957430553762
		elif tree_dict['bmi'] == '< 18.5':
			return -350.2177203130231
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -445.4795526490802
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 42.31667062679883
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -338.1116224393785

def tree_71(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['age'] == '26-41':
			return 142.8202345260586
		elif tree_dict['age'] == '41-56':
			return 387.58339115566076
		elif tree_dict['age'] == '>56':
			return 516.3151788275154
		elif tree_dict['age'] == '18-26':
			return -48.0046496328699
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['region'] == 'southwest':
			return -252.39950346632332
		elif tree_dict['region'] == 'southeast':
			return 23.006287771704752
		elif tree_dict['region'] == 'northwest':
			return -171.39938925311353
		elif tree_dict['region'] == 'northeast':
			return 298.2564726120725
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['bmi'] == '35 - 40':
			return -138.99929236853845
		elif tree_dict['bmi'] == '25 - 30':
			return -372.8297671931242
		elif tree_dict['bmi'] == '40 - 54':
			return 4.904840878851987
		elif tree_dict['bmi'] == '30 - 35':
			return -267.6728521222337
		elif tree_dict['bmi'] == '18.5 - 25':
			return -491.79386207327946
		elif tree_dict['bmi'] == '< 18.5':
			return -473.18014012257714

def tree_72(tree_dict):
	if tree_dict['children'] == 0:
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -464.2018069401148
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return -1.6230585388582037
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -371.9415853609223
	elif tree_dict['children'] == 2:
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 240.16015901188766
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -121.8394350246714
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -0.4628719883343188
		elif tree_dict['exercise_frequency'] == 'Never':
			return -329.752024026142
	elif tree_dict['children'] == 1:
		if tree_dict['medical_history'] == 'Diabetes':
			return -207.54350840842
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -390.12663014109916
		elif tree_dict['medical_history'] == 'Heart disease':
			return 100.18549047322195
	elif tree_dict['children'] == 5:
		if tree_dict['region'] == 'southwest':
			return 87.46321580207504
		elif tree_dict['region'] == 'southeast':
			return 353.7585335695672
		elif tree_dict['region'] == 'northwest':
			return 114.64773523733707
		elif tree_dict['region'] == 'northeast':
			return 603.5554819619126
	elif tree_dict['children'] == 3:
		if tree_dict['region'] == 'southwest':
			return -112.44631840922898
		elif tree_dict['region'] == 'southeast':
			return 15.18943624598844
		elif tree_dict['region'] == 'northwest':
			return -76.08500099699573
		elif tree_dict['region'] == 'northeast':
			return 396.50083835477045
	elif tree_dict['children'] == 4:
		if tree_dict['age'] == '26-41':
			return -43.30037290352359
		elif tree_dict['age'] == '41-56':
			return 283.03939970530485
		elif tree_dict['age'] == '>56':
			return 449.26683537373236
		elif tree_dict['age'] == '18-26':
			return -102.03868244616073

def tree_73(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['gender'] == 'male':
			return 383.5447514822818
		elif tree_dict['gender'] == 'female':
			return -8.573820941557976
	elif tree_dict['smoker'] == 'no':
		if tree_dict['occupation'] == 'White collar':
			return 41.35158391930167
		elif tree_dict['occupation'] == 'Blue collar':
			return -49.280014752931216
		elif tree_dict['occupation'] == 'Student':
			return -317.5382302530622
		elif tree_dict['occupation'] == 'Unemployed':
			return -414.6192972380755

def tree_74(tree_dict):
	if tree_dict['age'] == '26-41':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -312.3136230496391
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 139.55488138929877
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -205.57986168396525
	elif tree_dict['age'] == '41-56':
		if tree_dict['bmi'] == '35 - 40':
			return 207.9870292502885
		elif tree_dict['bmi'] == '25 - 30':
			return -12.88770155207628
		elif tree_dict['bmi'] == '40 - 54':
			return 329.6695318107263
		elif tree_dict['bmi'] == '30 - 35':
			return 67.06298000548747
		elif tree_dict['bmi'] == '18.5 - 25':
			return -164.0169862746758
		elif tree_dict['bmi'] == '< 18.5':
			return -319.90643205587986
	elif tree_dict['age'] == '>56':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 564.0726157589373
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return 152.69021141095632
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 251.13695804677536
		elif tree_dict['exercise_frequency'] == 'Never':
			return 23.657590767587877
	elif tree_dict['age'] == '18-26':
		if tree_dict['children'] == 0:
			return -627.2738087535575
		elif tree_dict['children'] == 2:
			return -330.96819080105087
		elif tree_dict['children'] == 1:
			return -419.59805693139344
		elif tree_dict['children'] == 5:
			return -1.7221192204900269
		elif tree_dict['children'] == 3:
			return -265.6026594353129
		elif tree_dict['children'] == 4:
			return -91.86521143601782

def tree_75(tree_dict):
	if tree_dict['region'] == 'southwest':
		if tree_dict['age'] == '26-41':
			return -291.81294382246193
		elif tree_dict['age'] == '41-56':
			return -80.44814012129378
		elif tree_dict['age'] == '>56':
			return 83.08868164404615
		elif tree_dict['age'] == '18-26':
			return -468.64561959392347
	elif tree_dict['region'] == 'southeast':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 295.2908269900147
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -75.60355997860756
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 20.262097483145297
		elif tree_dict['exercise_frequency'] == 'Never':
			return -233.40263518356383
	elif tree_dict['region'] == 'northwest':
		if tree_dict['smoker'] == 'yes':
			return 65.01989869719017
		elif tree_dict['smoker'] == 'no':
			return -297.6679317169741
	elif tree_dict['region'] == 'northeast':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 118.97103260812214
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 560.2815271901183
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 214.63124837028698

def tree_76(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['medical_history'] == 'Diabetes':
			return 158.024940014709
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 51.1638281890625
		elif tree_dict['medical_history'] == 'Heart disease':
			return 503.5895543373704
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['children'] == 0:
			return -288.23386024554685
		elif tree_dict['children'] == 2:
			return -80.97308471762412
		elif tree_dict['children'] == 1:
			return -190.54455745878428
		elif tree_dict['children'] == 5:
			return 238.21451630359226
		elif tree_dict['children'] == 3:
			return 61.13905866969869
		elif tree_dict['children'] == 4:
			return 118.80611304769053
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['medical_history'] == 'Diabetes':
			return -276.00597982350206
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -377.1473594304195
		elif tree_dict['medical_history'] == 'Heart disease':
			return 53.667424199026144

def tree_77(tree_dict):
	if tree_dict['gender'] == 'male':
		if tree_dict['occupation'] == 'White collar':
			return 414.26021160403394
		elif tree_dict['occupation'] == 'Blue collar':
			return 278.09709433527627
		elif tree_dict['occupation'] == 'Student':
			return 78.98219858057273
		elif tree_dict['occupation'] == 'Unemployed':
			return -56.90194844407538
	elif tree_dict['gender'] == 'female':
		if tree_dict['bmi'] == '35 - 40':
			return -110.84702436766709
		elif tree_dict['bmi'] == '25 - 30':
			return -310.0691673178793
		elif tree_dict['bmi'] == '40 - 54':
			return 46.86367940390872
		elif tree_dict['bmi'] == '30 - 35':
			return -216.91804777792467
		elif tree_dict['bmi'] == '18.5 - 25':
			return -419.3759451694559
		elif tree_dict['bmi'] == '< 18.5':
			return -407.78760608069996

def tree_78(tree_dict):
	if tree_dict['family_medical_history'] == 'High blood pressure':
		if tree_dict['age'] == '26-41':
			return -272.4174237591308
		elif tree_dict['age'] == '41-56':
			return -82.10790888056795
		elif tree_dict['age'] == '>56':
			return 86.19163428764756
		elif tree_dict['age'] == '18-26':
			return -454.33844474742807
	elif tree_dict['family_medical_history'] == 'Heart disease':
		if tree_dict['bmi'] == '35 - 40':
			return 354.7484296291765
		elif tree_dict['bmi'] == '25 - 30':
			return 102.41549866518326
		elif tree_dict['bmi'] == '40 - 54':
			return 451.6909781723281
		elif tree_dict['bmi'] == '30 - 35':
			return 192.64195931472446
		elif tree_dict['bmi'] == '18.5 - 25':
			return -13.465038626354502
		elif tree_dict['bmi'] == '< 18.5':
			return -214.78176863917955
	elif tree_dict['family_medical_history'] == 'Diabetes':
		if tree_dict['medical_history'] == 'Diabetes':
			return -150.11416914775413
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -253.52375068901821
		elif tree_dict['medical_history'] == 'Heart disease':
			return 195.25609539823935

def tree_79(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 80.34445992345853
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 501.94869623927946
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 197.7324545241139
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['region'] == 'southwest':
			return -269.7840836823157
		elif tree_dict['region'] == 'southeast':
			return -68.98170977882837
		elif tree_dict['region'] == 'northwest':
			return -196.10047360334138
		elif tree_dict['region'] == 'northeast':
			return 161.62904718675196
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['gender'] == 'male':
			return 202.6434483189629
		elif tree_dict['gender'] == 'female':
			return -132.7444858345361
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['occupation'] == 'White collar':
			return 32.73328214688122
		elif tree_dict['occupation'] == 'Blue collar':
			return -66.38750337579381
		elif tree_dict['occupation'] == 'Student':
			return -285.3332262548055
		elif tree_dict['occupation'] == 'Unemployed':
			return -428.1224742206147

def tree_80(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['children'] == 0:
			return -80.6312698938395
		elif tree_dict['children'] == 2:
			return 130.35368808989796
		elif tree_dict['children'] == 1:
			return 15.887995798170763
		elif tree_dict['children'] == 5:
			return 426.8826302694624
		elif tree_dict['children'] == 3:
			return 216.87598735587378
		elif tree_dict['children'] == 4:
			return 309.0490372733649
	elif tree_dict['smoker'] == 'no':
		if tree_dict['children'] == 0:
			return -403.82940952676563
		elif tree_dict['children'] == 2:
			return -220.40177596426557
		elif tree_dict['children'] == 1:
			return -308.1880267761253
		elif tree_dict['children'] == 5:
			return 77.82732643747505
		elif tree_dict['children'] == 3:
			return -117.09129148590803
		elif tree_dict['children'] == 4:
			return -31.773039746185344

def tree_81(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['bmi'] == '35 - 40':
			return 290.36357692521005
		elif tree_dict['bmi'] == '25 - 30':
			return 132.044806498637
		elif tree_dict['bmi'] == '40 - 54':
			return 400.7234904392272
		elif tree_dict['bmi'] == '30 - 35':
			return 215.64816471817653
		elif tree_dict['bmi'] == '18.5 - 25':
			return -41.86328800151449
		elif tree_dict['bmi'] == '< 18.5':
			return -172.45689325132173
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['age'] == '26-41':
			return -136.11632157665366
		elif tree_dict['age'] == '41-56':
			return 57.15907155701741
		elif tree_dict['age'] == '>56':
			return 230.06666085494757
		elif tree_dict['age'] == '18-26':
			return -288.0680392829696
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['occupation'] == 'White collar':
			return 31.630212498953856
		elif tree_dict['occupation'] == 'Blue collar':
			return -87.55608624500935
		elif tree_dict['occupation'] == 'Student':
			return -260.28602824538876
		elif tree_dict['occupation'] == 'Unemployed':
			return -385.168565558136

def tree_82(tree_dict):
	if tree_dict['region'] == 'southwest':
		if tree_dict['children'] == 0:
			return -394.53005481602025
		elif tree_dict['children'] == 2:
			return -205.79850786127042
		elif tree_dict['children'] == 1:
			return -264.9112340282732
		elif tree_dict['children'] == 5:
			return 65.48723150442491
		elif tree_dict['children'] == 3:
			return -81.91293889305463
		elif tree_dict['children'] == 4:
			return 5.041841670754091
	elif tree_dict['region'] == 'southeast':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -164.13457825081866
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 225.5729372321473
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -69.35928698833875
	elif tree_dict['region'] == 'northwest':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -256.34412311106786
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 113.86015541162347
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -182.0599819818284
	elif tree_dict['region'] == 'northeast':
		if tree_dict['age'] == '26-41':
			return 159.59409681054316
		elif tree_dict['age'] == '41-56':
			return 336.5983556972929
		elif tree_dict['age'] == '>56':
			return 501.4366712356981
		elif tree_dict['age'] == '18-26':
			return 0.40691680144857834

def tree_83(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 164.82857303868118
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -145.21704326255633
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -30.327625947175356
		elif tree_dict['exercise_frequency'] == 'Never':
			return -249.96424643513558
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['gender'] == 'male':
			return 8.663169997217176
		elif tree_dict['gender'] == 'female':
			return -312.43789701213126
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['gender'] == 'male':
			return 387.01249070766363
		elif tree_dict['gender'] == 'female':
			return 57.78483104257908

def tree_84(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 33.74032788663397
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 441.73702301943985
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 140.79937439663723
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['bmi'] == '35 - 40':
			return 166.44431950946085
		elif tree_dict['bmi'] == '25 - 30':
			return -9.475725573450045
		elif tree_dict['bmi'] == '40 - 54':
			return 275.70594539800254
		elif tree_dict['bmi'] == '30 - 35':
			return 78.99659884388181
		elif tree_dict['bmi'] == '18.5 - 25':
			return -149.79860758776036
		elif tree_dict['bmi'] == '< 18.5':
			return -264.7731733338288
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['age'] == '26-41':
			return -190.50026645723528
		elif tree_dict['age'] == '41-56':
			return -33.29260439758667
		elif tree_dict['age'] == '>56':
			return 135.55347167571142
		elif tree_dict['age'] == '18-26':
			return -323.1764960072409
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['region'] == 'southwest':
			return -314.5845965893111
		elif tree_dict['region'] == 'southeast':
			return -204.91814046745242
		elif tree_dict['region'] == 'northwest':
			return -297.0382586345548
		elif tree_dict['region'] == 'northeast':
			return 51.85412836708324

def tree_85(tree_dict):
	if tree_dict['bmi'] == '35 - 40':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -101.24249160193723
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 288.65345284473676
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 14.372479175705543
	elif tree_dict['bmi'] == '25 - 30':
		if tree_dict['age'] == '26-41':
			return -219.68573313802673
		elif tree_dict['age'] == '41-56':
			return -8.411524305717295
		elif tree_dict['age'] == '>56':
			return 114.06142901900517
		elif tree_dict['age'] == '18-26':
			return -338.0587406451586
	elif tree_dict['bmi'] == '40 - 54':
		if tree_dict['smoker'] == 'yes':
			return 325.95008853786777
		elif tree_dict['smoker'] == 'no':
			return 18.440521141687583
	elif tree_dict['bmi'] == '30 - 35':
		if tree_dict['coverage_level'] == 'Premium':
			return 196.14696332924208
		elif tree_dict['coverage_level'] == 'Standard':
			return -63.441998958520884
		elif tree_dict['coverage_level'] == 'Basic':
			return -180.8877961319092
	elif tree_dict['bmi'] == '18.5 - 25':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 27.56353135848227
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -301.783719610517
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -146.5145814818893
		elif tree_dict['exercise_frequency'] == 'Never':
			return -395.282322490408
	elif tree_dict['bmi'] == '< 18.5':
		if tree_dict['age'] == '26-41':
			return -278.2949872878555
		elif tree_dict['age'] == '41-56':
			return -253.48738227830285
		elif tree_dict['age'] == '>56':
			return -67.51240359166677
		elif tree_dict['age'] == '18-26':
			return -604.7890635185445

def tree_86(tree_dict):
	if tree_dict['gender'] == 'male':
		if tree_dict['coverage_level'] == 'Premium':
			return 345.85835657016816
		elif tree_dict['coverage_level'] == 'Standard':
			return 124.43199242824373
		elif tree_dict['coverage_level'] == 'Basic':
			return -26.750105550727405
	elif tree_dict['gender'] == 'female':
		if tree_dict['children'] == 0:
			return -361.25729182504807
		elif tree_dict['children'] == 2:
			return -188.29784045168083
		elif tree_dict['children'] == 1:
			return -281.06172425607383
		elif tree_dict['children'] == 5:
			return 69.51294000082729
		elif tree_dict['children'] == 3:
			return -93.41167043343303
		elif tree_dict['children'] == 4:
			return -13.75870687605224

def tree_87(tree_dict):
	if tree_dict['exercise_frequency'] == 'Frequently':
		if tree_dict['region'] == 'southwest':
			return 81.58563641833503
		elif tree_dict['region'] == 'southeast':
			return 214.60161055789112
		elif tree_dict['region'] == 'northwest':
			return 114.66427410591854
		elif tree_dict['region'] == 'northeast':
			return 461.2355279012739
	elif tree_dict['exercise_frequency'] == 'Rarely':
		if tree_dict['smoker'] == 'yes':
			return 65.36864297621264
		elif tree_dict['smoker'] == 'no':
			return -213.77571921781916
	elif tree_dict['exercise_frequency'] == 'Occasionally':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -104.2957795649857
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 232.53450021983497
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -30.213589989520976
	elif tree_dict['exercise_frequency'] == 'Never':
		if tree_dict['region'] == 'southwest':
			return -289.9709825982679
		elif tree_dict['region'] == 'southeast':
			return -174.80485555685502
		elif tree_dict['region'] == 'northwest':
			return -283.56881760957924
		elif tree_dict['region'] == 'northeast':
			return 86.43884112685276

def tree_88(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['children'] == 0:
			return -301.1728832336718
		elif tree_dict['children'] == 2:
			return -89.689306854259
		elif tree_dict['children'] == 1:
			return -147.6966920014819
		elif tree_dict['children'] == 5:
			return 145.12982715704283
		elif tree_dict['children'] == 3:
			return -44.493880379035716
		elif tree_dict['children'] == 4:
			return 87.42423968274592
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['smoker'] == 'yes':
			return 17.32452353514227
		elif tree_dict['smoker'] == 'no':
			return -277.91608170349036
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['age'] == '26-41':
			return 101.18660603902687
		elif tree_dict['age'] == '41-56':
			return 276.7170510925896
		elif tree_dict['age'] == '>56':
			return 392.1710082184817
		elif tree_dict['age'] == '18-26':
			return -35.67669403895734

def tree_89(tree_dict):
	if tree_dict['occupation'] == 'White collar':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 33.80010049982036
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 390.7778786078139
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 125.89513140426688
	elif tree_dict['occupation'] == 'Blue collar':
		if tree_dict['medical_history'] == 'Diabetes':
			return 33.59841834271872
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -65.79670017575741
		elif tree_dict['medical_history'] == 'Heart disease':
			return 284.82041494428177
	elif tree_dict['occupation'] == 'Student':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -219.70903870489957
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 106.3419514261937
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return -156.9517576455947
	elif tree_dict['occupation'] == 'Unemployed':
		if tree_dict['coverage_level'] == 'Premium':
			return 13.623668480833487
		elif tree_dict['coverage_level'] == 'Standard':
			return -182.68485011426026
		elif tree_dict['coverage_level'] == 'Basic':
			return -317.73429834321075

def tree_90(tree_dict):
	if tree_dict['age'] == '26-41':
		if tree_dict['bmi'] == '35 - 40':
			return -39.92922367566732
		elif tree_dict['bmi'] == '25 - 30':
			return -195.40209060972217
		elif tree_dict['bmi'] == '40 - 54':
			return 86.02016128060399
		elif tree_dict['bmi'] == '30 - 35':
			return -100.41981543696795
		elif tree_dict['bmi'] == '18.5 - 25':
			return -290.7816461467485
		elif tree_dict['bmi'] == '< 18.5':
			return -253.0727853439256
	elif tree_dict['age'] == '41-56':
		if tree_dict['smoker'] == 'yes':
			return 213.9228055672667
		elif tree_dict['smoker'] == 'no':
			return -70.26407858467931
	elif tree_dict['age'] == '>56':
		if tree_dict['children'] == 0:
			return -46.16161097478658
		elif tree_dict['children'] == 2:
			return 138.89272292342952
		elif tree_dict['children'] == 1:
			return 53.46141920552939
		elif tree_dict['children'] == 5:
			return 399.21698957828244
		elif tree_dict['children'] == 3:
			return 234.09108458155478
		elif tree_dict['children'] == 4:
			return 303.4135222617496
	elif tree_dict['age'] == '18-26':
		if tree_dict['children'] == 0:
			return -448.0797994603238
		elif tree_dict['children'] == 2:
			return -229.4049452358937
		elif tree_dict['children'] == 1:
			return -295.08785053101644
		elif tree_dict['children'] == 5:
			return -5.544901389787049
		elif tree_dict['children'] == 3:
			return -198.04003603847937
		elif tree_dict['children'] == 4:
			return -64.44949622330692

def tree_91(tree_dict):
	if tree_dict['region'] == 'southwest':
		if tree_dict['gender'] == 'male':
			return 17.49353602291422
		elif tree_dict['gender'] == 'female':
			return -266.1257887966522
	elif tree_dict['region'] == 'southeast':
		if tree_dict['coverage_level'] == 'Premium':
			return 171.38428152736745
		elif tree_dict['coverage_level'] == 'Standard':
			return 16.38903340897926
		elif tree_dict['coverage_level'] == 'Basic':
			return -190.6211304673681
	elif tree_dict['region'] == 'northwest':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 100.60323068453967
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -153.17991943598236
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -41.394626455744145
		elif tree_dict['exercise_frequency'] == 'Never':
			return -254.09805640261638
	elif tree_dict['region'] == 'northeast':
		if tree_dict['bmi'] == '35 - 40':
			return 296.6647613814413
		elif tree_dict['bmi'] == '25 - 30':
			return 94.50159278935811
		elif tree_dict['bmi'] == '40 - 54':
			return 376.40109124359003
		elif tree_dict['bmi'] == '30 - 35':
			return 178.44560708383878
		elif tree_dict['bmi'] == '18.5 - 25':
			return 32.394033320156915
		elif tree_dict['bmi'] == '< 18.5':
			return -46.74806604695028

def tree_92(tree_dict):
	if tree_dict['family_medical_history'] == 'High blood pressure':
		if tree_dict['smoker'] == 'yes':
			return 19.971955118751882
		elif tree_dict['smoker'] == 'no':
			return -267.59750862811046
	elif tree_dict['family_medical_history'] == 'Heart disease':
		if tree_dict['smoker'] == 'yes':
			return 318.4459870533221
		elif tree_dict['smoker'] == 'no':
			return 24.740883189257815
	elif tree_dict['family_medical_history'] == 'Diabetes':
		if tree_dict['gender'] == 'male':
			return 84.59591443181395
		elif tree_dict['gender'] == 'female':
			return -202.8091186727247

def tree_93(tree_dict):
	if tree_dict['coverage_level'] == 'Premium':
		if tree_dict['occupation'] == 'White collar':
			return 348.4813386007885
		elif tree_dict['occupation'] == 'Blue collar':
			return 261.99715301089776
		elif tree_dict['occupation'] == 'Student':
			return 60.418157270322524
		elif tree_dict['occupation'] == 'Unemployed':
			return 9.172267419715876
	elif tree_dict['coverage_level'] == 'Standard':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 189.42625043572107
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -88.20623089120657
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return 7.854902571721685
		elif tree_dict['exercise_frequency'] == 'Never':
			return -178.62640064501113
	elif tree_dict['coverage_level'] == 'Basic':
		if tree_dict['children'] == 0:
			return -325.89984137516655
		elif tree_dict['children'] == 2:
			return -207.0139928844044
		elif tree_dict['children'] == 1:
			return -263.11784948777296
		elif tree_dict['children'] == 5:
			return 39.59448717454072
		elif tree_dict['children'] == 3:
			return -96.24644767913463
		elif tree_dict['children'] == 4:
			return -24.712445673502724

def tree_94(tree_dict):
	if tree_dict['bmi'] == '35 - 40':
		if tree_dict['age'] == '26-41':
			return -38.12840641363645
		elif tree_dict['age'] == '41-56':
			return 118.01016986612498
		elif tree_dict['age'] == '>56':
			return 253.70076580690684
		elif tree_dict['age'] == '18-26':
			return -179.86496964756094
	elif tree_dict['bmi'] == '25 - 30':
		if tree_dict['children'] == 0:
			return -248.64775220758318
		elif tree_dict['children'] == 2:
			return -157.7189373469878
		elif tree_dict['children'] == 1:
			return -225.10770884610787
		elif tree_dict['children'] == 5:
			return 134.09241825845166
		elif tree_dict['children'] == 3:
			return -32.75441678281132
		elif tree_dict['children'] == 4:
			return -10.184662572630671
	elif tree_dict['bmi'] == '40 - 54':
		if tree_dict['medical_history'] == 'Diabetes':
			return 90.61443202643134
		elif tree_dict['medical_history'] == 'High blood pressure':
			return 29.09230917344922
		elif tree_dict['medical_history'] == 'Heart disease':
			return 334.8134970565542
	elif tree_dict['bmi'] == '30 - 35':
		if tree_dict['occupation'] == 'White collar':
			return 154.32905854242657
		elif tree_dict['occupation'] == 'Blue collar':
			return 69.3750501435513
		elif tree_dict['occupation'] == 'Student':
			return -99.6928694214285
		elif tree_dict['occupation'] == 'Unemployed':
			return -166.06387720916038
	elif tree_dict['bmi'] == '18.5 - 25':
		if tree_dict['age'] == '26-41':
			return -259.2955853821907
		elif tree_dict['age'] == '41-56':
			return -102.72479210946389
		elif tree_dict['age'] == '>56':
			return -9.81437502204054
		elif tree_dict['age'] == '18-26':
			return -375.7411341918807
	elif tree_dict['bmi'] == '< 18.5':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return -58.96209789701167
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -317.3280737165763
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -212.09101510337365
		elif tree_dict['exercise_frequency'] == 'Never':
			return -400.914129990851

def tree_95(tree_dict):
	if tree_dict['gender'] == 'male':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return -9.26652275350943
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 302.9012787278183
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 75.40711124927873
	elif tree_dict['gender'] == 'female':
		if tree_dict['region'] == 'southwest':
			return -234.0689603230681
		elif tree_dict['region'] == 'southeast':
			return -133.6111885740437
		elif tree_dict['region'] == 'northwest':
			return -207.10588876903375
		elif tree_dict['region'] == 'northeast':
			return 88.72956244681225

def tree_96(tree_dict):
	if tree_dict['children'] == 0:
		if tree_dict['medical_history'] == 'Diabetes':
			return -253.00865394949722
		elif tree_dict['medical_history'] == 'High blood pressure':
			return -289.1155246444772
		elif tree_dict['medical_history'] == 'Heart disease':
			return 7.4370167907040114
	elif tree_dict['children'] == 2:
		if tree_dict['coverage_level'] == 'Premium':
			return 138.31736301708173
		elif tree_dict['coverage_level'] == 'Standard':
			return -50.68366344962433
		elif tree_dict['coverage_level'] == 'Basic':
			return -186.65241773924402
	elif tree_dict['children'] == 1:
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 99.95221604255978
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -169.91498027533882
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -89.91637901924311
		elif tree_dict['exercise_frequency'] == 'Never':
			return -262.33568857438166
	elif tree_dict['children'] == 5:
		if tree_dict['coverage_level'] == 'Premium':
			return 347.51966263701166
		elif tree_dict['coverage_level'] == 'Standard':
			return 166.92923276878741
		elif tree_dict['coverage_level'] == 'Basic':
			return 31.50137004449548
	elif tree_dict['children'] == 3:
		if tree_dict['age'] == '26-41':
			return -35.80047841313108
		elif tree_dict['age'] == '41-56':
			return 78.15630736764267
		elif tree_dict['age'] == '>56':
			return 202.02287220151214
		elif tree_dict['age'] == '18-26':
			return -170.50103369177384
	elif tree_dict['children'] == 4:
		if tree_dict['occupation'] == 'White collar':
			return 282.961575644952
		elif tree_dict['occupation'] == 'Blue collar':
			return 196.8172274740227
		elif tree_dict['occupation'] == 'Student':
			return 10.63589119684014
		elif tree_dict['occupation'] == 'Unemployed':
			return -45.402852170790595

def tree_97(tree_dict):
	if tree_dict['smoker'] == 'yes':
		if tree_dict['family_medical_history'] == 'High blood pressure':
			return 22.99516047600802
		elif tree_dict['family_medical_history'] == 'Heart disease':
			return 280.18378403683744
		elif tree_dict['family_medical_history'] == 'Diabetes':
			return 39.90442162219221
	elif tree_dict['smoker'] == 'no':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 49.22832933658921
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -169.6114530709476
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -77.7262590200278
		elif tree_dict['exercise_frequency'] == 'Never':
			return -270.76901359625214

def tree_98(tree_dict):
	if tree_dict['medical_history'] == 'Diabetes':
		if tree_dict['occupation'] == 'White collar':
			return 97.77276482055424
		elif tree_dict['occupation'] == 'Blue collar':
			return 25.12299769077919
		elif tree_dict['occupation'] == 'Student':
			return -109.26629980100996
		elif tree_dict['occupation'] == 'Unemployed':
			return -202.8524491316213
	elif tree_dict['medical_history'] == 'High blood pressure':
		if tree_dict['age'] == '26-41':
			return -182.38608088169786
		elif tree_dict['age'] == '41-56':
			return -56.07514083510278
		elif tree_dict['age'] == '>56':
			return 68.47151585456676
		elif tree_dict['age'] == '18-26':
			return -305.08877224282105
	elif tree_dict['medical_history'] == 'Heart disease':
		if tree_dict['coverage_level'] == 'Premium':
			return 321.98367030306787
		elif tree_dict['coverage_level'] == 'Standard':
			return 133.48302583013472
		elif tree_dict['coverage_level'] == 'Basic':
			return 34.3367570385675

def tree_99(tree_dict):
	if tree_dict['bmi'] == '35 - 40':
		if tree_dict['gender'] == 'male':
			return 159.47405008987909
		elif tree_dict['gender'] == 'female':
			return -97.13261270048217
	elif tree_dict['bmi'] == '25 - 30':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 120.98305828494885
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -125.37132778781869
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -61.072639059348894
		elif tree_dict['exercise_frequency'] == 'Never':
			return -228.21178177903198
	elif tree_dict['bmi'] == '40 - 54':
		if tree_dict['occupation'] == 'White collar':
			return 299.0469596180022
		elif tree_dict['occupation'] == 'Blue collar':
			return 188.21216564995385
		elif tree_dict['occupation'] == 'Student':
			return 71.57550500609396
		elif tree_dict['occupation'] == 'Unemployed':
			return -14.569789184554566
	elif tree_dict['bmi'] == '30 - 35':
		if tree_dict['gender'] == 'male':
			return 110.21713010778798
		elif tree_dict['gender'] == 'female':
			return -127.72029394486748
	elif tree_dict['bmi'] == '18.5 - 25':
		if tree_dict['exercise_frequency'] == 'Frequently':
			return 14.611694731675502
		elif tree_dict['exercise_frequency'] == 'Rarely':
			return -227.67208341049434
		elif tree_dict['exercise_frequency'] == 'Occasionally':
			return -109.83974393298759
		elif tree_dict['exercise_frequency'] == 'Never':
			return -297.5570832146455
	elif tree_dict['bmi'] == '< 18.5':
		if tree_dict['age'] == '26-41':
			return -209.8205164876355
		elif tree_dict['age'] == '41-56':
			return -211.71203620460818
		elif tree_dict['age'] == '>56':
			return -58.92659858352167
		elif tree_dict['age'] == '18-26':
			return -464.8727107621332
