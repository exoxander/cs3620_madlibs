from django.db import models

class Story(models.Model):

    def Format(self , inputWords):
        result = ""

        #chunks seperated by input spots
        sections = self.words.split("<>")

        #rebuild string with input spots filled
        for i in sections:
            result += sections[i]
            if(i < len(inputWords)):
                result += inputWords[i]
            else:
                result += "<#>"

        return result

    def __str__(self):
        return self.words

    words = models.CharField(max_length=1024)
