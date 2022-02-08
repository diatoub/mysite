from django import forms
from django.conf import settings


class PersonForm(forms.Form):
    name = forms.CharField(
        required = True,
        max_length = 200,
        strip = True,
        min_length = 2,
        widget = forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )

    age = forms.CharField(
        required = True,
        max_length = 200,
        strip = True,
        min_length = 2,
        widget = forms.NumberInput(
            attrs={
                'type': 'number'
            }
        )
    )

    sexe = forms.ChoiceField(
        required = True,
        choices = [(x, y) for (x, y) in settings.SEXES ],
        widget = forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )

    country = forms.ChoiceField(
        required = True,
        choices = [(x, y) for (x, y) in settings.COUNTRIES ],
        widget = forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )


    # class BoutikForm(forms.Form):
    #   name = forms.CharField(
    #     required = True,
    #     max_length = 200,
    #     strip = True,
    #     min_length = 2,
    #     widget = forms.TextInput(
    #         attrs={
    #             'type': 'text'
    #         }
    #     )
    # )

   
    # country = forms.ChoiceField(
    #     required = True,
    #     choices = [(x, y) for (x, y) in settings.COUNTRIES ],
    #     widget = forms.Select(
    #         attrs={
    #             'type': 'select'
    #         }
    #     )
    # )

    # created_at = forms.DateTimeField(
    #     required = True,
    #     auto_now_add = True,
    #     widget = forms.DateInput(
    #         attrs={
    #             'type': 'date'
    #         }
    #     )
    # )

    # updated_at = forms.DateTimeField(
    #     required = True,
    #     auto_now_add = True,
    #     widget = forms.DateInput(
    #         attrs={
    #             'type': 'date'
    #         }
    #     )
    # )

    # class ProduitForm(forms.Form):
    # price = forms.DecimalField(
    #     required = True,
    #     max_digits = 10,
    #     decimal_places=2,
    #     widget = forms.NumberInput(
    #         attrs={
    #             'type': 'number'
    #         }
    #     )
    # )

    # image = forms.ImageField(
    #     required = True,
    #     upload_to = "PRODUCT_IMG",
    #     widget = forms.Select(
    #         attrs={
    #             'type': 'image'
    #         }
    #     )
    # )

    # created_at = forms.DateTimeField(
    #     required = True,
    #     auto_now_add = True,
    #     widget = forms.DateInput(
    #         attrs={
    #             'type': 'date'
    #         }
    #     )
    # )

    # updated_at = forms.DateTimeField(
    #     required = True,
    #     auto_now_add = True,
    #     widget = forms.DateInput(
    #         attrs={
    #             'type': 'date'
    #         }
    #     )
    # )

    # magasin = forms.ForeignKey(
    #     required = True,
    #     on_delete = 
    # )
