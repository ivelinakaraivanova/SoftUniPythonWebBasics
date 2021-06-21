from django.core.exceptions import ValidationError


def validate_dot(value):
    if '.' in value:
        raise ValidationError("'.' is present in value")


def validate_owner_todos_count(owner):
    if owner.todo_set.count() > 2:  # todo_set - take all todos of this owner and count them
        raise ValidationError(f'{owner.name} cannot have more than 2 todos')
