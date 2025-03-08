import pytest
from embargo_roller.processor import StationXMLProcessor
from xml.etree.ElementTree import Element

@pytest.fixture
def processor():
    """Fixture to initialize a fresh instance of StationXMLProcessor."""
    return StationXMLProcessor(embargo_date="2020-06-01")
# =========================
# Tests for _split_channel
# =========================

def test_split_channel_basic_split(processor):
    """Test a basic split scenario for a channel."""
    # Define the namespace explicitly
    ns = processor.ns['stationxml']

    # Create a station and a channel
    station = Element(f"{{{ns}}}Station")
    network = Element(f"{{{ns}}}Network")
    channel = Element(f"{{{ns}}}Channel", {
        "code": "CH1",
        "startDate": "2020-01-01T00:00:00",
        "endDate": "2020-07-01T00:00:00",
        "restrictedStatus": "closed"
    })
    station.append(channel)

    # Call _split_channel
    processor._split_channel(channel, station, network)

    # Find the pre-embargo channel using the namespace
    pre_embargo = station.findall(f"{{{ns}}}Channel")[0]

    # Check that the pre-embargo channel has the correct attributes
    assert pre_embargo.attrib["endDate"] == "2020-06-01T00:00:00"
    assert pre_embargo.attrib["restrictedStatus"] == "open"

    # Check that the post-embargo channel has the correct attributes
    assert channel.attrib["startDate"] == "2020-06-01T00:00:00"
    assert channel.attrib["restrictedStatus"] == "closed"

    # Validate comments
    comment = pre_embargo.find(f"{{{ns}}}Comment")
    assert comment is not None
    assert comment.attrib["subject"] == "embargo-roller-20200601"

def test_split_channel_no_split(processor):
    station = Element("Station")
    network = Element("Network")
    channel = Element("Channel", {
        "code": "CH1",
        "startDate": "2020-01-01T00:00:00",
        "endDate": "2020-05-01T00:00:00",
        "restrictedStatus": "closed"
    })
    station.append(channel)

    processor._split_channel(channel, station, network)

    # Validate no split occurred
    assert len(station) == 1
    assert station[0] is channel

def test_split_channel_missing_end_date(processor):
    ns = processor.ns['stationxml']
    station = Element(f"{{{ns}}}Station")
    network = Element(f"{{{ns}}}Network")
    channel = Element(f"{{{ns}}}Channel", {
        "code": "CH1",
        "startDate": "2020-01-01T00:00:00",
        "restrictedStatus": "closed"
    })
    station.append(channel)

    # Call _split_channel
    processor._split_channel(channel, station, network)

    # Find the pre-embargo channel using the namespace
    pre_embargo = station.findall(f"{{{ns}}}Channel")[0]
    assert pre_embargo.attrib["endDate"] == "2020-06-01T00:00:00"
    assert pre_embargo.attrib["restrictedStatus"] == "open"

    # Validate post-embargo channel
    assert channel.attrib["startDate"] == "2020-06-01T00:00:00"
    assert "endDate" not in channel.attrib, "The 'endDate' attribute should not exist in channel.attrib"
    assert channel.attrib["restrictedStatus"] == "closed"

def test_split_channel_missing_restricted_status(processor):
    """Test that _split_channel handles a channel without restrictedStatus gracefully."""
    ns = processor.ns['stationxml']
    station = Element(f"{{{ns}}}Station")
    network = Element(f"{{{ns}}}Network")
    channel = Element(f"{{{ns}}}Channel", {
        "code": "CH1",
        "startDate": "2020-01-01T00:00:00",
        "endDate": "2020-07-01T00:00:00"
    })
    station.append(channel)

    # Call _split_channel
    processor._split_channel(channel, station, network)

    # Validate the pre-embargo channel
    pre_embargo = station.findall(f"{{{ns}}}Channel")[0]
    assert pre_embargo.attrib["endDate"] == "2020-06-01T00:00:00", "Pre-embargo channel should have correct endDate"
    assert pre_embargo.attrib["restrictedStatus"] == "open", "Pre-embargo channel should default to 'open'"

    # Validate the post-embargo channel
    post_embargo = channel
    assert post_embargo.attrib["startDate"] == "2020-06-01T00:00:00", "Post-embargo channel should have correct startDate"
    assert post_embargo.attrib["restrictedStatus"] == "closed", "Post-embargo channel should default to 'closed'"

