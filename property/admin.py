from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ("owner", )


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ("created_at", )
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ("liked_by", )
    fieldsets = (
        (None, {
            'fields': ("created_at", "description", "price", "town", "town_district",
                       "address",  "living_area", "active",
                       "construction_year", "new_building", "liked_by", "owner_pure_phone")
        }),
        ('Описание объекта', {
            'fields': ("rooms_number", "floor", "has_balcony",)
        }),
    )
    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat", "author")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats", )
