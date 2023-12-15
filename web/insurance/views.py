from django.shortcuts import render
from base.models import UserX
from . import trees

# Create your views here.

def apply(req):

    userx = UserX.objects.get(user = req.user)

    res = 0

    if req.method == "POST":
        post_data = req.POST

        

        p_data = post_data.copy()

        p_data['smoker'] = ('yes' if post_data["smoker"] == True else 'no') if post_data.get("smoker") else "no"

        if 18 <= int(p_data['age']) < 26:
            p_data['age'] = "18-26"
        elif 26 <= int(p_data['age']) < 41:
            p_data['age'] = "26-41"
        elif 41 <= int(p_data['age']) < 56:
            p_data['age'] = "41-56"
        elif 56 <= int(p_data['age']) <= 64:
            p_data['age'] = "56-64"

        if int(p_data['bmi']) < 18.5:
            p_data['bmi'] = "< 18.5"
        elif 18.5 <= int(p_data['bmi']) < 25:
            p_data['bmi'] = "18.5 - 25"
        elif 25 <= int(p_data['bmi']) < 30:
            p_data['bmi'] = "25 - 30"
        elif 30 <= int(p_data['bmi']) < 35:
            p_data['bmi'] = "30 - 35"
        elif 35 <= int(p_data['bmi']) < 40:
            p_data['bmi'] = "35 - 40"
        elif 40 <= int(p_data['bmi']) <= 54:
            p_data['bmi'] = "40 - 54"

        p_data['children'] = int(p_data['children'])

        print(p_data)
        res = 13270.42

        for i in range(100):

            tree_res = getattr(trees, f"tree_{i}")(p_data)

            print(i, tree_res)
            res += 0.1 * tree_res

    context = {
        'userx': userx,
        'res': res
    }

    return render(req, 'insurance/apply.html', context)
