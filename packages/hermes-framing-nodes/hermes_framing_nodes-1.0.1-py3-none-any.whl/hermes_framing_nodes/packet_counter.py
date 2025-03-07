import time
from dataclasses import dataclass


@dataclass
class PacketStatistics:
    tx_packets: int = 0
    rx_packets: int = 0
    tx_rate: float = 0  # in packets per second
    rx_rate: float = 0  # in packets per second


class PacketStatisticsManager:
    def __init__(self):
        self.tx_packets = 0
        self.rx_packets = 0
        self.last_rate_update = time.time()
        self.last_stats = PacketStatistics()

    def get_rates(self) -> PacketStatistics:
        now = time.time()

        elapsed = now - self.last_rate_update

        if elapsed < 0.1:
            return self.last_stats

        tx_rate = (self.tx_packets - self.last_stats.tx_packets) / elapsed
        rx_rate = (self.rx_packets - self.last_stats.rx_packets) / elapsed

        self.last_stats = PacketStatistics(
            tx_packets=self.tx_packets,
            rx_packets=self.rx_packets,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
        )

        self.last_rate_update = now

        return self.last_stats

    def register_tx_packets(self, packets: int):
        self.tx_packets += packets

    def register_rx_packets(self, packets: int):
        self.rx_packets += packets
