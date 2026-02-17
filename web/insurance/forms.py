from django.forms import ModelForm

from .models import InsuranceProfile


class InsuranceProfileForm(ModelForm):

    class Meta:

        model = InsuranceProfile
        fields = [
            "age",
            "sex",
            "region",
            "smoker",
            "children",
            "occupation",
            "bmi",
            "medical_history",
            "family_medical_history",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["age"].help_text = "(18 - 64)"
        self.fields["children"].help_text = "(0 - 5)"
        self.fields["age"].initial = None
        self.fields["bmi"].initial = None
        self.fields["children"].initial = None
