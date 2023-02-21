from django.shortcuts import render
from .agents.cost_living import CostLiving


def start_page(request):
    return render(request, "main/start_page.html")


def test_function(request):
    cl = CostLiving()
    cl.get_information()
    test_list = cl.out(1, 0, 3, 0, "общественный транспорт", "1-к в центре", "Рейтинг стран")
    context = {"info": test_list}

    return render(request, "main/test_page.html", context)
