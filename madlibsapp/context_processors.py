from .models import Story

def StoryList(request):
	return {"StoryList": Story.objects.all(),}