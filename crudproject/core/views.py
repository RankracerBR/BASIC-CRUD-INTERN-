from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        matricula = request.POST['matricula']
        try:
            aluno = Aluno.objects.get(nome=nome, matricula=matricula)
        except Aluno.DoesNotExist:
            mensagem_erro = "Credenciais incorretas. Tente novamente."
            return render(request, 'index.html', {'mensagem_erro':mensagem_erro})

        nome = aluno.nome
        matricula = aluno.matricula
        
        request.session['nome'] = nome
        request.session['matricula'] = matricula
            
        return redirect('user_page')
        
    return render(request, 'index.html')
        
def create_user(request):
    message = 'Aluno já registrado'
    if request.method == 'POST':
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')

        if Aluno.objects.filter(nome=nome, matricula=matricula).exists():
            return render(request, 'create_user.html', {'message':message})

        aluno = Aluno(
            nome = nome,
            matricula = matricula,
        )
        
        aluno.save()
        
        return redirect('sucess_page')
    
    return render(request,'create_user.html')

def sucess_page(request):
    return render(request, 'sucess_page.html')

def user_page(request):
    nome = request.session.get('nome')
    matricula = request.session.get('matricula')

    return render(request, 'user_page.html', {'nome': nome, 'matricula': matricula})

def delete_user(request):
    aluno = None

    if request.method == 'POST':
        nome = request.session.get('nome')
        matricula = request.session.get('matricula')

        aluno = get_object_or_404(Aluno, nome=nome, matricula=matricula)
        aluno.delete()

        del request.session['nome']
        del request.session['matricula']
        
        return redirect('deleted_user')  

    elif request.method == 'GET':
        nome = request.session.get('nome')
        matricula = request.session.get('matricula')

        aluno = get_object_or_404(Aluno, nome=nome, matricula=matricula)

    return render(request, 'deleting_user.html', {'aluno': aluno})

def deleted_user(request):
    return render(request, 'deleted_user.html')

def update_user(request):
    nome = request.POST.get('nome')
    matricula = request.POST.get('matricula')
    
    aluno = Aluno.objects.get(nome=request.session['nome'], matricula=request.session['matricula'])

    aluno.nome = nome
    aluno.matricula = matricula
    aluno.save()

    request.session['nome'] = aluno.nome
    request.session['matricula'] = aluno.matricula

    return redirect('user_page')