from django.shortcuts import render
import xlrd
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response

from Excel2Graph.forms import LoadForm


def index(request):
    form = LoadForm()
    return render(request, "index.html", {'form': form})


def load_file(request):
    if request.method == "POST":
        form = LoadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = request.FILES['download_file']
            rb = xlrd.open_workbook(filename=None, file_contents=doc.read())
            sheet = rb.sheet_by_index(0)
            wr = open('values.txt', 'w')
            vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
            for val in vals:
                for v in val:
                    wr.write(str(v) + " ")
                wr.write("\n")
            wr.close()
    return index(request)


def result(request):
    f = open('values.txt', 'r')
    list_example = []
    list = []
    for line in f:
        string = line.split(" ")
        for l in string:
            print("L = " + l)
            try:
                list_example.append(float(l))
            except ValueError:
                pass

        print(list_example)
        list.append(list_example)
        list_example = []
    print(list)
    f.close()
    return render(request, 'result.html', {'list': list})
