from django.forms import ModelForm
from django.shortcuts import redirect, render

from .models import *


# Função index - Lista Transações
def index(request):
    ult_transacoes = Transacao.objects.order_by('-data')[:20]
    context = {'ult_transacoes': ult_transacoes}
    return render(request, 'contas/index.html', context)

# Formulário Cadastro transações
class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = '__all__'

def nova_transacao(request): 
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        transacao = form.save()
        return redirect('index')
    return render(request, 'contas/form_transacao.html', {'form': form})

# Formulário Atualiza Transação
def up_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance = transacao)
    if form.is_valid():
        transacao = form.save()
        return redirect('index')
    contexto = {'form': form}
    contexto.update({'transacao': transacao})
    return render(request, 'contas/form_transacao.html', contexto)

# Formulário Deleta Transação
def del_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('index')
