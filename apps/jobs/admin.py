from django.contrib import admin

from .models import Company, Manager, Worker, Skill, Position, Offer, TimeSheet


class WorkerSkillInline(admin.TabularInline):
    model = Worker.skills.through


class WorkerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [WorkerSkillInline]


class PositionSkillInline(admin.TabularInline):
    model = Position.skills.through


class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [PositionSkillInline]


admin.site.register(Company)
admin.site.register(Manager)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Skill)
admin.site.register(Position, PositionAdmin)
admin.site.register(Offer)
admin.site.register(TimeSheet)
