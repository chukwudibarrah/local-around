# cli.py

import click
from app import create_app
from flask.cli import with_appcontext
from app.services.xml_parser import parse_xml_folder, find_bus_route

@click.command()
@click.option('--start', prompt='Start location', help='Starting point of the journey')
@click.option('--end', prompt='End location', help='End point of the journey')
@with_appcontext
def query_route(start, end):
    """Query route information between two points."""
    app = create_app()
    routes = parse_xml_folder('app/data')
    
    matching_routes = find_bus_route(routes, start, end)
    
    if matching_routes:
        click.echo(f"Routes found from {start} to {end}:")
        for i, route in enumerate(matching_routes, 1):
            click.echo(f"Route {i}:")
            for j, (from_stop, to_stop) in enumerate(route, 1):
                click.echo(f"  {j}. {from_stop} -> {to_stop}")
    else:
        click.echo(f"No route found between {start} and {end}")

if __name__ == '__main__':
    query_route()