from django.shortcuts import render
from markdown2 import Markdown
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_md = util.get_entry(title)

    if entry_md:
        # Title exists, convert md to HTML and return rendered template
        entry_HTML = Markdown().convert(entry_md)
        print(entry_HTML)
        return render(request, "encyclopedia/entry.html", {"title": title, "entry": entry_HTML})
    else:
        return HttpResponse("No entry, please check your entry!")