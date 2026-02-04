from socket import socket, AF_INET, SOCK_DGRAM
from backend.networking.protocol_handler import ProtocolHandler
from backend.config.settings import NETWORK_CONFIG
from backend.utils.logger import logger

class CommunicationService:
    def __init__(self) -> None:
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((NETWORK_CONFIG['host'], NETWORK_CONFIG['port']))
        self.protocol_handler = ProtocolHandler()

    def send_data(self, data: bytes, address: tuple[str, int]) -> None:
        try:
            self.sock.sendto(data, address)
            logger.info('Data sent to {}:{}'.format(*address))
        except Exception as e:
            logger.error('Failed to send data: {}', e)

    def receive_data(self) -> None:
        while True:
            try:
                data, address = self.sock.recvfrom(4096)
                logger.info('Data received from {}:{}'.format(*address))
                self.protocol_handler.handle_incoming_data(data, address)
            except Exception as e:
                logger.error('Failed to receive data: {}', e)