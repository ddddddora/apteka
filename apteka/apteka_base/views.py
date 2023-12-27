from django.core.exceptions import BadRequest
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from .models import action
from .models import partners

Treatmens = [
    {'id' : 1, 'medicines_name' : 'Противовирусные', 'recept' : False, 'describ' : 'Противовирусные лекарственные средства — очень разнородная фармакологическая группа, в которую входят препараты для лечения различных вирусных инфекций', 'image_1': 'arbid.png','image_2': 'ingav.png','image_3': 'unif.png','image_4': 'tirolon.png'},

    {'id' : 2, 'medicines_name' : 'Дерматотропные','recept' : False, 'describ' : 'Действие лекарственных средств защищающее кожу от воздействия микробов и паразитов, стимулирующее процессы регенерации и эпителизации кожи при заживлении ран, размягчении и рассасывании рубцовой ткани', 'image_1': 'aravia.png','image_2': 'treti-care.png','image_3': 'tretino.png','image_4': 'zink.png'},

    {'id' : 3, 'medicines_name' : 'Гормональные','recept' : False, 'describ' : 'Гормональные препараты — лекарственные средства, действующими началами которых являются гормоны и синтетические Вещества, обладающие гормоноподобным биологическим действием.', 'image_1': 'decsa.png','image_2': 'medrol.png','image_3': 'novinet.png','image_4': 'dimia.png'},

    {'id' : 4, 'medicines_name' : 'Антидепрессанты','recept' : True, 'describ' : 'Антидепрессанты — это группа лекарственных препаратов с тимоаналептическим эффектом, нормализующих активность нейромедиаторов (например, серотонина, норадреналина, дофамина) за счет прямого или опосредованного воздействия на уровень моноаминов.', 'image_1': 'fevarin.png','image_2': 'reksetin.png','image_3': 'pirazidol.png','image_4': 'lenuksil.png'},

    {'id' : 5, 'medicines_name' : 'Антисептические','recept' : False, 'describ' : 'Антисептики — препараты с антимикробной активностью. Они не имеют избирательного действия.', 'image_1': 'hloreks.png','image_2': 'mesta-mid.png','image_3': 'sprei.png','image_4': 'dezipol.png'},

    {'id' : 6, 'medicines_name' : 'Антиаллергитические','recept' : False, 'describ' : 'Предотвращение аллергических реакций.','image_1': 'suprast.png','image_2': 'loratod.png','image_3': 'zodak.png','image_4': 'zetrin.png'},

    {'id' : 7, 'medicines_name' : 'Сердечно-сосудистые','recept' : True, 'describ' : 'Сердечные препараты корректируют расстройства функций кардиоваскулярной системы.','image_1': 'bisoporol.png.','image_2': 'kardiolip.png','image_3': 'mokso.png','image_4': 'rozart.png'},

    {'id' : 8, 'medicines_name' : 'Иммунотропные','recept' : True, 'describ' : 'Иммунотропные препараты — это лекарственные средства, которые оказывают влияние на иммунную систему.', 'image_1': 'amiksin.png','image_2': 'galavit.png','image_3': 'radamir.png','image_4': 'tirolon-ver.png'},

    {'id' : 9, 'medicines_name' : 'Метаболики','recept' : True, 'describ' : 'Кардиометаболические препараты – средства, которые показаны людям нарушением питания сердечной мышцы.','image_1': 'asparkam.png','image_2': 'meldon.png','image_3': 'dioskl.png','image_4': 'kardioaktiv.png'},

    {'id' : 10, 'medicines_name': 'Антибиотики','recept' : False, 'describ' : 'Антибиотики — соединения, применяемые для блокирования развития или полного уничтожения опасных для человека микроорганизмов.','image_1': 'amozikl.png','image_2': 'arpeflu.png','image_3': 'ziprofl.png','image_4': 'tetrazikl.png'},

    {'id' : 11, 'medicines_name': 'Противоопухолевые', 'recept' : True, 'describ' : 'Предотвращение заболевание онкологии различного типа и стадий.','image_1': 'anazatrol.png','image_2': 'metotrit.png','image_3': 'reaferon.png','image_4': 'metatreks.png'},

    {'id' : 12, 'medicines_name': 'Офтальмологические','recept' : False, 'describ' : 'Лечение заболеваний глаз', 'image_1': 'defislez.png','image_2': 'gilan.png','image_3': 'oftolik.png','image_4': 'taufon.png'},
]


menu = [
    {'title': 'Главная страница', 'url_n': 'home'},
    {'title': 'О компании', 'url_n': 'about'},
    {'title': 'Препараты', 'url_n': 'tretm'},
    {'title': 'Акции', 'url_n': 'action_spisok'},
]


data = {'apteka': Treatmens, 'menu': menu, 'tretm_url': 'medicines'}
def index(request):
    return render(request, 'index.html', context=data)
def about(request):
    return render(request,'about.html', context=data)

def medicines_index(request, medicines_id):
    if 1 <= medicines_id <= 12:
        current = Treatmens[medicines_id - 1]
        return render(request, 'curr_medicines.html', context=current)
def Treatmens_mainpage(request):
    return render(request, 'medicines_name.html', context=data)

def action_spisok(request):
    actions = action.objects.all()
    return render(request, 'action_name.html', {'actions': actions})

def inf_action(request, action_id):
    actions = action.objects.get(id=action_id)
    return render(request, 'action.html', {'actions': actions})

def part(request, patners_name):
    partner = get_object_or_404(partners, slug=patners_name)
    data = {
            'part': partner,
            'menu': menu,
            }
    return render(request, 'partners.html', context=data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def Forbidden(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>')
def InternalServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')
def ErrBadRequest(request, exception):
    return HttpResponseBadRequest('<h1>Неверный запрос</h1>')
def err_400(request):
    raise BadRequest
def err_500(request):
    raise ffff
# имитация ошибки сервера

