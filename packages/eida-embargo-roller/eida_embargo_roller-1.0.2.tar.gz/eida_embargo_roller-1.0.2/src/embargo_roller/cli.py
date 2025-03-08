import click
import sys
from embargo_roller.processor import StationXMLProcessor
from embargo_roller.utils import default_embargo
from embargo_roller.logger import setup_logger

logger = setup_logger(__name__)

@click.command()
@click.option('-i', '--inplace', is_flag=True, help="Edit StationXML file in place.")
@click.option('-e', '--embargo-date', default=default_embargo(), show_default=True, help="Embargo start date.")
@click.argument('stationxml', type=click.File('rb'))
def cli(inplace, embargo_date, stationxml):
    """
    CLI for processing StationXML file in respect to embargo date.

    Example Usage:
    - Save output to a file: uv run eida_embargo_roller -e 2020-06-01 tests/files/Z3.A190A.xml > result1.xml
    - Process a file in place: uv run eida_embargo_roller -i -e 2020-06-01 tests/files/Z3.A190A.xml
    """
    logger.info(f"Transforming {stationxml.name} to respect embargo starting at {embargo_date}")
    
    # Check if output is redirected
    output_redirected = not sys.stdout.isatty()
    
    if inplace and output_redirected:
        logger.error("Cannot use -i (in-place) with redirected output. Remove -i or avoid redirecting.")
        sys.exit(1)
    
    processor = StationXMLProcessor(embargo_date)
    
    # Process file
    if inplace:
        logger.info(f"Editing {stationxml.name} in place.")
        processor.process_file(stationxml, inplace=True)
    else:
        logger.info(f"Processing {stationxml.name} and outputting the result to output file.")
        processor.process_file(stationxml, inplace=False)
