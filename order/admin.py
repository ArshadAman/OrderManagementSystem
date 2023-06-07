from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Order, Mesurement
admin.site.register(Order)


class MeasurementAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Customer Details', {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'order'),
        }),
        ('Blazer/Jacket Mesurement', {
            'fields': ('display_blazer_image', 'front_length', 'shoulder', 'sleeves', 'chest', 'waist', 'hip', 'crossfront', 'crossback', 'sherwani_vest', 'slits', 'Blazer_Jacket_Additional_Information','jacket_order_quantity', 'Blazer_sample_cloth_image'),
        }),
        ('Kurta/Shirts Mesurement', {
            'fields': ('display_kurta_image', 'kurta_front_length', 'kurta_shoulder', 'kurta_sleeves', 'kurta_chest', 'kurta_waist', 'kurta_hip', 'kurta_sleeves_opening', 'kurta_biceps', 'kurta_Cut_Choices', 'kurta_Style_Choices', 'kurta_Neck_Choices', 'kurta_Collor_Choices', 'Kurta_Shirt_Additional_Information',"kurta_order_quantity", 'Kurta_sample_cloth_image'),
        }),
        ('Trouser Mesurement', {
            'fields': ('display_trouser_image', 'Trouser_length', 'Trouser_inseam', 'Trouser_bottom', 'Trouser_knee', 'Trouser_thigh', 'Trouser_waist', 'Trouser_hips', 'Trouser_rounding', 'Rise_Choices', 'front_Down', 'Pleat_Choices', 'Belt_Choices', 'Pocket_Choices', 'Watch_Pocket_Choices', 'Watch_Pocket_Number', 'Mobile_Pockets', 'pocketSize', 'Trouser_Additional_Information',"trouser_order_quantity", 'Trouser_sample_cloth_image'),
        }),
    )

    readonly_fields = ('display_blazer_image', 'display_kurta_image', 'display_trouser_image')

    def display_blazer_image(self, obj):
        if obj.blazer_image:
            return mark_safe('<div class="d-flex justify-content-start"><img src="{}" width="340px"/></div>'.format(obj.blazer_image.url))
        else:
            return ''

    def display_kurta_image(self, obj):
        if obj.kurta_image:
            return mark_safe('<div class="d-flex justify-content-start"><img src="{}" width="340px"/></div>'.format(obj.kurta_image.url))
        else:
            return ''

    def display_trouser_image(self, obj):
        if obj.trouser_image:
            return mark_safe('<div class="d-flex justify-content-start"><img src="{}" width="340px"/></div>'.format(obj.trouser_image.url))
        else:
            return ''

    display_blazer_image.short_description = 'Blazer/Jacket Mesurement'
    display_kurta_image.short_description = 'Kurta/Shirts Mesurement'
    display_trouser_image.short_description = 'Trouser Mesurement'

admin.site.register(Mesurement, MeasurementAdmin)
