from xml.etree.ElementTree import Element
from embargo_roller.utils import  parse_date, elements_equal, get_element_characteristics

def test_elements_equal():
    e1 = Element("channel", attrib={"code": "CH1"})
    e2 = Element("channel", attrib={"code": "CH1"})
    assert elements_equal(e1, e2), "Identical elements should be equal"

    # Different tags
    e3 = Element("station", attrib={"code": "CH1"})
    assert not elements_equal(e1, e3), "Different tags should not be equal"

def test_get_element_characteristics():
    # Test Case 1: Valid Input with Both Attributes
    e1 = Element("channel", attrib={"code": "CH1", "startDate": "2024-01-01T00:00:00"})
    result = get_element_characteristics(e1)
    assert result == ("CH1", parse_date("2024-01-01T00:00:00")), "Should return correct code and parsed startDate"

    # Test Case 2: Missing `startDate` Attribute
    e2 = Element("channel", attrib={"code": "CH2"})
    result = get_element_characteristics(e2)
    assert result == ("CH2", None), "Should handle missing startDate and return None"

    # Test Case 3: Missing `code` Attribute
    e3 = Element("channel", attrib={"startDate": "2024-02-01T00:00:00"})
    try:
        get_element_characteristics(e3)
        assert False, "Should raise KeyError if 'code' attribute is missing"
    except KeyError:
        pass  # Expected behavior
    