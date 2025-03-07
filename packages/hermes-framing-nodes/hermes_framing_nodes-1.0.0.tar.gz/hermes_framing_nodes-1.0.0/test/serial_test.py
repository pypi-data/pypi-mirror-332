import time

from hermes_stream_nodes import SerialStream

from hermes_framing_nodes import BurstLinkNode


def main():
    serial_node = SerialStream(SerialStream.Config(port="COM28", baudrate=115200))
    serial_node.init()
    
    node = BurstLinkNode(BurstLinkNode.Config(stream="serial_node.config"))
    node.init(serial_node)
    
    bytes_read = 0
    print_timestamp = time.time()

    while True:
        data = node.read()
        
        for d in data:
            bytes_read += len(d)
            
        if time.time() - print_timestamp > 1:
            print(f"Data rate: {bytes_read * 8 / 1000:.2f} kbps")
            bytes_read = 0
            print_timestamp = time.time()

if __name__ == "__main__":
    main()
