from django.forms import ModelForm
from student.models import Project
class ProjectReg(ModelForm):
    required_css_class="required" 
class Meta:
    model=Project
    fields=['studentname','ptopic','plangauges','pduration']