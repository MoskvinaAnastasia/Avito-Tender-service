from django.contrib import admin

from .models import Bid, Organization, Tender


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created_at', 'updated_at')
    search_fields = ('name', 'description')


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'organization', 'creator',
                    'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('status', 'organization')


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'tender', 'organization', 'creator',
                    'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('status', 'tender', 'organization')
