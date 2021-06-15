from django.contrib import admin

from todo_project.todo_app.models import Todo, Person, Category


#@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['text', 'owner']
    sortable_by = ['text']
    list_filter = ['owner']

    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)

