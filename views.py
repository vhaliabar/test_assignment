from courses.models import Course
#from ads.forms import CreateForm, CommentForm
from courses.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from django.shortcuts import render

from django.contrib.humanize.templatetags.humanize import naturaltime
from courses.utils import dump_queries

class CourseListView(View):
    template_name = "courses/course_list.html"
    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval)
            query.add(Q(start__icontains=strval), Q.OR)
            query.add(Q(finish__icontains=strval), Q.OR)
            objects = Course.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            objects = Course.objects.all().order_by('-updated_at')[:10]

        # Augment the post_list
        for obj in objects:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'course_list' : objects, 'search': strval}
        retval = render(request, self.template_name, ctx)

        dump_queries()
        return retval

class CourseDetailView(OwnerDetailView):
    model = Course
    template_name = "courses/course_detail.html"

class CourseCreateView(OwnerCreateView):
    model = Course
    template_name = 'courses/course_form.html'
#    context_object_name = 'courses_list'
    fields = ['title', 'price', 'lectures', 'start', 'finish']


class CourseUpdateView(OwnerUpdateView):
    model = Course
    template_name = 'courses/course_form.html'
    fields = ['title', 'price', 'lectures', 'start', 'finish']


class CourseDeleteView(OwnerDeleteView):
    model = Course
    template_name = 'courses/course_delete.html'

def send_json(request):

    data = [{'Course_title': '{{course.title}}', 'Course_start': '{{course.start}}'},
            {'Course_finish': '{{course.finish}}', 'email': 'julia@example.org'}]

    return JsonResponse(data, safe=False)

