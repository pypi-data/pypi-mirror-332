import pytest
from xml.etree import ElementTree
from embargo_roller.processor import StationXMLProcessor

@pytest.fixture
def sample_input():
    """Sample input XML as a string."""
    return """<FDSNStationXML xmlns="http://www.fdsn.org/xml/station/1" schemaVersion="1.2">
    <Network code="NET1">
        <Station code="STA1">
            <Channel code="CH1" startDate="2020-01-01T00:00:00" endDate="2020-06-01T00:00:00" restrictedStatus="closed"/>
            <Channel code="CH1" startDate="2020-06-01T00:00:00" endDate="2020-12-31T00:00:00" restrictedStatus="closed"/>
            <Channel code="CH2" startDate="2021-01-01T00:00:00" restrictedStatus="open"/>
            <Channel code="CH3" startDate="2020-01-01T00:00:00" endDate="2021-06-01T00:00:00" restrictedStatus="closed"/>
        </Station>
    </Network>
</FDSNStationXML>"""

@pytest.fixture
def expected_output():
    """Expected output XML after processing."""
    return """<ns0:FDSNStationXML xmlns:ns0="http://www.fdsn.org/xml/station/1" schemaVersion="1.2">
	<ns0:Network code="NET1" restrictedStatus="partial">
		<ns0:Station code="STA1" restrictedStatus="partial">
			<ns0:Channel code="CH1" startDate="2020-01-01T00:00:00" endDate="2020-05-01T00:00:00" restrictedStatus="open">
				<ns0:Comment id="1" subject="embargo-roller-20200501">
					<ns0:Value>Open Restriction Epoch due to embargo at: 2020-05-01</ns0:Value>
				</ns0:Comment>
			</ns0:Channel>
			<ns0:Channel code="CH1" startDate="2020-05-01T00:00:00" endDate="2020-06-01T00:00:00" restrictedStatus="closed">
				<ns0:Comment id="2" subject="embargo-roller-20200501">
					<ns0:Value>Closed Restriction Epoch due to embargo at: 2020-05-01</ns0:Value>
				</ns0:Comment>
			</ns0:Channel>
			<ns0:Channel code="CH1" startDate="2020-06-01T00:00:00" endDate="2020-12-31T00:00:00" restrictedStatus="closed" />
			<ns0:Channel code="CH2" startDate="2021-01-01T00:00:00" restrictedStatus="open" />
			<ns0:Channel code="CH3" startDate="2020-01-01T00:00:00" endDate="2020-05-01T00:00:00" restrictedStatus="open">
				<ns0:Comment id="3" subject="embargo-roller-20200501">
					<ns0:Value>Open Restriction Epoch due to embargo at: 2020-05-01</ns0:Value>
				</ns0:Comment>
			</ns0:Channel>
			<ns0:Channel code="CH3" startDate="2020-05-01T00:00:00" endDate="2021-06-01T00:00:00" restrictedStatus="closed">
				<ns0:Comment id="4" subject="embargo-roller-20200501">
					<ns0:Value>Closed Restriction Epoch due to embargo at: 2020-05-01</ns0:Value>
				</ns0:Comment>
			</ns0:Channel>
		</ns0:Station>
	</ns0:Network>
</ns0:FDSNStationXML>
"""

def normalize_xml(xml_string):
    """Helper to normalize XML for comparison by removing whitespace and canonicalizing structure."""
    root = ElementTree.fromstring(xml_string)
    ElementTree.indent(root, space="\t", level=0)  # Optional, keeps pretty print formatting
    return ElementTree.tostring(root, encoding='unicode')

def test_station_xml_processor(sample_input, expected_output, tmp_path):
    """Test the StationXMLProcessor for splitting and merging channels."""
    # Write the sample input to a temporary file
    input_file = tmp_path / "input.xml"
    input_file.write_text(sample_input)

    # Initialize the processor with the embargo date
    processor = StationXMLProcessor(embargo_date="2020-05-01")

    # Process the file
    processor.process_file(input_file.open("r"), inplace=True)

    # Read the output and compare with the expected output
    output_xml = input_file.read_text()

    # Normalize and compare the XML strings
    normalized_output = normalize_xml(output_xml)
    normalized_expected = normalize_xml(expected_output)

    # Assert equality with normalized XML
    assert normalized_output == normalized_expected, f"Processed XML did not match expected output.\n\nOutput:\n{normalized_output}\n\nExpected:\n{normalized_expected}"
