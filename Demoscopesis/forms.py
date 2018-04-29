from django import forms
from django.forms import ModelForm, Textarea
from Demoscopesis.models import Poll

class PollForm(ModelForm):
	class Meta:
		model = Poll
		fields = ('PL_TITLE', 'PL_SHRBODY', 'PL_BODY', 'PL_STARTDT', 'PL_ENDDT', 'PL_CODE', 'POLLCAT')
		widgets = {
			'PL_TITLE' : forms.TextInput(attrs={'type':'text','id':'title','class':'form-control','placeholder':'Title', 'required': True}),
			'PL_SHRBODY' : Textarea(attrs={'id':'shortbody','class':'form-control','rows':'3', 'required': True, 'autofocus':True}),
			'PL_BODY' : Textarea(attrs={'id':'body','class':'form-control','rows':'10', 'required': True, 'autofocus':True}),
			'PL_STARTDT' : forms.TextInput(attrs={'type':'date','id':'startdate','class':'form-control','required': True}),
			'PL_ENDDT' : forms.TextInput(attrs={'type':'date','id':'enddate','class':'form-control','required': True}),
			'PL_CODE' : forms.TextInput(attrs={'type':'text','id':'code','class':'form-control','required': True}),
			'POLLCAT' : forms.TextInput(attrs={'type':'text','id':'code','class':'form-control','required': True}),
		}