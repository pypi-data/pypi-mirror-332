from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from embargo_roller.utils import parse_date, get_element_characteristics
import copy
from embargo_roller.logger import setup_logger
logger = setup_logger(__name__)



class StationXMLProcessor:
    def __init__(self, embargo_date):
        self.embargo_date = parse_date(embargo_date)
        self.ns = {'stationxml': 'http://www.fdsn.org/xml/station/1'}
    
    def process_file(self, file, inplace):
        root = ElementTree.parse(file)
        self._process_channels(root)
        self._save_file(root, file, inplace)
        logger.info("File processing complete.")
    
    def _process_channels(self, root):
        for net in root.findall('.//stationxml:Network', self.ns):
            logger.debug(f"Entering Network: {net.attrib['code']}")
            for sta in net.findall('./stationxml:Station', self.ns):
                logger.debug(f"Entering Station: {net.attrib['code']}_{sta.attrib['code']}")
                self._process_station(sta, net)
    
    def _process_station(self, station, network):
        """
        Processes a <Station> element by applying embargo rules to its child <Channel> elements 
        and merging channels if eligible.

        Parameters:
            station (Element): The <Station> element to process.
            network (Element): The parent <Network> element for inheritance context.
        """
        # Process channels
        for channel in station.findall('./stationxml:Channel', self.ns):
            logger.debug(
                f"Processing Channel: {channel.attrib.get('code', 'N/A')} "
                f"with startDate: {channel.attrib.get('startDate', 'N/A')} "
                f"and endDate: {channel.attrib.get('endDate', 'N/A')} "
                f"under Station: {station.attrib.get('code', 'N/A')}"
            )
            self._process_channel(channel, station, network)
        
        # Merge channels after processing
        self._merge_channels(station)
        # Update parents to 'partial' or 'open'
        self._update_parent_restricted_status(station, network)
        

    
    def _process_channel(self, channel, station, network):
        """
        Processes a single <Channel> element, applying embargo rules.
        """
        def _get_restricted_status(channel, station, network):
            """Determine restrictedStatus with inheritance and fallback."""
            status = next(
                (
                    attr.attrib.get('restrictedStatus')
                    for attr in (channel, station, network)
                    if attr.attrib.get('restrictedStatus') is not None
                ),
                'open'
            )
            return 'closed' if status == 'partial' else status

        # Determine restrictedStatus
        restricted_status = _get_restricted_status(channel, station, network)

        # Parse dates
        start_time = parse_date(channel.attrib.get('startDate'))
        end_time = parse_date(channel.attrib.get('endDate'), default=None)

        # Log key information
        logger.debug(
            f"Channel '{channel.attrib.get('code', 'N/A')}' - "
            f"restrictedStatus: {restricted_status}, startDate: {start_time}, "
            f"embargoDate: {self.embargo_date}, endDate: {end_time}"
        )

        # Skip invalid start times
        if start_time is None:
            logger.warning(f"Invalid or missing 'startDate' for channel: {channel.attrib}")
            return
        # If channel before embargo set it to open restriction
        if end_time and end_time <= self.embargo_date:
            logger.debug(
                f"Channel '{channel.attrib.get('code', 'N/A')}' has endDate ({end_time}) "
                f"before embargoDate ({self.embargo_date}). Setting restrictedStatus to 'open'."
            )
            # Set channel's status to 'open'
            channel.set('restrictedStatus', 'open')
            self._update_parent_restricted_status(station, network)
        # Apply embargo rules
        if restricted_status == 'closed' and start_time < self.embargo_date:
            logger.debug(f"Channel '{channel.attrib.get('code', 'N/A')}' meets split conditions.")
            self._split_channel(channel, station, network)
        else:
            logger.debug(f"Channel '{channel.attrib.get('code', 'N/A')}' does not meet split conditions.")
            # Ensure the channel is added as-is to the station
            if channel not in station:
                station.append(channel)


    def _update_parent_restricted_status(self, station, network):
        """
        Updates or sets the restrictedStatus of parent elements (Station and Network) based on their child elements.
        Ensures that the Network uses the updated restrictedStatus of its Stations.
        """
        def calculate_restricted_status(parent, child_tag):
            """
            Determine the restrictedStatus based on child elements (e.g., Channels for Station or Stations for Network).
            Args:
                parent: The parent element (Station or Network).
                child_tag: The tag of the child elements to evaluate (e.g., 'Channel' or 'Station').

            Returns:
                - 'partial' if at least one child is 'partial' or both 'open' and 'closed' exist.
                - 'closed' if all children are 'closed'.
                - 'open' if all children are 'open'.
                - Defaults to 'open' if no children exist.
            """
            child_elements = parent.findall(f'./stationxml:{child_tag}', self.ns)
            child_statuses = {
                child.attrib.get('restrictedStatus', 'open') for child in child_elements
            }

            # Determine the restrictedStatus based on child statuses
            if 'partial' in child_statuses:
                return 'partial'
            if 'closed' in child_statuses and 'open' in child_statuses:
                return 'partial'
            if 'closed' in child_statuses:
                return 'closed'
            if 'open' in child_statuses:
                return 'open'
            return 'open'  # Default to open if no children are present

        # Update or set restrictedStatus for Station
        new_station_status = calculate_restricted_status(station, 'Channel')
        current_station_status = station.attrib.get('restrictedStatus')
        if current_station_status != new_station_status:
            station.set('restrictedStatus', new_station_status)
            logger.debug(
                f"Station '{station.attrib.get('code', 'N/A')}' restrictedStatus updated "
                f"from '{current_station_status or 'N/A'}' to '{new_station_status}'."
            )

        # After updating all Station restrictedStatus values, calculate Network's status
        new_network_status = calculate_restricted_status(network, 'Station')
        current_network_status = network.attrib.get('restrictedStatus')
        if current_network_status != new_network_status:
            network.set('restrictedStatus', new_network_status)
            logger.debug(
                f"Network '{network.attrib.get('code', 'N/A')}' restrictedStatus updated "
                f"from '{current_network_status or 'N/A'}' to '{new_network_status}'."
            )








    def _split_channel(self, channel, station, network):
        """
        Splits a <Channel> element into two parts at the embargo date.
        Ensures each split part has only one relevant <Comment>, and the comment is the first child.
        """
        embargo_date_str = self.embargo_date.strftime('%Y-%m-%dT%H:%M:%S')
        end_time = parse_date(channel.attrib.get('endDate'), default=None)

        # Might be unnecessary (already checked earlier)
        if end_time and end_time <= self.embargo_date:
            logger.info(
                f"Channel '{channel.attrib['code']}' not split: endDate ({channel.attrib['endDate']}) "
                f"is before embargo date ({embargo_date_str})."
            )
            return

        # Helper to update attributes
        def update_channel_attributes(chan, start=None, end=None, status=None):
            if start:
                chan.set('startDate', start)
            if end:
                chan.set('endDate', end)
            if status:
                chan.set('restrictedStatus', status)

        # Create pre-embargo copy
        cha_before = copy.deepcopy(channel)
        update_channel_attributes(cha_before, end=embargo_date_str, status='open')

        # Update post-embargo channel
        update_channel_attributes(channel, start=embargo_date_str, status='closed')

        # Helper to add embargo comments
        def add_embargo_comment(chan, status):
            """
            Adds a comment to the channel to indicate the embargo action.
            Logs the addition of the comment for debugging purposes.
            """
            new_comment = Element(f"{{{self.ns['stationxml']}}}Comment", {
                "id": "placeholder",  # Temporary placeholder, will be updated later
                "subject": f"embargo-roller-{self.embargo_date.strftime('%Y%m%d')}"
            })
            value = Element(f"{{{self.ns['stationxml']}}}Value")
            value.text = (
                f"Open Restriction Epoch due to embargo at: {self.embargo_date.strftime('%Y-%m-%d')}"
                if status == "open"
                else f"Closed Restriction Epoch due to embargo at: {self.embargo_date.strftime('%Y-%m-%d')}"
            )
            new_comment.append(value)
            chan.insert(0, new_comment)  # Add as the first child

            # Log the addition of the comment
            logger.debug(
                f"Added embargo comment to channel '{chan.attrib.get('code', 'N/A')}' with status '{status}'. "
                f"Subject: {new_comment.attrib['subject']}, Value: {value.text}"
            )

        def ensure_unique_comment_ids(station):
            """
            Ensures all <Comment> elements in the station have unique, incrementing IDs.
            """
            next_id = 1  # Start ID sequence

            for comment in station.findall(f".//{{{self.ns['stationxml']}}}Comment"):
                comment.set("id", str(next_id))
                next_id += 1

            logger.debug(f"Updated all comment IDs in station '{station.attrib.get('code', 'N/A')}'.")


    # Add embargo comments to both parts
        add_embargo_comment(cha_before, "open")
        add_embargo_comment(channel, "closed")

        # Reconstruct the station's channel list to preserve order
        new_channels = []
        for chan in station.findall('./stationxml:Channel', self.ns):
            if chan is channel:
                # Insert the open epoch first, followed by the closed epoch
                new_channels.append(cha_before)
                new_channels.append(channel)
            else:
                # Retain other channels as-is
                new_channels.append(chan)

        # Clear and update the station's channels
        for elem in station.findall('./stationxml:Channel', self.ns):
            station.remove(elem)
        for new_chan in new_channels:
            station.append(new_chan)


        ensure_unique_comment_ids(station)

        
        logger.info(
            f"Channel '{channel.attrib['code']}' split at {embargo_date_str} "
            f"into open and closed epochs."
        )



    def _merge_channels(self, station):
        """
        Improved algorithm to merge contiguous identical channels in a station.
        Ensures all channels are processed and output is sorted by 'code' and 'startDate'.
        """
        # Preserve station attributes
        station_attributes = dict(station.attrib)

        # Extract non-channel elements
        non_channel_elements = [
            el for el in station if el.tag != f"{{{self.ns['stationxml']}}}Channel"
        ]

        # Extract and sort channel elements
        channels = station.findall('./stationxml:Channel', self.ns)
        def ensure_unique_comment_ids(station):
            """
            Ensures all <Comment> elements in the station have unique, incrementing IDs.
            """
            next_id = 1  # Start ID sequence

            for comment in station.findall(f".//{{{self.ns['stationxml']}}}Comment"):
                comment.set("id", str(next_id))
                next_id += 1

            logger.debug(f"Updated all comment IDs in station '{station.attrib.get('code', 'N/A')}'.")
        def channel_sort_key(channel):
            return (
                channel.attrib.get('code', '').lower(),
                parse_date(channel.attrib.get('startDate'))
            )

        channels.sort(key=channel_sort_key)

        logger.debug("--- Debugging _merge_channels: Sorted Input ---")
        for idx, channel in enumerate(channels):
            logger.debug(f"Channel {idx}: {channel.attrib}")
        logger.debug("---------------------------------------------")

        # Initialize the output list and the current merged channel
        output_channels = []
        merged_channel = None
        
        for channel in channels:
            if merged_channel is None:
                # Start a new merged channel
                merged_channel = channel
            elif self._can_merge(merged_channel, channel):
                # Merge the current channel into the merged_channel
                logger.debug(f"Merging Channel '{channel.attrib['code']}' into Merged Channel '{merged_channel.attrib['code']}'")
                merged_channel.attrib['endDate'] = channel.attrib['endDate']

                # Merge comments
                for comment in channel.findall(f"{{{self.ns['stationxml']}}}Comment"):
                    if not any(
                        existing.attrib.get('subject') == comment.attrib.get('subject')
                        for existing in merged_channel.findall(f"{{{self.ns['stationxml']}}}Comment")
                    ):
                        merged_channel.insert(0,comment)
            else:
                # Add the current merged channel to the output
                output_channels.append(merged_channel)
                # Start a new merged channel with the current channel
                merged_channel = channel

        # Add the final merged channel to the output
        if merged_channel:
            output_channels.append(merged_channel)

        # Clear and reconstruct the station
        station.clear()
        station.attrib.update(station_attributes)
        station.extend(non_channel_elements)
        station.extend(output_channels)
        ensure_unique_comment_ids(station)
        logger.debug("--- Final Merged and Sorted Channels ---")
        for idx, c in enumerate(output_channels):
            logger.debug(f"Channel {idx}: {c.attrib}")
        logger.debug("-----------------------------------------")








    
    

    def _can_merge(self, prev_element, current_element):
        """
        Check if two channels can be merged.
        Conditions:
        1. End date of the previous element matches the start date of the current element.
        2. Attributes (excluding 'startDate', 'endDate', and comments) match.
        3. Both elements contain a valid embargo-related comment with 'id' starting with 'embargo-roller'.
        """
        def attributes_match_except_dates(elem1, elem2):
            """Compare attributes, ignoring 'startDate' and 'endDate'."""
            return all(
                elem1.attrib.get(k) == elem2.attrib.get(k)
                for k in elem1.attrib.keys() - {'startDate', 'endDate'}
            )

        def has_valid_embargo_comment(element):
            """Check if the element has a valid embargo-related comment."""
            comment = element.find("stationxml:Comment", self.ns)
            if comment is not None:
                return comment.attrib.get("subject", "").startswith("embargo-roller")
            return False

        # Temporal alignment
        end_date_match = prev_element.attrib.get('endDate') == current_element.attrib.get('startDate')

        # Attribute comparison
        restricted_status_match = prev_element.attrib.get('restrictedStatus') == current_element.attrib.get('restrictedStatus')
        attributes_match = attributes_match_except_dates(prev_element, current_element)

        # Embargo comment validation
        comments_valid = has_valid_embargo_comment(prev_element) and has_valid_embargo_comment(current_element)

        # Log debug information
        logger.debug(
            f"_can_merge: end_date_match={end_date_match}, restricted_status_match={restricted_status_match}, "
            f"attributes_match={attributes_match}, comments_valid={comments_valid}"
        )

        # Merge is allowed if all conditions are met
        return end_date_match and restricted_status_match and attributes_match and comments_valid



    
    def _save_file(self, root, file, inplace):
        ElementTree.indent(root, space="\t", level=0)
        if inplace:
            path = file.name
            file.close()
            with open(path, 'wb') as f:
                root.write(f)
            logger.info(f"File saved in place: {path}")
        else:
            ElementTree.dump(root)
            logger.info("File output dumped to console.")
