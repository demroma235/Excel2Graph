from django.forms import Form, FileField


class LoadForm(Form):
    download_file = FileField()