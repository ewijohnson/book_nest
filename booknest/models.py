from django.db import models


class MainEntry(models.Model):

    class Meta:
        verbose_name = 'Main Entry'
        verbose_name_plural = 'Main Entries'

    main_entry_id = models.AutoField(primary_key=True)
    main_entry_name = models.CharField(max_length=255, blank=True, default='')
    main_entry_role = models.CharField(max_length=50, blank=True, default='')


class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    work_title = models.CharField(max_length=255, unique=True)
    work_title_var = models.CharField(max_length=255, blank=True, default='')
    main_entry = models.ForeignKey(MainEntry, related_name='works', on_delete=models.PROTECT)


class Publication(models.Model):
    publication_id = models.AutoField(primary_key=True)
    publication_place = models.CharField(max_length=100, blank=True, default='')
    publication_name = models.CharField(max_length=100, blank=True, default='')
    publication_date = models.CharField(max_length=50, blank=True, default='')
    copyright_date = models.CharField(max_length=50, blank=True, default='')
    current_publication_freq = models.CharField(max_length=100, blank=True, default='')
    previous_publication_freq = models.CharField(max_length=100, blank=True, default='')


class PhysicalDescription(models.Model):

    class Meta:
        verbose_name = 'Physical Description'
        verbose_name_plural = 'Physical Descriptions'

    physical_id = models.AutoField(primary_key=True)
    physical_extent = models.CharField(max_length=100, blank=True, default='')
    physical_details = models.CharField(max_length=100, blank=True, default='')
    physical_dimensions = models.CharField(max_length=100, blank=True, default='')
    physical_accomp_mats = models.CharField(max_length=100, blank=True, default='')


class Series(models.Model):

    class Meta:
        verbose_name_plural = 'Series'

    series_id = models.AutoField(primary_key=True)
    series_name = models.CharField(max_length=255, blank=True, default='')
    series_vol_num = models.CharField(max_length=50, blank=True, default='')
    series_issn = models.CharField(max_length=9, blank=True, default='')


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_added = models.CharField(max_length=255, blank=True, default='')
    subject_added_type = models.CharField(max_length=100, blank=True, default='')


class AddedEntry(models.Model):

    class Meta:
        verbose_name = 'Added Entry'
        verbose_name_plural = 'Added Entries'

    added_entry_id = models.AutoField(primary_key=True)
    added_entry_name = models.CharField(max_length=255, blank=True, default='')
    added_entry_type = models.CharField(max_length=255, blank=True, default='')


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=13, blank=True, default='')
    book_issn = models.CharField(max_length=9, blank=True, default='')
    book_language = models.CharField(max_length=50, blank=True, default='')
    book_lc_callno = models.CharField(max_length=50, blank=True, default='')
    book_ddc_callno = models.CharField(max_length=50, blank=True, default='')
    book_edition = models.CharField(max_length=255, blank=True, default='')
    book_note_gen = models.TextField(blank=True, default='')
    book_note_bib = models.TextField(blank=True, default='')
    book_note_contents = models.TextField(blank=True, default='')
    work = models.ForeignKey(Work, related_name='books', on_delete=models.PROTECT)
    publication = models.ForeignKey(Publication, related_name='books', on_delete=models.PROTECT)
    physical_description = models.ForeignKey(PhysicalDescription, related_name='books', on_delete=models.PROTECT)
    series = models.ForeignKey(Series, related_name='books', on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, related_name='books', on_delete=models.PROTECT)
    added_entry = models.ForeignKey(AddedEntry, related_name='books', on_delete=models.PROTECT)


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255, unique=True)


class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    collection_name = models.CharField(max_length=255, unique=True)


class Holding(models.Model):
    holding_id = models.AutoField(primary_key=True)
    holding_units = models.TextField(blank=True, default='')
    holding_supplements = models.TextField(blank=True, default='')
    holding_indexes = models.TextField(blank=True, default='')
    book = models.ForeignKey(Book, related_name='holdings', on_delete=models.PROTECT)
    collection = models.ForeignKey(Collection, related_name='holdings', on_delete=models.PROTECT)


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_barcode = models.IntegerField(blank=True, default='')
    item_callno = models.CharField(max_length=50, blank=True, default='')
    item_copy = models.IntegerField(blank=True, default='')
    holding = models.ForeignKey(Holding, related_name='items', on_delete=models.PROTECT)
