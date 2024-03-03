from django.shortcuts import render, redirect
from user.models import UserX
from .models import Proposal, Package, InsuranceProfile
from . import predictor_classify
from .predictor import predictor
import pandas as pd
from .preproc import preproc

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
                
        


            # print(p_data)

            
            req.session['insurance_profile'] = {"user": req.user.username, "age": post_data['age'], "sex":post_data['sex'], "region": post_data['region'], "smoker": (True if post_data["smoker"] == "on" else False) if post_data.get("smoker") else False, "children": post_data['children'], "occupation": post_data['occupation'], "bmi": post_data['bmi'], "medical_history": post_data['medical_history'], "family_medical_history": post_data['family_medical_history']}


            df = pd.DataFrame(preproc(post_data), index=[0])

            p = predictor(dff=df,est=50,l_r=0.55, mean_y=14401.838215521071)

            p_B = predictor_classify.predictor_BASIC(df,0.1,BRONZE_LOG_ODDS,14)
            p_G = predictor_classify.predictor_STANDARD(df,0.1,GOLD_LOG_ODDS,14)
            p_P = predictor_classify.predictor_PREMIUM(df,0.1,PLATNIUM_LOG_ODS,14)



            pred_pack_info = [("BASIC", p_B.loc[0,"Prob"]), ("STANDARD", p_G.loc[0,"Prob"]), ("PREMIUM", p_P.loc[0,"Prob"])]

            max_prob=0
            pred_pack = "BASIC"
            for pack, prob in pred_pack_info:
                if prob > max_prob:
                    pred_pack = pack
                    max_prob = prob

            print(max_prob)
            print(pred_pack)
            print(p.loc[0, "Predicted"])

            predd_package = Package.objects.get(package_name=pred_pack)

            packages = Package.objects.all()

            



            
            context = {
                'userx': userx,
                'predicted_price': p.loc[0, "Predicted"],
                'predicted_package': predd_package,
                'predicted_package_prob': max_prob,
                'packages': packages,
                'basic_price': p.loc[0, "Predicted"] - p.loc[0, "Predicted"] * 0.2,
                'prem_price': p.loc[0, "Predicted"] + p.loc[0, "Predicted"] * 0.2,

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

                    return redirect("userproposals")

                    
                    


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