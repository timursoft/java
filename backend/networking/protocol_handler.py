from backend.utils.logger import logger

class ProtocolHandler:
    def __init__(self) -> None:
        self.acknowledged_packets = {}

    def handle_incoming_data(self, data: bytes, address: tuple[str, int]) -> None:
        logger.info('Handling data from {}:{}'.format(*address))
        # Process and acknowledge data
        if self.is_acknowledgment(data):
            self.acknowledged_packets[data] = True
            logger.info('Acknowledgment received for packet from {}:{}'.format(*address))
        else:
            # Process the data
            self.send_acknowledgment(data, address)

    def send_acknowledgment(self, data: bytes, address: tuple[str, int]) -> None:
        ack_packet = self.create_ack_packet(data)
        # Simulated send function
        logger.info('Sending acknowledgment to {}:{}'.format(*address))

    def is_acknowledgment(self, data: bytes) -> bool:
        # Determine if the data is an acknowledgment packet
        return data.startswith(b'ACK')

    def create_ack_packet(self, data: bytes) -> bytes:
        # Create an acknowledgment packet
        return b'ACK' + data