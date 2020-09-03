from django.contrib import admin
from django import forms
from ibprojecten.api.models import (Requirement,
                                    Product,
                                    ProductType,
                                    Requirement,
                                    Scope,
                                    ScopeType,
                                    Criteria,
                                    CriteriaType,
                                    Dimension,
                                    SubDimension,
                                    SubDimensionType,
                                    DataElement)

# Change header name
admin.site.site_header = 'Data Quality Requirements'

# Register your models here.

# //////////////////////////////////////////////
# Option lists
# /////////////////////////////////////////////

#class ProductTypeAdmin(admin.ModelAdmin):
#    list_product_type = ('product_type')

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Scope)
admin.site.register(ScopeType)
admin.site.register(Criteria)
admin.site.register(CriteriaType)
admin.site.register(Dimension)
admin.site.register(SubDimension)
admin.site.register(SubDimensionType)
admin.site.register(DataElement)
admin.site.register(Requirement)

#class RolesAdmin(admin.ModelAdmin):
 #   list_roles = ('Rol')
   # filter_horizontal = ('user',)

# Subproject list view in project
#class DimensionInline(DimensionAdminMixin, admin.StackedInline):
#    model = Dimension
#    show_change_link = True
#    extra = 0


# //////////////////////////////////////////////
# Main Project
# /////////////////////////////////////////////


#class RequirementAdmin(admin.ModelAdmin):
#   list_requirements = ('Requirement')
    #inlines = [DimensionInline,]


#admin.site.register(Requirement, RequirementAdmin)


