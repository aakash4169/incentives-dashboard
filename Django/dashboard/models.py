# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Deal(models.Model):
    deal_id = models.IntegerField(primary_key=True)
    deal_date = models.DateField()
    incentive = models.FloatField()
    program_deal = models.ForeignKey('Incentiveprogram', models.DO_NOTHING)

    def __str__(self):
        return self.deal_id

    class Meta:
        managed = False
        db_table = 'Deal'


class Dealobjective(models.Model):
    deal_objective = models.ForeignKey(Deal, models.DO_NOTHING, primary_key=True)
    deal_objective_0 = models.CharField(db_column='deal_objective', max_length=250)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'DealObjective'


class Dealtype(models.Model):
    deal_type = models.ForeignKey(Deal, models.DO_NOTHING, primary_key=True)
    deal_type_0 = models.CharField(db_column='deal_type', max_length=250)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'DealType'


class Incentiveprogram(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.program_name

    class Meta:
        managed = False
        db_table = 'IncentiveProgram'


class Programindustryactivity(models.Model):
    activity_program = models.ForeignKey(Incentiveprogram, models.DO_NOTHING, primary_key=True)
    industry_activity = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ProgramIndustryActivity'
        unique_together = (('activity_program', 'industry_activity'),)


class Programindustrysector(models.Model):
    sector_program = models.ForeignKey(Incentiveprogram, models.DO_NOTHING, primary_key=True)
    industry_sector = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'ProgramIndustrySector'
        unique_together = (('sector_program', 'industry_sector'),)







