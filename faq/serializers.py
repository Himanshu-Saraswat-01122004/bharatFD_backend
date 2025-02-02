from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def to_representation(self, instance):
        lang = self.context.get('lang', 'en')
        data = super().to_representation(instance)
        data['question'] = instance.get_translated_question(lang)
        data['answer'] = instance.get_translated_answer(lang)
        return data