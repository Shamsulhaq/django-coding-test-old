from django.views import generic
from django_filters.views import FilterView

from product.models import Variant, Product
from product.filters import ProductFilters


class ProductView(FilterView, generic.ListView):
    template_name = 'products/list.html'
    filterset_class = ProductFilters
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variant'] = Variant.objects.all()
        context['total_items'] = self.object_list.count()
        return context


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
