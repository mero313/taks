from django.shortcuts import render

from . import util


from markdown2 import Markdown
from . import util


def convert_html(title):
    content = util.get_entry(title)
    markdown =Markdown()
    if content == None:
        return None
    else:
        return markdown.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    html_content = convert_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "this entry does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title ,
            "content": html_content 
        })
    

def search(request):
    if request.method=="POST":
        search=request.POST['q']
        html_content = convert_html(search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
            "title": search ,
            "content": html_content 
        })
        else:
            allEntries = util.list_entries()
            counter = []
            for entry in allEntries:
                if search.lower() in entry.lower():
                    counter.append(entry)
                    return render (request ,'encyclopedia/search.html' ,{
                        'counter': counter
                    })
                
        
def new_page(request):
    if request.method =="GET":
        return render(request , "encyclopedia/new.html" )
    else:
        title= request.POST['title']
        content = request.POST['content']
        titleExist =util.get_entry(title)
        if titleExist is not None:
            return render (request , "encyclopedia/error.html" , {
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title , content)
            html_content = convert_html(title)
            return render(request , "encyclopedia/entry.html" , {
                "title":title , 
                "content": html_content
            })



        

