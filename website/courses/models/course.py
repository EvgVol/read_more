from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from pytils.translit import slugify

from .subject import Subject
from .advantage import Advantage
from .technology import Technology


User = get_user_model()


class Course(models.Model):
    """A model representing a course."""

    class Complexity(models.TextChoices):
        """Choices for the complexity of the course"""

        JUNIOR = 'JN', _('junior')
        MIDDLE = 'MD', _('middle')
        SENIOR = 'SN', _('senior')

    class Load(models.TextChoices):
        LITE = 'LT', _('lite')
        INTENSIVE = 'IS', _('intensive')
        MODERATE = 'MR', _('moderate')
        HIGH = 'HG', _('high')
        HIGHEST = 'HH', _('highest')

    owner = models.ForeignKey(User,
                              verbose_name=_("owner"),
                              related_name='courses_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                verbose_name=_("subject"),
                                related_name='courses',
                                on_delete=models.CASCADE)
    complexity = models.CharField(_('complexity'),
                                  max_length=2,
                                  choices=Complexity.choices,
                                  default=Complexity.JUNIOR)
    description = models.TextField(_("description"), max_length=650,
                                   help_text=_('Enter a description'))
    advantages = models.ManyToManyField(Advantage,
                                        verbose_name=_("advantages"),
                                        related_name='courses',
                                        blank=True)
    technologies = models.ManyToManyField(Technology,
                                          verbose_name=_("technologies"),
                                          related_name='courses',
                                          blank=True)
    title = models.CharField(_("title"), max_length=200,
                             help_text=_('Enter the course title'))
    slug = models.SlugField(_("slug"), max_length=200, unique=True)
    overview = models.CharField(_("overview"), max_length=100)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    image = models.ImageField(_('image'), upload_to='courses/images/',)
    load = models.CharField(_('load'),
                            max_length=2,
                            choices=Load.choices,
                            default=Load.LITE)
    period = models.PositiveSmallIntegerField(
        _("period"), help_text='Enter the training period'
    )
    count_projects = models.PositiveSmallIntegerField(_("count projects"), blank=True)
    price_per_mouth = models.PositiveIntegerField(_("price per mouth"))
    price_immediately = models.PositiveIntegerField(_("price immediately"))
    cards = models.ManyToManyField("Card",
                                   verbose_name=_("cards"),
                                   related_name='courses',
                                   blank=True)

    class Meta:
        ordering = ['created']
        verbose_name = _('course')
        verbose_name_plural = _('courses')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"pk": self.pk})

    def get_complexity_full_name(self):
        return self.get_complexity_display()

    def get_load_full_name(self):
        return self.get_load_display()

    def benefit(self):
        total_cost = self.period * self.price_per_mouth
        benefit = total_cost - self.price_immediately
        benefit_percentage = (benefit / total_cost) * 100
        return benefit_percentage


class Card(models.Model):

    title = models.CharField(_("title"), max_length=100)
    course = models.ForeignKey(Course,
                               verbose_name=_("course"),
                               on_delete=models.CASCADE,
                               related_name='courses')
    additional_text = models.TextField(_("additional text"))
    status = models.CharField(_("status"), max_length=10, blank=True)

    class Meta:
        verbose_name = _("card")
        verbose_name_plural = _("cards")

    def __str__(self):
        return self.title
