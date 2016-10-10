from django.shortcuts import render
from django.http import JsonResponse
from .models import Enigma, RotorI, RotorII, RotorIII, RotorIV, RotorV
from .models import RotorVI, RotorVII, RotorVIII
# Create your views here.


def home(request):
    return render(request, 'index.html', context=None)


def enigma(request):
    return render(request, 'enigma.html', context=None)


def encrypt(request):
    rotor_selection = {'I': RotorI(), 'II': RotorII(), 'III': RotorIII(),
                       'IV': RotorIV(), 'V': RotorV(), 'VI': RotorVI(),
                       'VII': RotorVII(), 'VIII': RotorVIII()}
    rotor_list = request.GET.getlist('rotor')
    slow_rotor = rotor_selection[rotor_list[0]]
    middle_rotor = rotor_selection[rotor_list[1]]
    fast_rotor = rotor_selection[rotor_list[2]]
    rotor_settings = request.GET.getlist('setting')
    letter = request.GET['letter']
    if rotor_settings[2] in fast_rotor.turnover:
        fast_rotor_turnover = True
    else:
        fast_rotor_turnover = False
    if rotor_settings[1] in middle_rotor.turnover:
        middle_rotor_turnover = True
    else:
        middle_rotor_turnover = False
    enigma = Enigma(slow_rotor, middle_rotor, fast_rotor, rotor_settings)
    cipher_letter = enigma.encrypt(letter)
    return JsonResponse({'cipher_letter': cipher_letter,
                         'middle_rotor_turnover': middle_rotor_turnover,
                         'fast_rotor_turnover': fast_rotor_turnover})
