from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
#...
 
def test_redirect(request):
    return HttpResponseRedirect("polls/")