from django.contrib import admin
from .models import Student, Track
# Register your models here.

class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['Student Information', {'fields': ['fname','lname','age']}],
        ['Scholarship Information', {'fields': ['student_track']}]
    )

    list_display = ('fname', 'lname', 'age', 'student_track', 'is_graduated')
    list_filter = ['student_track', 'fname']
    search_fields = ['fname', 'student_track__name']

class InlineStudent(admin.StackedInline):
    model = Student
    extra = 3

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]

admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)
