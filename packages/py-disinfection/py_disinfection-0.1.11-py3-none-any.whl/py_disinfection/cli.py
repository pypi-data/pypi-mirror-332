"""Console script for py_disinfection."""

import json

import typer
from rich.console import Console

from py_disinfection.core import (
    CTReqEstimator,
    DisinfectantAgent,
    DisinfectionSegment,
    DisinfectionSegmentOptions,
    EnumEncoder,
)

app = typer.Typer(
    name="disinfect",
    help="A command-line tool for drinking water disinfection analysis.",
)
console = Console()


def convert_temperature(temp: float, unit: str) -> float:
    """Convert Fahrenheit to Celsius if needed."""
    if unit.lower() == "f":
        return (temp - 32) * 5.0 / 9.0
    return temp


@app.command()
def analyze_segment(
    volume: float = typer.Option(..., "-v", "--volume", help="Volume in gallons"),
    temp: float = typer.Option(..., "-t", "--temp", help="Temperature value"),
    temp_unit: str = typer.Option(
        "C", "-u", "--temp-unit", help="Temperature unit: C or F"
    ),
    ph: float = typer.Option(..., "-p", "--ph", help="pH level"),
    chlorine: float = typer.Option(
        ..., "-c", "--concentration", help="Disinfectant concentration in mg/L"
    ),
    method: str = typer.Option(
        ...,
        "-m",
        "--method",
        help="Estimation method: conservative, interpolation, regression",
    ),
    agent: str = typer.Option(
        ...,
        "-a",
        "--agent",
        help="Disinfectant agent: free_chlorine, chlorine_dioxide, chloramines",
    ),
    baffling_factor: float = typer.Option(
        ..., "-b", "--baffling-factor", help="Baffling factor (0-1)"
    ),
    peak_flow: float = typer.Option(
        ..., "-f", "--peak-flow", help="Peak hourly flow in gallons per minute"
    ),
    json_output: bool = typer.Option(
        False, "--json", help="Print output in JSON format"
    ),
) -> None:
    """Analyze a disinfection segment and print results."""
    if method not in {"conservative", "interpolation", "regression"}:
        console.print(
            "[red]Invalid method. Use 'conservative', 'interpolation', or 'regression'.[/red]"
        )
        return

    if agent not in {"free_chlorine", "chlorine_dioxide", "chloramines"}:
        console.print(
            "[red]Invalid agent. Use 'free_chlorine', 'chlorine_dioxide', or 'chloramines'.[/red]"
        )
        return

    agent_enum = DisinfectantAgent[agent.upper()]
    method_enum = CTReqEstimator[method.upper()]
    temp_celsius = convert_temperature(temp, temp_unit)
    results = None
    try:
        options = DisinfectionSegmentOptions(
            volume_gallons=volume,
            agent=agent_enum,
            temperature_celsius=temp_celsius,
            ph=ph,
            concentration_mg_per_liter=chlorine,
            ctreq_estimator=method_enum,
            baffling_factor=baffling_factor,
            peak_hourly_flow_gallons_per_minute=peak_flow,
        )

        segment = DisinfectionSegment(options)

        results = segment.analyze()
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        return None

    if json_output:
        jparams = json.loads(json.dumps(options, cls=EnumEncoder))
        jparams["temp_fahrenheit"] = temp_celsius * 9 / 5 + 32
        total_results = {"parameters": jparams, "results": results}
        console.print(json.dumps(total_results, indent=4))
    else:
        console.print("[bold yellow]Segment Parameters:[/bold yellow]")
        for key, value in options.__dict__.items():
            console.print(f"{key}: [cyan]{value}[/cyan]")

        console.print("\n[bold green]Disinfection Analysis Results:[/bold green]")
        for key, value in results.items():
            console.print(f"{key}: [cyan]{value}[/cyan]")


if __name__ == "__main__":
    app()
