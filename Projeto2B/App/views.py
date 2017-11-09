from django.shortcuts import render




#Impoto a <nome_da_app>.models e a Classe criada para aparecer na página contato.html
def index(request):
    return render(request,"index.html")

def matricula(request):
    return render(request,"matricula.html")