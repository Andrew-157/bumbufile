from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table


def progress() -> Progress:
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    )

def print_dict_as_table(
   table_title: str,
   key_column_name: str,
   value_column_name: str,
   source: dict,
) -> None:
    table = Table(title=table_title)
    table.add_column(key_column_name, justify="right", style="cyan", no_wrap=True)
    table.add_column(value_column_name, justify="right", style="green")
    for k, v in source.items():
        table.add_row(str(k), str(v))
    console = Console()
    console.print(table)

def print_error(err: str) -> None:
    raise NotImplementedError
