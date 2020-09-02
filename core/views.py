from django.shortcuts import render, HttpResponse

def hello(request):
    return HttpResponse ('<h1> Minha Calculadora</h1>')
def calculadora(request, acao, dig1 , dig2):
    if acao == 'soma':
        resultado = dig1 + dig2
    if acao == 'multiplicacao':
        resultado = dig1 * dig2
    if acao == 'divisao':
        resultado = dig1 / dig2
    if acao == 'subtracao':
        resultado = dig1 - dig2
    return HttpResponse ('<h1> O resultado da {} entre {} e {} é igual a {}</h1>'.format(acao,dig1,dig2,resultado))
