from ast import Return
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#Function to show the page when user types "/wiki/ <name>"
def wiki (request, name):
    return render(request, (f"encyclopedia/wiki/, {name}"), {
        "entries": util.get_entry()
    })
