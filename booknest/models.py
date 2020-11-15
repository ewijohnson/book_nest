from django.db import models
from datetime import datetime


class MainEntry(models.Model):
    main_entry_id = models.AutoField(primary_key=True)
    main_entry_name = models.CharField(max_length=255)
    main_entry_date = models.CharField(max_length=255, blank=True, default='')
    main_entry_identifier = models.CharField(max_length=255, blank=True, default='')
    main_entry_role = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Main Entry'
        verbose_name_plural = 'Main Entries'
        unique_together = ('main_entry_name', 'main_entry_date', 'main_entry_identifier', 'main_entry_role')


class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    work_title = models.CharField(max_length=255)
    work_title_var = models.CharField(max_length=255, blank=True, default='')
    main_entry = models.ForeignKey(MainEntry, related_name='works', blank=True, default='', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('work_title', 'main_entry')


class Series(models.Model):
    series_id = models.AutoField(primary_key=True)
    series_title = models.CharField(max_length=255)
    series_date = models.CharField(max_length=255, blank=True, default='')
    series_author = models.CharField(max_length=255, blank=True, default='')
    series_author_date = models.CharField(max_length=255, blank=True, default='')
    series_author_identifier = models.CharField(max_length=255, blank=True, default='')
    series_issn = models.CharField(max_length=9, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Series'


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_added = models.CharField(max_length=255)
    subject_added_subfield1 = models.CharField(max_length=255, blank=True, default='')
    subject_added_subfield2 = models.CharField(max_length=255, blank=True, default='')
    subject_added_subfield3 = models.CharField(max_length=255, blank=True, default='')
    subject_added_subfield4 = models.CharField(max_length=255, blank=True, default='')
    subject_added_type = models.CharField(max_length=100)

    class Meta:
        unique_together = ('subject_added', 'subject_added_subfield1', 'subject_added_subfield2',
                           'subject_added_subfield3', 'subject_added_subfield4', 'subject_added_type')


class AddedEntry(models.Model):
    added_entry_id = models.AutoField(primary_key=True)
    added_entry_name = models.CharField(max_length=255)
    added_entry_date = models.CharField(max_length=255, blank=True, default='')
    added_entry_identifier = models.CharField(max_length=255, blank=True, default='')
    added_entry_type = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Added Entry'
        verbose_name_plural = 'Added Entries'
        unique_together = ('added_entry_name', 'added_entry_date', 'added_entry_identifier', 'added_entry_type')


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=13, blank=True, default='')
    book_issn = models.CharField(max_length=9, blank=True, default='')
    book_language = models.CharField(max_length=50, blank=True, default='')
    book_lc_callno = models.CharField(max_length=50, blank=True, default='')
    book_ddc_callno = models.CharField(max_length=50, blank=True, default='')
    book_edition = models.CharField(max_length=255, blank=True, default='')
    book_publication_place = models.CharField(max_length=100, blank=True, default='')
    book_publication_name = models.CharField(max_length=100, blank=True, default='')
    book_publication_date = models.CharField(max_length=50, blank=True, default='')
    book_copyright_date = models.CharField(max_length=50, blank=True, default='')
    book_current_publication_freq = models.CharField(max_length=100, blank=True, default='')
    book_previous_publication_freq = models.CharField(max_length=100, blank=True, default='')
    book_physical_extent = models.CharField(max_length=100, blank=True, default='')
    book_physical_details = models.CharField(max_length=100, blank=True, default='')
    book_physical_dimensions = models.CharField(max_length=100, blank=True, default='')
    book_accompanying_materials = models.CharField(max_length=100, blank=True, default='')
    book_note_gen = models.TextField(blank=True, default='')
    book_note_bib = models.TextField(blank=True, default='')
    book_note_contents = models.TextField(blank=True, default='')
    book_series_vol_num = models.CharField(max_length=50, blank=True, default='')
    work = models.ForeignKey(Work, related_name='books', on_delete=models.PROTECT)
    series = models.ForeignKey(Series, related_name='books', blank=True, default='', on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, related_name='books', blank=True, default='', on_delete=models.PROTECT)
    added_entry = models.ForeignKey(AddedEntry, related_name='books', blank=True, default='', on_delete=models.PROTECT)


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255, unique=True)


class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    collection_name = models.CharField(max_length=255, unique=True)
    location = models.ForeignKey(Location, related_name='collections', default='', on_delete=models.PROTECT)


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
    item_owner = models.CharField(max_length=255, blank=True, default='')
    item_receiving_date = models.DateField(blank=True, default=datetime.now)
    item_enum_a = models.CharField(max_length=255, blank=True, default='')
    item_enum_b = models.CharField(max_length=255, blank=True, default='')
    item_enum_c = models.CharField(max_length=255, blank=True, default='')
    item_chron_i = models.CharField(max_length=255, blank=True, default='')
    item_chron_j = models.CharField(max_length=255, blank=True, default='')
    item_chron_k = models.CharField(max_length=255, blank=True, default='')
    item_description = models.CharField(max_length=255, blank=True, default='')
    holding = models.ForeignKey(Holding, related_name='items', on_delete=models.PROTECT)
