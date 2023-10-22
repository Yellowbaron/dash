from dash import html, dcc
from dash_bootstrap_components import Navbar, Container, Nav, NavItem, NavLink
from dash.dependencies import Input, Output

header = html.Header([
    Navbar(
        children=[
            Container(
                fluid=True,
                children=[
                    html.A(
                        "ESO Data Portal",
                        className="navbar-brand",
                        href="/"
                    ),
                    Nav(
                        className="mr-auto",
                        children=[
                            NavItem(
                                NavLink("Подбор товаров на аукцион", href="/auction-selection", id="nav-auction-selection")
                            ),
                            NavItem(
                                NavLink("Оценка стоимости товара на основе истории продаж", href="/price-estimation", id="nav-price-estimation")
                            )
                        ]
                    )
                ]
            )
        ]
    )
])


