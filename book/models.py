from django.db import models


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return CategoryModel.objects.all()

    def __str__(self):
        return self.name


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')
    published_at = models.DateTimeField()
    text = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, default=1, related_name='categories')

    def __str__(self):
        return f'{self.title}'