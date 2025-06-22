from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil

class UsuarioCreate(CreateView):
    template_name = "usuarios/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:login')

    def form_valid(self, form):
        url = super().form_valid(form)
        grupo, _ = Group.objects.get_or_create(name="Docente")
        self.object.groups.add(grupo)
        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context

class PerfilUpdate(UpdateView):
    template_name = "usuarios/form.html"
    model = Perfil
    fields = ["nome_completo", "bi", "telefone"]
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return get_object_or_404(Perfil, usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"