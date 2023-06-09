from django import forms


class Form_courses(forms.Form):
    course = forms.CharField()
    commission = forms.IntegerField()


class Form_students(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()


class Form_teachers(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    profession = forms.CharField(max_length=30)


class Form_assignment(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    course = forms.CharField()
    commission = forms.IntegerField()
    assignment_date = forms.DateField(input_formats=['%d/%m/%Y'])
    assignment = forms.BooleanField(required=False)
