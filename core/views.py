from django.shortcuts import render_to_response
from django.template import RequestContext

###
# Homepage
###
def homepage(request):
	return render_to_response('core/homepage.html', {}, context_instance=RequestContext(request))