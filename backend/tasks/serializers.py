from rest_framework import serializers

from .models import Task


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)

        # Instance of the parent class
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class TaskSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
