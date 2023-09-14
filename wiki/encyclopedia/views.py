from django.shortcuts import render

from . import util


from markdown2 import Markdown
from . import util


def convert_html(title):
    content = util.get_entry(title)
    markdown = Markdown()
    if content == None:
        return "No such entry"
    else:
        return markdown.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    html_contet = convert_html(title)
    if html_contet == None:
        return render(request, "encyclopedia/error.html", {
            "message": "this entry not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title ,
            "content": html_contet ,
            
        })
