from django import forms

class DocumentUploadForm(forms.Form):
	BRANCH = (
        ('CST','CST'),
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('BCA','BCA'),
        ('Aerospace','Aerospace'),
        ('Mechanical','Mechanical'))
	SEMESTER = (
		('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'))
	branch = forms.ChoiceField(label='Branch',widget=forms.Select(attrs={'class':'form-control'}),choices=BRANCH)
	semester = forms.ChoiceField(label='Semester',widget=forms.Select(attrs={'class':'form-control'}),choices=SEMESTER)
	course = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	file_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	my_file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))