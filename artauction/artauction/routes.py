def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('art', '/art/{art_id}')
    config.add_route('collection', '/account/collection/{bidder_id}')
    config.add_route('bids', '/account/bids/{bidder_id}')
