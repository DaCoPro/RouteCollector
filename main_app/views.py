from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Temporarily defining my class and adding data here.
class Route:
    def __init__(self, name, grade, description, crag, rock_type, sends, photos, pitches):
        self.name = name
        self.grade = grade
        self.description = description
        self.crag = crag
        self.rock_type = rock_type
        self.pitches = 1
        self.sends = False
        self.photos = False
        

routes = [
    Route(
        'Screaming Yellow Zonkers',
        '5.10b',
        'A very interesting route. It wanders a bit, and has a lot of variation. Zig zag your way up the face to a final steep move below the anchor. Careful lowering off.',
        'Smith Rock', 
        'Basalt',
        1,
        False,
        False
        
    ),
    Route(
        'Cosmos',
        '5.10a',
        'Knob fest. Nubbing galore pepper this plseant face. Crux comes at the top. Makes a good start to Trezlar.',
        'Smith Rock', 
        'Basalt',
        1,
        False,
        False
    ),
    Route(
        'First Kiss',
        '5.7',
        '''
        The First Kiss is a creatively constructed, fully bolted multi-pitch route tucked off in the northern most reaches of the park. The route has five pitches but, by linking the first two pitches, it can be done in four (but not recommended). All anchor stations have two bolts. Be aware that due to the locations of the anchor stations communication can be challenging - especially if there is a breeze blowing and/or if you've linked the first two pitches - and rope drag can be a problem on much of the route.
        The first pitch (5.7) follows a generous collection of bolts up in a fairly straight line past a single high step crux to a fairly comfortable, semi-hanging belay station.
        Pitch two (5.6) continues up an interesting blocky face and on a short arete to an excellent wide belay balcony with a sweet view of the north face of Monkey Face and the Cascade mountains to the west.
        Note: if you chose to link pitches one and two be sure to attempt to use standard length runners at appropriate bolts to minimize rope drag. However, if you link these pitches, no matter how skillfully you might long runner and/or skip bolts you will experience some rope drag.
        Pitch three heads horizontally north slightly down for about 40 feet along a ramp and then turns modestly up left another 40 feet to a fun crux move (5.5) just before the belay station. Plan on substantial rope drag on this nearly horizontal and rounded traverse pitch.
        Pitch four (5.5) traverses up and left into and then up and out of a mossy bowl via a short and fun blocky arete. A short traverse left after the arete leads to a belay station atop a small bolder at the base of an orange-colored, pothole filled wall.
        Pitch five (5.7) heads straight up the wall passing a short left-facing book and then continuing up another fun wall to the finishing anchors. There are two sets of anchor bolts at the top of the climb - the upper set are recommended.
        Descent:
        It is recommended that you do not attempt to rappel this wandering route. Instead, walk off (you did remember to bring your approach shoes with you, didn't you?) by a short scramble above the final anchors to the top of the formation and then carefully down-climbing from the exposed top to a notch. Follow the faint climbers trail that leads to the hikers trail coming down from the mesa. The other option is to pack all of your gear and climb the route "alpine style". Then hike / scramble up to the trail system on the top of the mesa.
        ''',
        'Smith Rock', 
        'Basalt',
        1,
        False,
        False
    )
]
        



# Define the home view
def home(request):
  return render(request, 'home.html')

def routes_index(request):
  return render(request, 'routes/index.html', {'routes': routes})
