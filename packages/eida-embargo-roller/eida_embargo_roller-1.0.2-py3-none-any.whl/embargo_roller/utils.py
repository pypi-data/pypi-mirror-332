import pendulum
from embargo_roller.logger import setup_logger

logger = setup_logger(__name__)
def default_embargo(years=2):
    """Returns the first day of /years/ years ago."""
    return pendulum.now().subtract(years=years, days=(pendulum.now().day_of_year - 1)).to_date_string()

def parse_date(date_str, default=None):
    """Parses a date string using Pendulum or returns a default date."""
    try:
        return pendulum.parse(date_str)
    except Exception:
        return default
def elements_equal(e1, e2):
    """
    Compare two XML elements for equality, excluding comments and ignoring 
    'startDate' and 'endDate' attributes during comparison.
    """
    logger.debug(f"Comparing Elements: {e1.tag} vs {e2.tag}")

    # Compare tags, text, and tail
    if (e1.tag != e2.tag or 
        (e1.text or "").strip() != (e2.text or "").strip() or 
        (e1.tail or "").strip() != (e2.tail or "").strip()):
        logger.debug(f"Mismatch found in tag, text, or tail: {e1.tag}")
        return False

    # Compare attributes, ignoring 'startDate' and 'endDate'
    ignored_attributes = {'startDate', 'endDate'}
    if {k: v for k, v in e1.attrib.items() if k not in ignored_attributes} != \
        {k: v for k, v in e2.attrib.items() if k not in ignored_attributes}:
        logger.debug(f"Attributes do not match: {e1.attrib} vs {e2.attrib}")
        return False

    # Filter and compare non-comment children
    def filtered_children(elem):
        return [child for child in elem if child.tag != "Comment"]

    children1, children2 = map(filtered_children, (e1, e2))
    if len(children1) != len(children2):
        logger.debug(f"Child count mismatch: {len(children1)} != {len(children2)}")
        return False

    # Recursively compare children
    return all(elements_equal(c1, c2) for c1, c2 in zip(children1, children2))

def get_element_characteristics(element):
    code = element.attrib.get('code', None)  # Safely get 'code', default to None
    start_date = element.attrib.get('startDate', None)  # Safely get 'startDate', default to None
    
    if not code:
        raise KeyError("'code' attribute is required but missing.")
    
    # If start_date is missing, handle it as None or return a default date
    if start_date:
        start_date = parse_date(start_date)
    else:
        start_date = None  # You can also choose a default date here, e.g., "1970-01-01"
    
    return (code, start_date)
