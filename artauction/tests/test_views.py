from artauction.views.home import home
from artauction.views.notfound import notfound_view


def test_home(app_request):
    info = home(app_request)
    assert app_request.response.status_int == 200
    assert info['project'] == 'Art Auction House'

def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
