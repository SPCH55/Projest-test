from django import forms
from .models import Equipment
from .models import Field
from .models import News

class PetanqueBallForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'weight']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['name', 'img']  # กำหนดฟิลด์ที่ใช้ในฟอร์ม


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['image', 'title', 'content', 'announcement_date', 'link']
