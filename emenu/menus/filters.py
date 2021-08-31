from django_filters import CharFilter, DateFilter, FilterSet

from .models import Menu


class MenuFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains", distinct=True)
    # format in query params: YYYY-MM-DD
    created_from = DateFilter(field_name="created", lookup_expr="gte", distinct=True)
    created_to = DateFilter(field_name="created", lookup_expr="lte", distinct=True)
    modified_from = DateFilter(field_name="modified", lookup_expr="gte", distinct=True)
    modified_to = DateFilter(field_name="modified", lookup_expr="lte", distinct=True)

    class Meta:
        model = Menu
        fields = [
            "name",
            "created_from",
            "created_to",
            "modified_from",
            "modified_to",
        ]
