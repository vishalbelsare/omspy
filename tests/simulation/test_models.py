from omspy.simulation.models import *
import pendulum
import pytest


@pytest.fixture
def vtrade():
    return VTrade(
        trade_id="202310001",
        order_id="20234567812",
        symbol="aapl",
        quantity=50,
        price=120,
        side=Side.BUY,
        timestamp=pendulum.datetime(2023, 1, 2, 7, 10),
    )


@pytest.fixture
def vorder_kwargs():
    return dict(
        order_id="20234567812",
        symbol="aapl",
        quantity=100,
        side=1,
        exchange_timestamp=pendulum.datetime(2023, 1, 2, 7, 10),
    )


def test_vtrade_defaults(vtrade):
    assert vtrade.price == 120
    assert vtrade.side == Side.BUY
    assert vtrade.value == 6000


def test_vorder_defaults(vorder_kwargs):
    vorder = VOrder(**vorder_kwargs)
    assert vorder.quantity == 100
    assert vorder.side == Side.BUY
    assert vorder.status_message is None
    assert vorder.timestamp is not None
    assert vorder.filled_quantity == 0
    assert vorder.pending_quantity == 100
    assert vorder.canceled_quantity == 0
    assert vorder.average_price == 0


def test_vorder_quantities(vorder_kwargs):
    vorder_kwargs["pending_quantity"] = 50
    vorder = VOrder(**vorder_kwargs)
    assert vorder.quantity == 100
    assert vorder.filled_quantity == 50
    assert vorder.pending_quantity == 50
    assert vorder.canceled_quantity == 0

    vorder_kwargs["filled_quantity"] = 100
    vorder = VOrder(**vorder_kwargs)
    assert vorder.quantity == 100
    assert vorder.filled_quantity == 100
    assert vorder.pending_quantity == 0
    assert vorder.canceled_quantity == 0

    vorder_kwargs["canceled_quantity"] = 100
    vorder = VOrder(**vorder_kwargs)
    assert vorder.quantity == 100
    assert vorder.filled_quantity == 0
    assert vorder.pending_quantity == 0
    assert vorder.canceled_quantity == 100


def test_vposition_defaults():
    pos = VPosition(symbol="aapl")
    assert pos.buy_quantity == pos.sell_quantity == 0
    assert pos.buy_value == pos.sell_value == 0


def test_vorder_status(vorder_kwargs):
    order = VOrder(**vorder_kwargs)
    assert order.filled_quantity == 0
    assert order.pending_quantity == 100
    assert order.status == Status.OPEN

    order.filled_quantity = 100
    assert order.status == Status.COMPLETE

    order.filled_quantity = 40
    order.canceled_quantity = 60
    order.pending_quantity = 0
    assert order.status == Status.PARTIAL_FILL

    order.filled_quantity = 40
    order.pending_quantity = 60
    order.canceled_quantity = 0
    assert order.status == Status.PENDING


def test_vorder_status_canceled_rejected(vorder_kwargs):
    order = VOrder(**vorder_kwargs)
    assert order.filled_quantity == 0
    assert order.pending_quantity == 100
    assert order.status == Status.OPEN

    order.filled_quantity = order.pending_quantity = 0
    order.canceled_quantity = 100
    assert order.status == Status.CANCELED

    order.status_message = "REJECTED: no margins"
    assert order.status == Status.REJECTED

    # test with lower case
    order.status_message = "rejected: no margins"
    assert order.status == Status.REJECTED


def test_vtrade_value(vtrade):
    assert vtrade.value == 6000
    vtrade.side = Side.SELL
    vtrade.price = 100
    assert vtrade.value == -5000


def test_vorder_value(vorder_kwargs):
    order = VOrder(**vorder_kwargs)
    order.average_price = 120
    assert order.value == 0
    order.filled_quantity = 50
    assert order.value == 6000
    order.filled_quantity = 100
    assert order.value == 12000
    order.side = -1
    assert order.value == -12000
    assert order.side == Side.SELL
