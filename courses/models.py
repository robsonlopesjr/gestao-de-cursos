from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço Original"
    )
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Preço Desconto",
    )
    image = models.ImageField(
        upload_to="courses/", blank=True, null=True, verbose_name="Imagem"
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Data de criação"
    )
    updated_at = models.DateField(auto_now=True, verbose_name="Data de edição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
