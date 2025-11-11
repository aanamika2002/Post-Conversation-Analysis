from django.contrib import admin
from .models import Conversation, Message, ConversationAnalysis


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'message_count', 'has_analysis']
    list_filter = ['created_at']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    
    def message_count(self, obj):
        return obj.messages.count()
    message_count.short_description = 'Messages'
    
    def has_analysis(self, obj):
        return hasattr(obj, 'analysis')
    has_analysis.boolean = True
    has_analysis.short_description = 'Analyzed'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'conversation', 'sender', 'text_preview', 'timestamp']
    list_filter = ['sender', 'timestamp']
    search_fields = ['text', 'conversation__title']
    date_hierarchy = 'timestamp'
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Message'


@admin.register(ConversationAnalysis)
class ConversationAnalysisAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'conversation',
        'overall_score',
        'sentiment',
        'resolution',
        'escalation_needed',
        'created_at'
    ]
    list_filter = ['sentiment', 'resolution', 'escalation_needed', 'created_at']
    search_fields = ['conversation__title']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Conversation', {
            'fields': ('conversation',)
        }),
        ('Quality Metrics', {
            'fields': (
                'clarity_score',
                'relevance_score',
                'accuracy_score',
                'completeness_score',
                'coherence_score'
            )
        }),
        ('Interaction Metrics', {
            'fields': (
                'sentiment',
                'empathy_score',
                'politeness_score',
                'avg_response_time'
            )
        }),
        ('Resolution Metrics', {
            'fields': (
                'resolution',
                'escalation_needed',
                'fallback_frequency'
            )
        }),
        ('Overall', {
            'fields': ('overall_score',)
        }),
    )
    
    readonly_fields = ['created_at']
