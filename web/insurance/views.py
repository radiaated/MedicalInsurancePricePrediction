from django.shortcuts import render, redirect
from user.models import UserX
from .models import Proposal, Package, InsuranceProfile
import pandas as pd
from .forms import InsuranceProfileForm
import pickle
import math
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy


# Create your views here.


class CustomUnpickler(pickle.Unpickler):

    def find_class(self, module, name):

        from insurance.stream.modules import (
            GradientBoosting,
            EncoderPipeline,
            CategoricalLabelEncoder,
            DiscretizationEncoder,
            DecisionTree,
            DecisionNode,
        )

        class_map = {
            "GradientBoosting": GradientBoosting,
            "EncoderPipeline": EncoderPipeline,
            "CategoricalLabelEncoder": CategoricalLabelEncoder,
            "DiscretizationEncoder": DiscretizationEncoder,
            "DecisionTree": DecisionTree,
            "DecisionNode": DecisionNode,
        }

        if name in class_map:
            return class_map[name]
        else:
            return super().find_class(module, name)


def apply(request):

    if request.method == "POST":
        post_data = request.POST

        if post_data["submit"] == "Submit":

            form = InsuranceProfileForm(request.POST)

            if form.is_valid():

                request.session["insurance_profile"] = form.cleaned_data

                with open("./insurance/stream/encoders_1.pkl", "rb") as file:

                    encoders = CustomUnpickler(file).load()

                with open("./insurance/stream/gb_regression_1.pkl", "rb") as file:

                    gb = CustomUnpickler(file).load()

                data = {
                    "age": form.cleaned_data["age"],
                    "gender": form.cleaned_data["gender"],
                    "region": form.cleaned_data["region"],
                    "smoker": "yes" if form.cleaned_data["smoker"] else "no",
                    "children": form.cleaned_data["children"],
                    "occupation": form.cleaned_data["occupation"],
                    "bmi": form.cleaned_data["bmi"],
                    "medical_history": form.cleaned_data["medical_history"],
                    "family_medical_history": form.cleaned_data[
                        "family_medical_history"
                    ],
                    "exercise_frequency": form.cleaned_data["exercise_frequency"],
                }

                package_basic_data = {**data, "coverage_level": "Basic"}
                package_standard_data = {**data, "coverage_level": "Standard"}
                package_premium_data = {**data, "coverage_level": "Premium"}

                package_basic_encoded_data = encoders.transform(package_basic_data)
                package_standard_encoded_data = encoders.transform(
                    package_standard_data
                )
                package_premium_encoded_data = encoders.transform(package_premium_data)

                package_basic_charge = round(gb.predict(package_basic_encoded_data), 2)
                package_standard_charge = round(
                    gb.predict(package_standard_encoded_data), 2
                )
                package_premium_charge = round(
                    gb.predict(package_premium_encoded_data), 2
                )

                packages = Package.objects.all()

                context = {
                    "package_basic_charge": package_basic_charge,
                    "package_standard_charge": package_standard_charge,
                    "package_premium_charge": package_premium_charge,
                    "packages": packages,
                }

                return render(request, "insurance/apply.html", context=context)

        elif post_data["submit"] == "Submit proposal":

            package = Package.objects.get(package_name=post_data["predicted_package"])

            insurance_profile = request.session.get("insurance_profile", {})

            # insurance_profile

            if insurance_profile:

                insurance_profile_form = InsuranceProfileForm(insurance_profile)

                insurance_profile = insurance_profile_form.save(commit=False)

                insurance_profile.user = request.user

                insurance_profile.save()

                proposal = Proposal.objects.create(
                    predicted_amt=float(post_data["predicted_amt"]),
                    package=package,
                    insurance_profile=insurance_profile,
                )

                if proposal:
                    proposal.save()

                return redirect("userproposals")

    else:

        form = InsuranceProfileForm()

    context = {"form": form}

    return render(request, "insurance/apply.html", context)


class UserProposalListView(ListView):
    model = Proposal
    template_name = "insurance/userproposals.html"
    context_object_name = "proposals"


class UserProposalDeleteView(DeleteView):
    model = Proposal
    success_url = reverse_lazy("userproposals")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


class UserProposalDetailView(DetailView):
    model = Proposal
    template_name = "insurance/userproposalbyid.html"
    context_object_name = "proposal"
