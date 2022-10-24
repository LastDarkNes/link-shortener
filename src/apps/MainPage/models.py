from django.db import models
import random, string


class Link(models.Model):
    full_link = models.TextField(verbose_name='full_link')
    short_link = models.TextField(verbose_name='short_link')

    @staticmethod
    def generate_link(chars=string.ascii_uppercase + string.digits):
        short_links = Link.objects.all().values_list('short_link', flat=True)

        while True:
            result = ''.join(random.choice(chars) for _ in range(7))
            if result not in short_links:
                break

        return result

    @staticmethod
    def get_short_link_by_full_link(full_link):
        link, new_link = Link.objects.get_or_create(full_link=full_link)

        if new_link:
            short_link = Link.generate_link()
            new_link = Link.objects.get(full_link=full_link)
            new_link.short_link = short_link
            result = short_link
            new_link.save()
        else:
            result = link.short_link

        return result

