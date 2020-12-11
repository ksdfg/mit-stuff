class Log:
    """
    Class reperesenting a single log entry
    """

    def __init__(self, source: str, destination: str, protocol: str):
        """
        Initialize the Log object
        :param source: Source IP of the packet
        :param destination: Destination IP of the packet
        :param protocol: Protocol used
        """
        self.source = source.strip()
        self.destination = destination.strip()
        self.protocol = protocol.strip()

    def __eq__(self, other) -> bool:
        """
        Check if a log object is equal to another Log object
        :param other: The other Log object we are comparing to
        :return: True if they are equal, else False
        """
        return self.source == other.source and self.destination == other.destination and self.protocol == other.protocol

    def __repr__(self) -> str:
        """
        String representation of a log object
        :return: Formatted string with source, destination and protocol listed in that order
        """
        return "{:>17}\t{:>17}\t{:>17}".format(self.source, self.destination, self.protocol)

    def __hash__(self) -> int:
        """
        Get the hashed value of the Log object
        :return:
        """
        return hash(str(self))


if __name__ == "__main__":
    # read all logs from the log file
    with open('logs.csv', 'r') as log_file:
        lines = log_file.read().split("\n")

    # make list of logs
    logs: list[Log] = []
    for line in lines:
        # split the line by `,` since it is a csv
        args = [x.strip() for x in line.split(",")]
        if len(args) == 3:
            logs.append(Log(*args))

    # print all unique logs and how many times they appear
    print("{:>17}\t{:>17}\t{:>17}\t{:>17}".format("Source", "Destination", "Protocol", "Count"), end="\n\n")
    for log in set(logs):
        print("{}\t{:>17}".format(log, logs.count(log)))
