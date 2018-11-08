from django.shortcuts import render
import getpass

def index(response):
    v = getpass.getuser()
    return render(response,'hellopage/hellopage.html', {'val' : v})
