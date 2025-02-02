from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

def translate_text(text, dest_lang):
    try:
        return translator.translate(text, dest=dest_lang).text
    except:
        return text

def save_translations(instance):
    instance.question_hi = translate_text(instance.question, 'hi')
    instance.question_bn = translate_text(instance.question, 'bn')
    instance.answer_hi = translate_text(instance.answer, 'hi')
    instance.answer_bn = translate_text(instance.answer, 'bn')

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = RichTextField(blank=True, null=True)  # Hindi
    answer_bn = RichTextField(blank=True, null=True)  # Bengali

    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):
        return self.question
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only on creation
            save_translations(self)
        super().save(*args, **kwargs)