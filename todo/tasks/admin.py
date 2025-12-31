from django.contrib.admin import register, ModelAdmin

from todo.tasks.models import Task


@register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ('user', 'titulo', 'descricao', 'status', 'criada_em')
    list_filter = ('user', 'status')
    ordering = ['-criada_em']
