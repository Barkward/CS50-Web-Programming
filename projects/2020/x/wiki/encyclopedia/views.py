from ast import Return
from xml.etree.ElementInclude import include
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from markdown import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


#Function to show the page when user types "/wiki/ <name>" -- return nonExistant in not found
def wiki (request, name):
    mark = Markdown()
    page = util.get_entry(name)

    if page is None:
        return render(request, "encyclopeia/nopage.html", {
            "entryTitle":name
        })

    else:
        return render(request, "encyclopedia/entry.html", {

            "entry":mark.convert(page),
            "entryTitle": name
        })
