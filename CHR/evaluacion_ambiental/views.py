from django.shortcuts import render
from datetime import datetime
from bs4 import BeautifulSoup
from .models import Project
import requests
import json
import os


url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?'

def get_data(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    table = soup.find('table', class_ = 'tabla_datos')
    tbody = [[x.text for x in row.find_all('td')[:-1]] for row in table.find_all('tr')[2:]]
    thead = [[x.text for x in row.find_all('th')[:-1]] for row in table.find_all('tr')][0]
    result = [dict(zip(thead, t)) for t in tbody]

    with open('file.json', 'w', encoding='UTF-8') as f:
        json.dump(result, f)

get_data(url)

def date_converter(date):
    new_date = datetime.strptime(date, "%d/%m/%Y")
    return new_date

def get_file_data():
    file = f'{os.getcwd()}\\file.json'
    project_list = []
    all_projects = [x.id for x in Project.objects.all()]
    with open(file, 'r') as f:
        rows = json.loads(f.read())
        for row in rows:
            if int(row["No"]) not in all_projects:
                presentation_date = date_converter(row["FechaPresentaci\u00f3nFecha deIngreso(*)"])
                project = Project.objects.create(
                    id=row["No"],
                    name=row["Nombre"],
                    type=row["Tipo"],
                    region=row["Regi\u00f3n"],
                    typology=row["Tipolog\u00eda"],
                    holder=row["Titular"],
                    investment=row["Inversi\u00f3n(MMU$)"].replace(",", "."),
                    presentation_date=presentation_date,
                    state=row["Estado"],
                )
                project.save()
                project_list.append(project)
            else:
                project_list.append(Project.objects.filter(id=row["No"]).last())

    return project_list

def index(request):
    project_list = get_file_data()
    context = dict(
        project_list = project_list,
    )
    return render(request, 'evaluacion_ambiental/index.html', context=context)