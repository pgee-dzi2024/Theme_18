from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row


# class SkillWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','','','','','',''])

# class SkillsField(forms.MultiValueField):
# 	widget=SkillWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]} {data_list[3]} {data_list[4]} {data_list[5]} {data_list[6]}'


# class ExpWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class ExpField(forms.MultiValueField):
# 	widget=ExpWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'

# class EduWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class EduField(forms.MultiValueField):
# 	widget=EduWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'


class ContactForm(forms.Form):
    name = forms.CharField(label='Име')  #required=False
    email = forms.EmailField(label='E-mail')
    mobile = forms.CharField(label='Телефон')
    address = forms.CharField(label='Адрес')
    skills_1 = forms.CharField(label='Ключово умение')
    skills_2 = forms.CharField(label='Ключово умение (1)')
    skills_3 = forms.CharField(label='Ключово умение (2)', required=False)
    skills_4 = forms.CharField(label='Ключово умение (3)', required=False)

    experience_1_title = forms.CharField(label='Професионален опит - място')
    experience_1_dur = forms.CharField(label='Професионален опит - период')
    experience_1_desc = forms.CharField(label='Професионален опит - позиция')

    experience_2_title = forms.CharField(required=False, label='Професионален опит - място (1)')
    experience_2_dur = forms.CharField(required=False, label='Професионален опит - период (1)')
    experience_2_desc = forms.CharField(required=False, label='Професионален опит - позиция (1)')

    education_1 = forms.CharField(label='Образование - място')
    education_1_dur = forms.CharField(label='Образование - период')
    education1_score = forms.CharField(label='Образование - степен')

    education_2 = forms.CharField(label='Образование - място (1)')
    education_2_dur = forms.CharField(label='Образование - период (1)')
    education2_score = forms.CharField(label='Образование - степен (1)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_class = ' container justify-content-center '
        # self.helper.label_class = ''
        # self.helper.field_class = 'col-md-6 col-xs-9'
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-5  mb-10'),
                Column('email', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('mobile', css_class='form-group col-md-5  mb-10'),
                Column('address', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('skills_1', css_class='form-group col-md-6  mb-10'),
                Column('skills_2', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('skills_3', css_class='form-group col-md-6  mb-10'),
                Column('skills_4', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('experience_1_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_1_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
            'experience_1_desc',
            Row(
                Column('experience_2_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_2_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
            'experience_2_desc',
            'education_1',
            Row(
                Column('education_1_dur', css_class='form-group col-md-6 mb-10'),
                Column('education1_score', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            'education_2',
            Row(
                Column('education_2_dur', css_class='form-group col-md-6  mb-10'),
                Column('education2_score', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            Submit('submit', 'ГЕНЕРИРАЙ', css_class="btn-success")
        )
