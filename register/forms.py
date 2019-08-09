from django import forms
from .models import Building

class BuildingPost(forms.ModelForm):
    class Meta:
        model=Building
        fields=['room_name','tele_num','address','room_img']

        