from typing import List

from rich.table import Table


def get_category_color(category):
    COLORS = {
        "Learn": "cyan2",
        "YouTube": "red",
        "Sports": "cyan",
        "Study": "green",
        "Work": "yellow",
        "Home": "magenta",
        "Other": "blue",
        "Shopping": "green",
        "Personal": "magenta",
    }
    if category in COLORS:
        return COLORS[category]
    return "white"


def create_default_table(colum_names: List[str]) -> Table:
    table = Table(show_header=True, header_style="bold dark_slate_gray2")
    table.add_column("#", style="dim", width=6, justify="center")

    for colum_name in colum_names:
        table.add_column(colum_name, min_width=20, justify="center")
    return table
