from django import forms
from .models import Course, Detailsmodel

class studdetailsform(forms.ModelForm):
    class Meta:
        model = Detailsmodel
        fields = '__all__'
        # fields = (
        # 'firstname','dob','age','gender','phone', 'email','address','dprtmnt','courses','purpose','materialprovides'
        # )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()


         # if 'department' in self.data:
         #     try:
         #         department_id = int(self.data.get('department'))
         #         self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
         #     except (ValueError, TypeError):
         #         pass  # invalid input from the client; ignore and fallback to empty City queryset
         # elif self.instance.pk:
         #     self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
