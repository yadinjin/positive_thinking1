from django.db import models

# Create your models here.


class Home(models.Model):
    site_section_name = models.CharField(verbose_name="Название раздела",
                                         max_length=50)
    site_section_slug = models.SlugField(verbose_name="Слаг",
                                         max_length=50)
    link_to_section_page = models.URLField(verbose_name="Ссылка на страницу раздела")
    site_section_icon = models.ImageField(verbose_name="Иконка раздела",
                                          upload_to="icons/")
    output_order = models.IntegerField(verbose_name="Порядок вывода в списке разделов",
                                       unique=True,
                                       auto_created=False)
    section_is_active = models.BooleanField(verbose_name="Признак отображения на главной странице",
                                            editable=True,
                                            default=False)



