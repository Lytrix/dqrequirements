#from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime

# /////////////////////////////////////////////////
# Option menu's
# /////////////////////////////////////////////////

# class Organisatie(models.Model):
#     org_id = models.AutoField(primary_key=True)
#     Cluster = models.CharField(max_length=255, null=True)
#     Organisatie = models.CharField(max_length=255, null=True)

#     def __str__(self):
#         return '{} - {}'.format(self.Cluster, self.Organisatie)

#     class Meta:
#         db_table = 'organisatie'


# class Rol(models.Model):
#     role_id = models.AutoField(primary_key=True)
#     Rol = models.CharField(max_length=255, null=True)

#     def __str__(self):
#         return '{}'.format(self.Rol)

#     class Meta:
#         db_table = 'rol'

class ProductType(models.Model):
    product_type_id = models.AutoField(primary_key=True)
    product_type_name = models.CharField(max_length=255, null=True)
    product_description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.product_type_name)

    class Meta:
        db_table = 'product_type'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=True)
    product_type = models.ForeignKey(ProductType, blank=True,
                            related_name='product_type'
                            )
    def __str__(self):
        return '{} - {}'.format(self.product_type, self.product_name)

    class Meta:
        db_table = 'product'


class CriteriaType(models.Model):
    criteria_type_id = models.AutoField(primary_key=True)
    criteria_type_name = models.CharField(max_length=255, null=True)
    criteria_description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.criteria_type_name)


class Criteria(models.Model):
    criteria_id = models.AutoField(primary_key=True)
    criteria_type = models.ForeignKey(CriteriaType, blank=True, related_name='criteria_type', on_delete=models.CASCADE, null=True)
    criteria_value = models.CharField(max_length=255, null=True)


class ScopeType(models.Model):
    scope_id = models.AutoField(primary_key=True)
    scope_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.scope_name)


class Scope(models.Model):
    scope_id = models.AutoField(primary_key=True)
    scope_type = models.CharField(max_length=255, null=True)
    scope_description = models.ManyToManyField(ScopeType,
                            related_name='scope_type')
    def __str__(self):
        return '{}'.format(self.scope_type)


class SubDimensionType(models.Model):
    subdimension_type_id = models.AutoField(primary_key=True)
    subdimension_type_name = models.CharField(max_length=255, null=True)
    subdimension_type_description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.subdimension_type_name)


class Dimension(models.Model):
    dimension_id = models.AutoField(primary_key=True)
    dimension_name = models.CharField(max_length=255, null=True)
    dimension_description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.dimension_name)

    class Meta:
        db_table = 'dimension'


class SubDimension(models.Model):
    subdimension_id = models.AutoField(primary_key=True)
    subdimension_type = models.ForeignKey(SubDimensionType, blank=True, related_name='subdimension_type', on_delete=models.CASCADE, null=True)
    subdimension_acceptance_criteria = models.ForeignKey(Criteria, blank=True, related_name='acceptance_criteria', on_delete=models.CASCADE, null=True)
    subdimension_scope = models.CharField(max_length=255, null=True)
    subdimension_dimension = models.ForeignKey(Dimension,
                            related_name='dimension')
    subdimension_description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{} - {}'.format(self.subdimension_dimension, self.subdimension_type.subdimension_type_name)

    class Meta:
        db_table = 'subdimension'


class DataElement(models.Model):
    data_element_id = models.AutoField(primary_key=True)
    data_element_name = models.CharField(max_length=255, null=True)
    data_element_uri = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.data_element_name)

    class Meta:
        db_table = 'data_element'


# class Employee(models.Model):
#     employee_id = models.AutoField(primary_key=True)
#     Voornaam = models.CharField(max_length=255, null=True)
#     Achternaam = models.CharField(max_length=255, null=True)
#     Email = models.CharField(max_length=128, null=True)
#     Telefoon = models.CharField(max_length=128, null=True)
#     Rol = models.ForeignKey(Rol,
#                             related_name='collegue_role',
#                             on_delete=models.CASCADE,
#                             null=True)
#     ZoekeenCollegaUrl = models.CharField(max_length=128, blank=True, null=True)

#     def Functie(self):
#         return '{}'.format(self.Rol.Rol)

#     def __str__(self):
#         return '{} - {} {}'.format(self.Rol, self.Voornaam, self.Achternaam)

#     def fullName(self):
#         return '{} {}'.format(self.Voornaam, self.Achternaam)

#     class Meta:
#         db_table = 'employee'


# /////////////////////////////////////////////////
# Main Project
# /////////////////////////////////////////////////

class Requirement(models.Model):
    req_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, blank=True, null=True)
    data_element = models.ForeignKey(DataElement, blank=True, related_name='data_element', on_delete=models.CASCADE, null=True)
    subdimension = models.ManyToManyField(SubDimension, related_name='requirement_subdimension')
    Intakedate = models.DateField(blank=False, default=datetime.now)
    #Organisatie_opdrachtgever = models.ForeignKey(Organisatie, blank=True, related_name='organisatie_project', on_delete=models.CASCADE, null=True)

    # Convert manytomany list into a string 
    #@property
    #def product(self):
    #    return '{}'.format(self.product_name)

    #@property
    #def subdimension(self):
    #    return '{} - {}'.format(self.subdimension_dimension.dimension_name, self.subdimension_type.subdimension_name)
        #return ', '.join([a.dimension_name for a in self.dimension_name.all()])

    #@property
    #def Jaar(self):
    #    return '{}'.format(self.startdatum.year)

    def __str__(self):
        return '{} - {} - {}'.format(self.req_id, self.data_element, self.product.product_name)

    class Meta:
        db_table = 'requirement'

# Subprojects

    #def project_directory_path(instance, filename):
     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
     #    return 'projectplannen/project_{0}/{1}'.format(instance.Project.pjid,
      #                                              filename)


# class Regulation(models.Model):
#     pp_id = models.AutoField(primary_key=True)
#     Projectplan = models.FileField(upload_to=project_directory_path, blank=True)
#     Aanleiding = models.CharField(max_length=2000, blank=True, null=True)
#     Doel = models.CharField(max_length=2000, blank=True, null=True)
#     Resultaat = models.CharField(max_length=2000, blank=True, null=True)
#     Afbakening = models.CharField(max_length=2000, blank=True, null=True)
#     Project = models.ForeignKey(Project, related_name='projectplan_project_set', on_delete=models.CASCADE, null=True)
    
#     def __str__(self):
#         return '{}-{}'.format(self.pp_id, self.Projectplan)

#     class Meta:
#         db_table = 'projectplan'

