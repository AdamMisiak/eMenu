class CurrentUrlObject(object):
    def __init__(self, model, url_field, lookup_field="id"):
        self.model = model
        self.url_field = url_field
        self.lookup_field = lookup_field

    def set_context(self, serializer_field):
        self.object = self.model.objects.get(
            **{self.lookup_field: serializer_field.context["view"].kwargs.get(self.url_field)}
        )

    def __call__(self):
        return self.object
