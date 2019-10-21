# from django.db import models
# from django.contrib.auth.models import User
# from tinymce.models import HTMLField
# #from django.db.models import search_term
# import datetime as dt





# class Categories(models.Model):
#     categories = models.CharField(max_length=40)

#     def __str__(self):
#         return self.categories

#     def save_category(self):
#         self.save()

#     @classmethod
#     def delete_category(cls, categories):
#         cls.objects.filter(categories=categories).delete()

# class Technologies(models.Model):
#     technologies = models.CharField(max_length=40)

#     def __str__(self):
#         return self.technologies

#     def save_technologies(self):
#         self.save()

#     @classmethod
#     def delete_technologies(cls, technologies):
#         cls.objects.filter(technologies=technologies).delete()

# class Countries(models.Model):
#     countries = models.CharField(max_length=40)

#     def __str__(self):
#         return self.countries

#     def save_country(self):
#         self.save()

#     @classmethod
#     def delete_country(cls, countries):
#         cls.objects.filter(countries=countries).delete()

# class Project(models.Model):
#     title = models.CharField(max_length=40)
#     landing_page = models.ImageField(upload_to='media')
#     description = HTMLField()
#     link = models.CharField(max_length=200)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     country = models.ForeignKey(Countries,on_delete=models.CASCADE)
#     technologies = models.ManyToManyField(Technologies)
#     categories = models.ManyToManyField(Categories)
#     post_date = models.DateTimeField(auto_now_add=True)
#     pic = models.ImageField(upload_to='media/')

#     def __str__(self):
#         return self.title

#     @classmethod
#     def search_project(cls,search_term):
#         aword = cls.objects.filter(title__icontains=search_term)
#         return aword
        
# class Profile(models.Model):
#     pic = models.ImageField(upload_to='media')
#     description = HTMLField()
#     country = models.ForeignKey(Countries,on_delete=models.CASCADE)
#     username = models.ForeignKey(User,on_delete=models.CASCADE)
#     name =models.CharField(max_length=100)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name   