from . import viewsets

routeList = (
    (r'days', viewsets.DayViewSet),
    (r'slots', viewsets.SlotViewSet),
)
