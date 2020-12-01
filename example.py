from aiohttp import web
from aiohttp_prometheus import metrics_middleware, MetricsView

app = web.Application()
app.middlewares.append(metrics_middleware)
app.router.add_route('GET', '/metrics', MetricsView)

web.run_app(app)
