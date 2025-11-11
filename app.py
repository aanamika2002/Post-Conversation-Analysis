from django.apps import AppConfig


class AnalysisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analysis'
    verbose_name = 'Conversation Analysis'
    
    def ready(self):
        # Import signals or other startup code here if needed
        pass
