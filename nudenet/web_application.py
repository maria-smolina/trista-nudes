import nudenet.predictor as predictor
from urllib.error import HTTPError
from aiohttp import web

async def ping(request):
    return web.Response(text="pong")

async def check_image(request):
    url = request.rel_url.query.get('url', '')
    if not url:
        return web.HTTPBadRequest(text='url param is required')
    try:
        result = predictor.predict_web_image(url)
    except HTTPError:
        raise web.HTTPBadRequest(text='file downloading error')
    return web.Response(text=str(result))

if __name__ == '__main__':
    app = web.Application()
    app.router.add_route('GET', "/ping", ping)
    app.router.add_route('GET', "/checkImage", check_image)
    web.run_app(app)