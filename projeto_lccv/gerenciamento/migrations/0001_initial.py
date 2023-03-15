# Generated by Django 4.1.7 on 2023-03-12 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alunos",
            fields=[
                ("id_aluno", models.IntegerField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=11)),
                ("rg", models.CharField(max_length=8)),
                ("matricula", models.CharField(max_length=8)),
                ("telefone", models.CharField(max_length=11)),
                ("email", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Disciplinas",
            fields=[
                (
                    "id_disciplina",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("nome", models.CharField(max_length=255)),
                ("codigo", models.CharField(max_length=7)),
                ("carga_horaria", models.IntegerField(null=True)),
                ("ementa", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Frequencia",
            fields=[
                (
                    "id_frequencia",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("dia", models.DateField()),
                (
                    "id_materia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.disciplinas",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professores",
            fields=[
                (
                    "id_professor",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("nome", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=11)),
                ("rg", models.CharField(max_length=8)),
                ("codigo", models.CharField(max_length=8)),
                ("email", models.CharField(max_length=255)),
                ("telefone", models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name="PlanoAula",
            fields=[
                (
                    "id_plano_aula",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("tema_aula", models.CharField(max_length=255)),
                ("conteudo", models.TextField()),
                ("metodo", models.CharField(max_length=50)),
                ("dia", models.DateField()),
                (
                    "id_disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.disciplinas",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FrequenciaAluno",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("presenca", models.CharField(default="T", max_length=1)),
                (
                    "id_aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.alunos",
                    ),
                ),
                (
                    "id_frequencia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.frequencia",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="disciplinas",
            name="id_professor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="gerenciamento.professores",
            ),
        ),
        migrations.CreateModel(
            name="DisciplinaAluno",
            fields=[
                (
                    "id_matricula",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("nota", models.FloatField()),
                (
                    "id_aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.alunos",
                    ),
                ),
                (
                    "id_disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.disciplinas",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Atividades",
            fields=[
                (
                    "id_atividade",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("atividade", models.TextField()),
                ("tipo", models.CharField(max_length=50)),
                ("data_postagem", models.DateField()),
                ("data_entrega", models.DateField()),
                (
                    "id_disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.disciplinas",
                    ),
                ),
                (
                    "id_plano_aula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.planoaula",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AtividadeAluno",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("nota", models.FloatField()),
                (
                    "id_aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.alunos",
                    ),
                ),
                (
                    "id_atividade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gerenciamento.atividades",
                    ),
                ),
            ],
        ),
    ]
