from django import forms

class psycho_form(forms.ModelForm):
    p_email = forms.CharField()
    p_password = forms.CharField()
    p_f_name = forms.CharField()
    p_l_name = forms.CharField()
    p_phone_no = forms.CharField()
    current_job_title = forms.CharField()
    scfhs_no = forms.CharField()
    scfhs_file = forms.FileField()

    
 