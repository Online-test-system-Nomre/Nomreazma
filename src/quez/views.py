import sqlite3
from os import system

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import ChoiceQuestions


@csrf_protect
def getresponses(request):
    """ This function gets response
    from frontend and scoring by json file"""

    if request.method == 'POST':
        user_data = {}
        user_data["num"] = int(request.POST.get("num"))

        user_data["stdudent_name"] = str(request.POST.get("username"))
        user_test = {}
        for i in range(1, 4):
            user_test[f"{i}"] = request.POST.get(f"t{i}")

        user_data["test"] = user_test

        ChoiceQuestionsclass = ChoiceQuestions(f'{user_data}')

        print(ChoiceQuestionsclass.get_data_json())
        return render(request, 'quez/test.html')

    else:
        return render(request, 'quez/test.html')


@csrf_protect
def postresponses(request):
    """"""
    # run readDB bash script, this script work create new html
    #system("chmod +x scripts/readDB;./scripts/readDB")
    conn = sqlite3.connect("score.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    db = cur.fetchall()
    
    datas = ''
    file = open("quez/templates/quez/natije.html", "w", encoding="utf-8")

    for data in db:
        data = str(data).replace("(", "");data = str(data).replace(")", "")
        data = str(data).replace('"', "");data = str(data).replace("'", "")
        datas += "<p>"+str(data)+"</p>"

    HTML_text = '''
                {% load static %}
                {% block content %}
                <head>
                    <title>نمره آزما</title>
                </head>
                <script>
                alert("نتیجه آزمون شما در زیر مشخص شده است با عرض معذرت که نمره شما خصوصی نیست ان‌شاالله در بروز رسانی های آینده اگر در سایت مشکلی وجود داشت لطفا به عوامل نمره آزما گذارش دهید(غیر از نمره کم!) سپاس فراوان تیم توسعه نمره آزما");
                </script>
    '''+datas+'{%endblock%}'
    file.write(HTML_text)

    file.close()    
    return render(request, 'quez/natije.html')


def index(request):
    context = {}
    return render(request, 'index.html', context)