# =========================
# Tests for _can_merge
# =====================
def test_can_merge_success(processor):
    """Test _can_merge for channels that meet merge criteria."""
    # Define the namespace
    ns = "http://www.fdsn.org/xml/station/1"
    stationxml_ns = f"{{{ns}}}"

    # Create previous and current channel elements
    prev_channel = Element(f"{stationxml_ns}Channel", {
        "code": "CH1",
        "endDate": "2020-04-01T00:00:00",
        "restrictedStatus": "open"
    })
    curr_channel = Element(f"{stationxml_ns}Channel", {
        "code": "CH1",
        "startDate": "2020-04-01T00:00:00",
        "restrictedStatus": "open"
    })

    # Add valid embargo comments
    prev_comment = Element(f"{stationxml_ns}Comment", {"id": "1", "subject": "embargo-roller-20200401"})
    curr_comment = Element(f"{stationxml_ns}Comment", {"id": "2", "subject": "embargo-roller-20200401"})
    prev_channel.append(prev_comment)
    curr_channel.append(curr_comment)

    # Assert that the channels can be merged
    assert processor._can_merge(prev_channel, curr_channel) is True


def test_can_merge_mismatched_attributes(processor):
    """Test _can_merge fails due to mismatched attributes."""
    # Define the namespace
    ns = "http://www.fdsn.org/xml/station/1"
    stationxml_ns = f"{{{ns}}}"

    # Create previous and current channel elements
    prev_channel = Element(f"{stationxml_ns}Channel", {
        "code": "CH1",
        "endDate": "2020-04-01T00:00:00",
        "restrictedStatus": "open"
    })
    curr_channel = Element(f"{stationxml_ns}Channel", {
        "code": "CH1",
        "startDate": "2020-04-01T00:00:00",
        "restrictedStatus": "closed"  # Mismatched status
    })

    # Add valid comments with namespace
    prev_comment = Element(f"{stationxml_ns}Comment", {"id": "embargo-roller-20200401", "subject": "epoch split"})
    curr_comment = Element(f"{stationxml_ns}Comment", {"id": "embargo-roller-20200401", "subject": "epoch split"})
    prev_channel.append(prev_comment)
    curr_channel.append(curr_comment)

    # Assert _can_merge returns False due to mismatched restrictedStatus
    assert processor._can_merge(prev_channel, curr_channel) is False

def test_can_merge_invalid_dates(processor):
    """Test _can_merge fails due to mismatched dates."""
    # Define the namespace
    ns = "http://www.fdsn.org/xml/station/1"
    stationxml_ns = f"{{{ns}}}"

    # Create previous and current channel elements
    prev_channel = Element(f"{stationxml_ns}Channel", {
        "code": "CH1",
        "endDate": "2020-03-01T00:00:00",  # Mismatched endDate
        "restrictedStatus": "open"
    })
    curr_channel = Element(f"{stationxml_ns}Channel", {
        "code": "CH1",
        "startDate": "2020-04-01T00:00:00",
        "restrictedStatus": "open"
    })

    # Add valid comments with namespace
    prev_comment = Element(f"{stationxml_ns}Comment", {"id": "embargo-roller-20200401", "subject": "epoch split"})
    curr_comment = Element(f"{stationxml_ns}Comment", {"id": "embargo-roller-20200401", "subject": "epoch split"})
    prev_channel.append(prev_comment)
    curr_channel.append(curr_comment)

    # Assert _can_merge returns False due to mismatched dates
    assert processor._can_merge(prev_channel, curr_channel) is False


def test_can_merge_invalid_comments(processor):
    """Test _can_merge fails due to invalid comments."""
    prev_channel = Element("Channel", {
        "code": "CH1",
        "endDate": "2020-04-01T00:00:00",
        "restrictedStatus": "open"
    })
    curr_channel = Element("Channel", {
        "code": "CH1",
        "startDate": "2020-04-01T00:00:00",
        "restrictedStatus": "open"
    })

    # Add invalid comments
    prev_comment = Element("Comment", {"id": "some-other-id", "subject": "unrelated subject"})
    curr_comment = Element("Comment", {"id": "embargo-roller-20200401", "subject": "epoch split"})
    prev_channel.append(prev_comment)
    curr_channel.append(curr_comment)

    assert processor._can_merge(prev_channel, curr_channel) is False