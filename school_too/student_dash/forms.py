from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ChurchLeader, Stats, Filter, Report, FinancialReport

class SignUpForm(UserCreationForm):

    class Meta:
        model = ChurchLeader
        fields = ['email','username','position', 'church_name','cellphone','password1','password2']


class StatsForm(forms.ModelForm):

    class Meta:

        model = Stats
        fields = ('church_name','women','men','youth_g1','youth_g2','children_g1',
                    'children_g2','children_g3','ordained_ministers','licensed_ministers','mission_workers')


class FilterForm(forms.ModelForm):

    class Meta:

        model = Filter
        fields = '__all__'


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('church_name','Pastors_report','pastor_activies','mens_ministry_report','Mens_activities',
        'womens_ministry_report','Womens_activities',
        'youth_ministry_report','youth_activities','childrens_ministry_report','children_activities',)


class FinancialForm(forms.ModelForm):

    class Meta:
        model = FinancialReport
        fields = ('church_name','tithe_budgeted','tithe_actual','offering_budgeted','offering_actual',
                   'other_income','salaries_budgeted','salaries_actual','housing_allowance_budgeted',
                    'housing_allowance_actual','pension_plan_budgeted','pension_plan_actual','clergy_continuing_Education_budgeted',
                    'clergy_continuing_Education_actual','travel_allowance_budgeted','travel_allowance_actual','office_supplies_budgeted',
                    'office_supplies_actual','worship_supplies_budgeted','worship_supplies_actual','cleaning_and_maintenance_budgeted',
                    'cleaning_and_maintenance_actual','taxes_budgeted','taxes_actual','insurance_budgeted','insurance_actual','utilities_budgeted',
                    'utilities_actual','telephone_budgeted','telephone_actual','capital_expenses_budgeted','capital_expenses_actual','debt_retirement_budgeted',
                    'debt_retirement_actual','other_expenses')