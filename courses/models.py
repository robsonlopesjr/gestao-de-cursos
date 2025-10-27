import os

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
    description = models.TextField(
        blank=True, null=True, verbose_name="Descrição"
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Data de criação"
    )
    updated_at = models.DateField(auto_now=True, verbose_name="Data de edição")

    # Sobrescrever o método save
    def save(self, *args, **kwargs):
        # Verificar se o objeto já existe no banco de dados
        if self.pk:
            # Buscar o objeto atual no banco
            old_image = Course.objects.get(pk=self.pk).image
            # Comparar se a imagem foi alterada
            if old_image and old_image != self.image:
                # Remover a imagem antiga do sistema de arquivos
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

        # Dar continuidade ao salvamento do registro
        super().save(*args, **kwargs)

    # Sobrescrever o método delete para remover a imagem
    def delete(self, *args, **kwargs):
        # Remover a imagem associada ao objeto
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        # Excluir o registro
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
