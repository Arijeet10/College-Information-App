from django.db import models    #import models method from django.db library
from django import forms    #import forms method from django library

########  COLLEGE DETAILS MODEL  ########

#College List
class clgdetails(models.Model):
    College_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255,unique=True)
    Address=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    Contact_no=models.BigIntegerField()
    Affiliation=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    Hostel_facility=models.CharField(max_length=100)
    Ratings=models.IntegerField()
    class Meta:
        db_table="College Details"  #database table name

#clgdetails model form
class clgdetails_forms(forms.ModelForm):
    model=clgdetails
    fields="__all__"

######  END ######

######## COURSE MODEL  ########

#College Courses
class courses(models.Model):
    Course_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Duration=models.CharField(max_length=100)
    Course_Description=models.CharField(max_length=255,default="Working")
    Course_fees=models.BigIntegerField()
    College_ID=models.ForeignKey(clgdetails,db_column='College_ID',to_field='College_ID',related_name='+',default=0, on_delete=models.CASCADE)
    class Meta:
        db_table="Course Details"   #database table name

#courses model form
class courses_form(forms.ModelForm):
    model=courses
    fields="__all__"

######  END  ######

########  SEATS MODEL  ########

#Available Seats
class seats(models.Model):
    Course_ID=models.ForeignKey(courses,db_column='Course_ID',to_field='Course_ID',related_name='+',default=0,on_delete=models.CASCADE)
    College_ID=models.ForeignKey(clgdetails,db_column='College_ID',to_field='College_ID',related_name='+',default=0, on_delete=models.CASCADE)
    Department=models.CharField(max_length=100,default=0)
    seats_no=models.BigIntegerField()
    class Meta:
        db_table="Available Seats"  #database table name

#seats model form
class seats_form(forms.ModelForm):
    model=seats
    fields="__all__"

#######  END  ######

#EXAMS
class exams(models.Model):
    Exam_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Date=models.DateField()
    Exam_Description=models.CharField(max_length=255,default="Working")
    Exam_fees=models.BigIntegerField()
    class Meta:
        db_table="Exam Details"   #database table name

#courses model form
class exams_form(forms.ModelForm):
    model=exams
    fields="__all__"



#College Admissions
class clg_link(models.Model):
    sn=models.AutoField(primary_key=True)
    Name=models.ForeignKey(clgdetails,db_column='Name',to_field='Name',related_name='+',default=0, on_delete=models.CASCADE)
    link=models.CharField(max_length=255)
    class Meta:
        db_table="College admissions"   #database table name

#college admissions model form
class clgadmi_form(forms.ModelForm):
    model=clg_link
    fields="__all__"


'''
#Create new user model
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname
'''

