from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    capitalize = request.POST.get('capitalize', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzetext = ''
        for char in djtext:
            if char not in punctuations:
                analyzetext = analyzetext + char

        params = {'purpose': 'Remove-Punctuation', 'TextAnalyze': analyzetext}
        djtext = analyzetext

    if newlineremover == 'on':
        analyzetext = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzetext = analyzetext + char

        params = {'purpose': 'Remove-New-Line', 'TextAnalyze': analyzetext}
        djtext = analyzetext

    if extraspaceremover == 'on':
        analyzetext = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzetext = analyzetext + char

        params = {'purpose': 'Remove-Extra-Space', 'TextAnalyze': analyzetext}
        djtext = analyzetext

    if capitalize == 'on':
        analyzetext = ''
        for char in djtext:
            analyzetext = analyzetext + char.upper()

        params = {'purpose': 'capital-Text', 'TextAnalyze': analyzetext}

    if removepunc != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and capitalize != 'on':
        return HttpResponse('please select any operation and try again..')

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')
