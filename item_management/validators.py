from django.forms import ValidationError
from django.http import JsonResponse


def validate_optional_fields(value):
    type_count = {
        'integer': 0,
        'string': 0,
        'multiline': 0,
        'boolean': 0,
        'date': 0,
    }
    max_fields_per_type = 3

    for key, field_value in value.items():
        field_type = key.split('_')[0]
        if field_type in type_count:
            type_count[field_type] += 1

            if type_count[field_type] > max_fields_per_type:
                return JsonResponse({ "message" : f'Too many fields of type {field_type}' })

        expected_type = None
        if field_type == 'integer':
            expected_type = int
        elif field_type == 'string' or field_type == 'multiline' or field_type == 'date':
            expected_type = str
        elif field_type == 'boolean':
            expected_type = bool

        if expected_type is not None and not isinstance(field_value, expected_type):
            return JsonResponse({ "message" : f'Invalid data type for key {key}. Expected {expected_type.__name__}' })