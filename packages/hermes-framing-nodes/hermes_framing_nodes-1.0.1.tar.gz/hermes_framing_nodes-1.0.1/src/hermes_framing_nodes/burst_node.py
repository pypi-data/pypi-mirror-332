from typing import List, Literal

from node_hermes_core.depencency import NodeDependency
from node_hermes_core.nodes import GenericNode
from burst_link_protocol import BurstInterfaceC
from hermes_stream_nodes import GenericStreamTransport, SerialStream
from .packet_counter import PacketStatistics, PacketStatisticsManager

class BurstLinkNode(GenericNode):
    class Config(GenericNode.Config):
        type: Literal["bust-link"] = "bust-link"

        stream: str | SerialStream.Config

    config: Config

    def __init__(self, config: Config):
        super().__init__(config)
        self.config = config
        self.base_dependency = NodeDependency(name="interface", config=config.stream, reference=SerialStream)
        self.dependency_manager.add(self.base_dependency)

    def init(self, interface: GenericStreamTransport):  # type: ignore
        super().init()
        self.stream_interface = interface
        self.interface = BurstInterfaceC()
        self.statistics = PacketStatisticsManager()

    def deinit(self):
        super().deinit()
        self.stream_interface = None
        self.interface = None
                
    def read(self) -> List[bytes]:
        data_read = self.stream_interface.read()
        
        packets =  self.interface.decode(data_read)

        if self.statistics is not None:
            self.statistics.register_rx_packets(len(packets))
        
        return packets