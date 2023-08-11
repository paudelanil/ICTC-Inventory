from django import forms
from django.forms import ModelForm
from .models import Item,Room,Floor,Categorie,SubItem
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

def validate_single_word(value):
     if (' ' in value) == True:
        raise ValidationError(
            ('%(value)s contains space '),
            params={'value': value},
        )

class addCategoryForm(forms.Form):
    categoryName = forms.CharField(max_length=40)
    extraField1 = forms.CharField(label='New field 1',max_length=30, required=False)
    extraField2 = forms.CharField(label='New field 2',max_length=30, required=False)
    extraField3 = forms.CharField(label='New field 3',max_length=30, required=False)


class addItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        for field in self.Meta.Notrequired:
            self.fields[field].required = False


    class Meta:
        model = Item
        fields = ['name', 'model', 'cost_per_item', 'room',
                  'date_of_acquire', 'working', 'in_maintenance', 'out_of_order', 'remarks', 'itemSource']
        Notrequired = ['room','model','cost_per_item','remarks']
        labels = {
        "in_maintenance": "Number of Repairable items",
        "out_of_order": "Number of Out-of-order items",
        "working":"Number of working items",
        'itemSource' : "Source of item",
        
        }
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        model = cleaned_data.get('model')

        if name and model:
            if Item.objects.filter(name=name, model=model).exists():
                self.add_error('name', 'An item with this name and model already exists.')
                self.add_error('model', '')
    
        return cleaned_data
  

class verifyItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        for field in self.Meta.Notrequired:
            self.fields[field].required = False


    class Meta:
        model = Item
        #removed name and model field as on form submission creates invalid error due to already existed namd and model.
        fields = [ 'cost_per_item', 'room',
                  'date_of_acquire', 'working', 'in_maintenance', 'out_of_order', 'remarks', 'itemSource']
        Notrequired = ['remarks','room','cost_per_item']
        labels = {
        "in_maintenance": "Number of Repairable items",
        "out_of_order": "Number of Out-of-order items",
        "working":"Number of working items",
        'itemSource' : "Source of item",
        }
class editItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Item
        fields = ['name', 'model', 'cost_per_item', 'room',
                  'date_of_acquire', 'working', 'in_maintenance', 'out_of_order', 'remarks', 'itemSource']
        labels = {
            "in_maintenance": "Number of Repairable items",
            "out_of_order": "Number of Out-of-order items",
            "working": "Number of working items",
            'itemSource': "Source of item",
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        model = cleaned_data.get('model')
        print (name,model)

        if name and model:
            # Get the instance being edited
            instance = self.instance
            print (instance)

            # Check if there's an item with the same name and model, excluding the current instance
            if Item.objects.filter(name=name, model=model).exclude(pk=instance.pk).exists():
                print("exist")
                self.add_error('name', 'An item with this name and model already exists.')
                self.add_error('model', '')

        return cleaned_data

        


    class Meta:
        model = Item
        #removed name and model field as on form submission creates invalid error due to already existed namd and model.
        fields = [ 'category','name','model','cost_per_item', 'room',
                  'date_of_acquire', 'working', 'in_maintenance', 'out_of_order', 'remarks', 'itemSource']
        Notrequired = ['remarks','room','cost_per_item']
        labels = {
        "in_maintenance": "Number of Repairable items",
        "out_of_order": "Number of Out-of-order items",
        "working":"Number of working items",
        'itemSource' : "Source of item",
        }
    def set_existing_item(self, existing_item):
        self.existing_item = existing_item
    


class addExistingForm(forms.Form):
    quantity = forms.IntegerField(required=True,validators=[MinValueValidator(0)])


class allocateForm(ModelForm):
    working = forms.IntegerField(label="Number of working items to allocate",required=False,validators=[MinValueValidator(0)])
    out_of_order = forms.IntegerField(label="Number of out of order items to allocate",required=False,validators=[MinValueValidator(0)])
    in_maintenance = forms.IntegerField(label="Number of repairable items to allocate",required=False,validators=[MinValueValidator(0)])

    class Meta:
        model = Item
        fields = ['room']

class addRoomForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.Meta.Notrequired:
            self.fields[field].required = False
    class Meta:
        model = Room
        fields = '__all__'
        Notrequired = ['room_name']

class addFloorForm(ModelForm):
    class Meta:
        model = Floor
        fields = ['floor']

class categoryEditForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ['category_name']

class subItemForm(ModelForm):
    class Meta:
        model = SubItem
        fields = ['name','model','cost_per_item','working','in_maintenance','out_of_order']
        labels = {
        "in_maintenance": "Number of Repairable items",
        "out_of_order": "Number of Out-of-order items",
        "working":"Number of working items",
        
        }
    
    
class editRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class editCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Categorie
        fields = ['category_name']
        