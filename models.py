from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Conversation(models.Model):
    title = models.CharField(max_length=255, default="Untitled Conversation")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Message(models.Model):
    SENDER_CHOICES = [
        ('user', 'User'),
        ('ai', 'AI'),
    ]
    
    conversation = models.ForeignKey(
        Conversation, 
        on_delete=models.CASCADE, 
        related_name="messages"
    )
    sender = models.CharField(max_length=20, choices=SENDER_CHOICES)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"{self.sender}: {self.text[:50]}..."


class ConversationAnalysis(models.Model):
    SENTIMENT_CHOICES = [
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    ]
    
    conversation = models.OneToOneField(
        Conversation,
        on_delete=models.CASCADE,
        related_name="analysis"
    )
    
    clarity_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="How clear and understandable the responses were (0-10)"
    )
    relevance_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="How relevant the AI responses were to user queries (0-10)"
    )
    accuracy_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Factual correctness of responses (0-10)"
    )
    completeness_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Whether AI provided complete answers (0-10)"
    )
    
    sentiment = models.CharField(
        max_length=20, 
        choices=SENTIMENT_CHOICES,
        help_text="Overall user sentiment"
    )
    empathy_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="How empathetic the AI was when needed (0-10)"
    )
    avg_response_time = models.FloatField(
        help_text="Average response time in seconds",
        null=True,
        blank=True
    )
    
    resolution = models.BooleanField(
        help_text="Was the user's issue resolved?"
    )
    escalation_needed = models.BooleanField(
        help_text="Should this be escalated to a human agent?"
    )
    
    fallback_frequency = models.IntegerField(
        default=0,
        help_text="Number of times AI used fallback responses"
    )
    coherence_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Logical flow and coherence of conversation (0-10)"
    )
    
    politeness_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="How polite and professional the AI was (0-10)"
    )
    
    overall_score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Overall satisfaction score (0-10)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Conversation Analyses"
    
    def __str__(self):
        return f"Analysis for {self.conversation.title} - Score: {self.overall_score}"
