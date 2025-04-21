from .customers import router as customer_router
from .layouts import router as layout_router
from .plots import router as plots_router
from .crops import router as crops_router
from .pricing import router as pricing_router
from .plot_history import router as plot_transactions_router

__routes__ = [
    customer_router,
    layout_router,
    plots_router,
    crops_router,
    pricing_router,
    plot_transactions_router
]