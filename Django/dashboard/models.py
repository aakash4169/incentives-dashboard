from django.db import models

class Deal(models.Model):
    deal_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_position = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.CharField(max_length=75, blank=True, null=True)
    contact_phone = models.CharField(max_length=10, blank=True, null=True)
    new_jobs = models.IntegerField(blank=True, null=True)
    safe_jobs = models.IntegerField(blank=True, null=True)
    capex = models.IntegerField(db_column='capEx', blank=True, null=True)  # Field name made lowercase.
    incentive = models.IntegerField(blank=True, null=True)
    deal_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        managed = False
        db_table = 'Deal'


class Dealprogram(models.Model):
    deal = models.ForeignKey(Deal, models.DO_NOTHING, primary_key=True)
    program = models.ForeignKey('Incentiveprogram', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DealProgram'
        unique_together = (('deal', 'program'),)


class Incentiveprogram(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=200, blank=True, null=True)
    program_description = models.TextField(blank=True, null=True)
    program_objectives = models.TextField(blank=True, null=True)
    contact_email = models.CharField(max_length=75, blank=True, null=True)
    contact_info = models.CharField(max_length=66, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    program_administration_type = models.CharField(max_length=13, blank=True, null=True)
    program_cap = models.CharField(max_length=100, blank=True, null=True)
    program_finish = models.CharField(max_length=20, blank=True, null=True)
    program_start = models.CharField(max_length=20, blank=True, null=True)
    program_specifics = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.program_name

    class Meta:
        managed = False
        db_table = 'IncentiveProgram'


class Programbusinessneeds(models.Model):
    program = models.ForeignKey(Incentiveprogram, models.DO_NOTHING, primary_key=True)
    business_needs = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'ProgramBusinessNeeds'
        unique_together = (('program', 'business_needs'),)


class Programcategory(models.Model):
    program = models.ForeignKey(Incentiveprogram, models.DO_NOTHING, primary_key=True)
    program_category = models.CharField(max_length=27)

    class Meta:
        managed = False
        db_table = 'ProgramCategory'
        unique_together = (('program', 'program_category'),)


class Programgeographicfocus(models.Model):
    program = models.ForeignKey(Incentiveprogram, models.DO_NOTHING, primary_key=True)
    geographic_focus = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ProgramGeographicFocus'
        unique_together = (('program', 'geographic_focus'),)


class Programindustry(models.Model):
    program = models.ForeignKey(Incentiveprogram, models.DO_NOTHING, primary_key=True)
    industry = models.CharField(max_length=72)

    class Meta:
        managed = False
        db_table = 'ProgramIndustry'
        unique_together = (('program', 'industry'),)


class Programtype(models.Model):
    program = models.ForeignKey(Incentiveprogram, models.DO_NOTHING, primary_key=True)
    program_type = models.CharField(max_length=23)

    class Meta:
        managed = False
        db_table = 'ProgramType'
        unique_together = (('program', 'program_type'),)
