from src.services.web.routes.routes import Routes
from src.services.web.routes.user import user_routes

__routes__ = Routes(routers=(user_routes.router,))
