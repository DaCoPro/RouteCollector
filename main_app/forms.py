from django.forms import ModelForm
from .models import Send

class SendForm(ModelForm):
  class Meta:
    model = Send
    fields = ['date', 'method', 'info']