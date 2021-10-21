from django.views.generic import ListView

from apps.calendarapp.models import Event


class AllEventsListView(ListView):
    """ All event list views """
    template_name = 'apps.calendarapp/events_list.html'
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)


class RunningEventsListView(ListView):
    """ Running events list view """
    template_name = 'apps.calendarapp/events_list.html'
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)
