from typing import List, Literal

from node_hermes_core.depencency import NodeDependency
from node_hermes_core.nodes import GenericNode
from burst_link_protocol import BurstInterfaceC
from hermes_stream_nodes import GenericStreamTransport, SerialStream


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

    def read(self) -> List[bytes]:
        data_read = self.stream_interface.read()
        return self.interface.decode(data_read)

    def deinit(self):
        super().deinit()
