# search_app views.py

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Csv, Product
from .forms import CsvModelForm
import csv
from .import searchengine as se

# Create your views here.

def index(request):
    pass
    return render(request, 'index.html')


def search(request):
    # print("=====request data====")
    # print(request.GET)
    element=request.GET.get('search')
    # print(element)
    products = Product.objects.values_list('name', flat=True)
    # print(products)
    products_list = list(products)
    # print(products_list)
    # print(type(products_list))

    results = se.search_element(element, products_list)
    # print(results)

    mydict = {
        "results" : results
    }
    # print(mydict)
    return render(request,'index.html', {'mydict':mydict})


def upload_csv(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(active=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    product = row[1]
                    Product.objects.create(
                        name = product,
                    )
                    print(row)
            obj.active = True
            obj.save()
        f.close()
    return render(request, 'upload.html', {'form':form})
