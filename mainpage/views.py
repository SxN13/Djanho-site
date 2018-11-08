from django.shortcuts import render
import getpass
from .form import UploadFileForm # подключение формы

sss = ""

def index(request):
    v = getpass.getuser()
    print(v)
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print(form)
        save_path = 'mainpage/static/upload/' # папка для сохранения файлов
        print(request.FILES['file'].name)
        if form.is_valid():
                # сохранение файла
            tmp = save_path
            handle_upload(request.FILES['file'], tmp)
            #return HttpResponse('/mainpage/up.html')
    else:
        form = UploadFileForm()
    return render(request, 'mainpage/index.html', {'value': v, 'form': form})


def handle_upload(f,p):
    path = p + f.name
    sss = path
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            print(chunk)


def up(request):
    str = ""
    with open(sss) as f:
        str = f.read()
    return render(request, 'mainpage/up.html', {'str': str})
