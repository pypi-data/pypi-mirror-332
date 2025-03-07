from pathlib import Path

from metricks import load_metric


def test_metricks():
    from metricks import load_metric  # noqa


def test_load_metric():
    path = Path(__file__).parent / "sample_metrics.yml"
    for metric_name in [
        "mikes.sandwiches.orders_overview",
        "mikes.sandwiches.menu_item_clicks",
        "mikes.sandwiches.menu_item_clicks_by_category",
    ]:
        print(load_metric(path, metric_name))
