from django import forms

class JobApplicationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    employment_type = forms.ChoiceField(choices=[
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('contract', 'Contract Work')
    ])
    start_date = forms.DateField()
    available_days = forms.MultipleChoiceField(choices=[
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday')
    ])
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField(widget=forms.Textarea)
    confirmation = forms.BooleanField(label="I certify that the information provided is true and accurate.")