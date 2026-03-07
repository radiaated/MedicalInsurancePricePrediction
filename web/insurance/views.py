from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Proposal, Package
from .forms import InsuranceProfileForm

import pickle

# Views for insurance application and user proposals


class CustomUnpickler(pickle.Unpickler):
    """
    Custom unpickler to safely load machine learning models
    and encoders from pickle files.
    """

    def find_class(self, module, name):
        """Map specific class names to local imports to allow unpickling."""
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
    """
    Handles insurance application form.
    On first submit, calculates predicted charges for packages.
    On 'Submit proposal', saves proposal linked to user and package.
    """

    if (
        request.session.get("insurance_profile")
        and request.session.get("predicted_package")
        and request.session.get("predicted_amt")
    ):
        package = Package.objects.get(
            package_name=request.session.get("predicted_package")
        )
        insurance_profile = request.session.get("insurance_profile", {})

        if insurance_profile:
            insurance_profile_form = InsuranceProfileForm(insurance_profile)
            insurance_profile = insurance_profile_form.save(commit=False)
            insurance_profile.user = request.user
            insurance_profile.save()

            proposal = Proposal.objects.create(
                predicted_amt=float(request.session.get("predicted_amt")),
                package=package,
                insurance_profile=insurance_profile,
            )
            if proposal:
                proposal.save()

            request.session.pop("insurance_profile")
            request.session.pop("predicted_package")
            request.session.pop("predicted_amt")

            return redirect("userproposals")

    if request.method == "POST":
        post_data = request.POST

        if post_data["submit"] == "Submit":
            form = InsuranceProfileForm(request.POST)
            if form.is_valid():
                # Save form data to session
                request.session["insurance_profile"] = form.cleaned_data

                # Load encoders and model
                with open("./insurance/stream/encoders_1.pkl", "rb") as file:
                    encoders = CustomUnpickler(file).load()

                with open("./insurance/stream/gb_regression_1.pkl", "rb") as file:
                    gb = CustomUnpickler(file).load()

                # Prepare data for prediction
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

                # Create separate package datasets
                package_basic_data = {**data, "coverage_level": "Basic"}
                package_standard_data = {**data, "coverage_level": "Standard"}
                package_premium_data = {**data, "coverage_level": "Premium"}

                # Encode data
                package_basic_encoded_data = encoders.transform(package_basic_data)
                package_standard_encoded_data = encoders.transform(
                    package_standard_data
                )
                package_premium_encoded_data = encoders.transform(package_premium_data)

                # Predict charges
                package_basic_charge = round(gb.predict(package_basic_encoded_data), 2)
                package_standard_charge = round(
                    gb.predict(package_standard_encoded_data), 2
                )
                package_premium_charge = round(
                    gb.predict(package_premium_encoded_data), 2
                )

                # Load available packages
                packages = Package.objects.all()

                context = {
                    "package_basic_charge": package_basic_charge,
                    "package_standard_charge": package_standard_charge,
                    "package_premium_charge": package_premium_charge,
                    "packages": packages,
                }

                return render(request, "insurance/apply.html", context=context)

        elif post_data["submit"] == "Submit proposal":
            # Save user proposal

            if not request.user.is_authenticated:

                # Get current path or any URL you want to return to after signup
                next_url = request.get_full_path()

                # Construct signup_url URL with redirect query parameter
                signup_url = f"{reverse('signup')}?redirect={next_url}"

                request.session["predicted_package"] = post_data["predicted_package"]
                request.session["predicted_amt"] = post_data["predicted_amt"]

                return redirect(signup_url)

            package = Package.objects.get(package_name=post_data["predicted_package"])
            insurance_profile = request.session.get("insurance_profile", {})

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

                request.session.pop("insurance_profile")

                return redirect("userproposals")

    else:
        form = InsuranceProfileForm()

    context = {"form": form}
    return render(request, "insurance/apply.html", context)


# User-specific proposal views


class UserProposalListView(LoginRequiredMixin, ListView):
    """
    Displays all proposals for the logged-in user.
    """

    model = Proposal
    template_name = "insurance/userproposals.html"
    context_object_name = "proposals"

    def get_queryset(self):
        """Filter proposals for the current user."""
        return super().get_queryset().filter(insurance_profile__user=self.request.user)


class UserProposalDetailView(LoginRequiredMixin, DetailView):
    """
    Displays details of a single user proposal.
    """

    model = Proposal
    template_name = "insurance/userproposalbyid.html"
    context_object_name = "proposal"


class UserProposalDeleteView(LoginRequiredMixin, DeleteView):
    """
    Allows a user to delete their proposal.
    """

    model = Proposal
    success_url = reverse_lazy("userproposals")

    def get(self, request, *args, **kwargs):
        """Delete proposal on GET request and redirect."""
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
