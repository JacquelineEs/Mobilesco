from django.shortcuts import render

# Create your views here.
def my_view(request):
    Pedidos = [
        {"title": "Maria Castillo Perez"},
        {"title": "Nancy Odeth Vallarta Meza"},
        {"title": "Claudia"}
    ]
    context = {
        "Pedidos": Pedidos
    }
    return render(request, "Pedidos/Pedidos.html", context)