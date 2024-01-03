from django.shortcuts import render, redirect
from user.models import UserX
from .models import Proposal, Package, InsuranceProfile
from . import predictor_classify
from .predictor import predictor
import pandas as pd

# Create your views here.

def apply(req):

    userx = UserX.objects.get(user = req.user)


    BRONZE_LOG_ODDS = 0.13721134108089075
    GOLD_LOG_ODDS = 0.3752345518796065
    
    PLATNIUM_LOG_ODS = 1.9279979643224976

    print("yo")
    context = {}
    if req.method == "POST":
        post_data = req.POST

        if post_data["submit"] == "Check":
                
        
            p_data = dict()
            print(post_data)

            

            p_data['smoker'] = ('yes' if post_data["smoker"] == "on" else 'no') if post_data.get("smoker") else "no"


            req.session['insurance_profile'] = {"user": req.user.username, "age": post_data['age'], "sex":post_data['sex'], "region": post_data['region'], "smoker": (True if post_data["smoker"] == "on" else False) if post_data.get("smoker") else False, "children": post_data['children'], "occupation": post_data['occupation'], "bmi": post_data['bmi'], "medical_history": post_data['medical_history'], "family_medical_history": post_data['family_medical_history']}

            if 18 <= int(float(post_data['age'])) < 26:
                p_data['age'] = "18-26"
            elif 26 <= int(float(post_data['age'])) < 41:
                p_data['age'] = "26-41"
            elif 41 <= int(float(post_data['age'])) < 56:
                p_data['age'] = "41-56"
            elif 56 <= int(float(post_data['age'])) <= 64:
                p_data['age'] = "56-64"

            if int(float(post_data['bmi'])) < 18.5:
                p_data['bmi'] = "< 18.5"
            elif 18.5 <= int(float(post_data['bmi'])) < 25:
                p_data['bmi'] = "18.5 - 25"
            elif 25 <= int(float(post_data['bmi'])) < 30:
                p_data['bmi'] = "25 - 30"
            elif 30 <= int(float(post_data['bmi'])) < 35:
                p_data['bmi'] = "30 - 35"
            elif 35 <= int(float(post_data['bmi'])) < 40:
                p_data['bmi'] = "35 - 40"
            elif 40 <= int(float(post_data['bmi'])) <= 54:
                p_data['bmi'] = "40 - 54"

            p_data['children'] = int(float(post_data['children']))
            p_data['sex'] = post_data['sex']
            p_data['region'] = post_data['region']
            p_data['occupation'] = post_data['occupation']
            p_data['medical_history'] = post_data['medical_history']
            p_data['family_medical_history'] = post_data['family_medical_history']

            # print(p_data)

            res = 13270.42

            df = pd.DataFrame(p_data, index=[0])

            p = predictor(dff=df,est=100,l_r=0.1, mean_y=14425.105596351208)

            p_B = predictor_classify.predictor_Bronze(df,0.1,BRONZE_LOG_ODDS,14)
            p_G = predictor_classify.predictor_Gold(df,0.1,GOLD_LOG_ODDS,14)
            p_P = predictor_classify.predictor_Platinum(df,0.1,PLATNIUM_LOG_ODS,14)

            print("Bronze", p_B)
            print("Gold", p_G)
            print("Platnium", p_P)

            pred_pack_info = [("BRONZE", p_B.loc[0,"Prob"]), ("GOLD", p_G.loc[0,"Prob"]), ("PLATINUM", p_P.loc[0,"Prob"])]

            max_prob=0
            pred_pack = "BRONZE"
            for pack, prob in pred_pack_info:
                if prob > max_prob:
                    pred_pack = pack
                    max_prob = prob

            print(max_prob)
            print(pred_pack)
            print(p.loc[0, "Predicted"])
            
            context = {
                'userx': userx,
                'predicted_price': p.loc[0, "Predicted"],
                'predicted_package': pred_pack,
                'predicted_package_prob': max_prob,
            }

            
            
        if post_data["submit"] == "Submit proposal":

                package = Package.objects.get(package_name=post_data["predicted_package"])

                session_data = req.session.get('insurance_profile', {})

                print(session_data)

                insurance_profile = InsuranceProfile.objects.create(user=req.user, age=session_data['age'], sex=session_data['sex'], region=session_data['region'], smoker=session_data['smoker'], children=session_data['children'], occupation=session_data['occupation'], bmi=session_data['bmi'], medical_history=session_data['medical_history'], family_medical_history=session_data['family_medical_history'])
                
                if insurance_profile:
    
                    proposal = Proposal.objects.create(
                        userx=UserX.objects.get(user=req.user),
                        predicted_amt=float(post_data["predicted_amt"]),
                        package=package,
                        insurance_profile=insurance_profile
                    )

                    if proposal:
                        proposal.save()
                    


    context = { **context,
        'userx': userx,       
    }

    return render(req, 'insurance/apply.html', context)


def userproposals(request):


    proposals = Proposal.objects.filter(userx__user=request.user)

    for p in proposals:
        print(p.predicted_amt)

    context={
        "proposals": proposals
    }

    return render(request, "insurance/userproposals.html", context)


def delete_proposal(request, id):


    proposal = Proposal.objects.get(userx__user=request.user, id=id)

    proposal.delete()


    return redirect("userproposals")




def userproposalbyid(req, id):

    if req.method == 'GET':
        proposal = Proposal.objects.get(id=id, userx__user=req.user)
    elif req.method == 'POST':
        pass


    context = {
        'proposal': proposal
    }

    return render(req, 'insurance/userproposalbyid.html', context)