from django.contrib import admin
from django import forms
from .models import Alunos, Professores, Disciplinas, Frequencia, FrequenciaAluno, DisciplinaAluno, PlanoAula, Atividades, AtividadeAluno

# Register your models here.
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = '__all__'
        widgets = {
            'id_aluno': forms.NumberInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
class AlunoAdmin(admin.ModelAdmin):
    form = AlunoForm      


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professores
        fields = '__all__'
        widgets = {
            'id_professor': forms.NumberInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'})
        }
class ProfessorAdmin(admin.ModelAdmin):
    form = ProfessorForm


class DisciplinaForm(forms.ModelForm):
    id_professor = forms.ModelChoiceField(queryset=Professores.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Disciplinas
        fields = '__all__'
        widgets = {
            'id_disciplina': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_professor': forms.NumberInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'carga_horaria': forms.NumberInput(attrs={'class': 'form-control'}),
            'ementa': forms.TextInput(attrs={'class': 'form-control'})
        }
class DisciplinaAdmin(admin.ModelAdmin):
    form = DisciplinaForm


class FrequenciaForm(forms.ModelForm):
    id_materia = forms.ModelChoiceField(queryset=Disciplinas.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Frequencia
        fields = '__all__'
        widgets = {
            'id_frequencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_materia': forms.NumberInput(attrs={'class': 'form-control'}),
            'dia': forms.DateInput(attrs={'class': 'form-control'}),           
        }
class FrequenciaAdmin(admin.ModelAdmin):
    form = DisciplinaForm


class FrequenciaAlunoForm(forms.ModelForm):
    id_aluno = forms.ModelChoiceField(queryset=Alunos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    id_frequencia = forms.ModelChoiceField(queryset=Frequencia.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = FrequenciaAluno
        fields = '__all__'
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_aluno': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_frequencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'presenca': forms.TextInput(attrs={'class': 'form-control'})
        }
class FrequenciaAlunoAdmin(admin.ModelAdmin):
    form = FrequenciaAlunoForm


class DisciplinaAlunoForm(forms.ModelForm):
    id_aluno = forms.ModelChoiceField(queryset=Alunos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    id_disciplina = forms.ModelChoiceField(queryset=Disciplinas.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = DisciplinaAluno
        fields = '__all__'
        widgets = {
            'id_matricula': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_aluno': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_disciplina': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),           
        }
class DisciplinaAlunoAdmin(admin.ModelAdmin):
    form = DisciplinaAlunoForm


class PlanoAulaForm(forms.ModelForm):
    id_disciplina = forms.ModelChoiceField(queryset=Disciplinas.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = PlanoAula
        fields = '__all__'
        widgets = {
            'id_plano_aula': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_disciplina': forms.NumberInput(attrs={'class': 'form-control'}),
            'tema_aula': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.TextInput(attrs={'class': 'form-control'}),
            'metodo': forms.TextInput(attrs={'class': 'form-control'}),
            'dia': forms.TextInput(attrs={'class': 'form-control'}),
                       
        }
class PlanoAulaAdmin(admin.ModelAdmin):
    form = PlanoAulaForm


class AtividadeForm(forms.ModelForm):
    id_disciplina = forms.ModelChoiceField(queryset=Disciplinas.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    id_plano_aula = forms.ModelChoiceField(queryset=PlanoAula.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Atividades
        fields = '__all__'
        widgets = {
            'id_atividade': forms.NumberInput(attrs={'class': 'form-control'}),
            'atividade': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_postagem': forms.DateInput(attrs={'class': 'form-control'}),
            'data_entrega': forms.DateInput(attrs={'class': 'form-control'}),
            'id_disciplina': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_plano_aula': forms.NumberInput(attrs={'class': 'form-control'}),             
        }
class AtividadeAdmin(admin.ModelAdmin):
    form = AtividadeForm


class AtividadeAlunoForm(forms.ModelForm):
    id_atividade = forms.ModelChoiceField(queryset=Atividades.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    id_aluno = forms.ModelChoiceField(queryset=Alunos.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = AtividadeAluno
        fields = '__all__'
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_atividade': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_aluno': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),                     
        }
class AtividadeAlunoAdmin(admin.ModelAdmin):
    form = AtividadeAlunoForm


admin.site.register(Alunos, AlunoAdmin)
admin.site.register(Professores, ProfessorAdmin)
admin.site.register(Disciplinas, DisciplinaAdmin)
admin.site.register(Frequencia, FrequenciaAdmin)
admin.site.register(FrequenciaAluno, FrequenciaAlunoAdmin)
admin.site.register(DisciplinaAluno, DisciplinaAlunoAdmin)
admin.site.register(PlanoAula, PlanoAulaAdmin)
admin.site.register(Atividades, AtividadeAdmin)
admin.site.register(AtividadeAluno, AtividadeAlunoAdmin)
