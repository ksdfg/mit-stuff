from csv import reader


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
        return "{:<16}\t{:<16}\t{:<16}".format(self.source, self.destination, self.protocol)

    def __hash__(self) -> int:
        """
        Get the hashed value of the Log object
        :return: Hashed value for current Log object
        """
        return hash(str(self))


if __name__ == "__main__":
    with open('logs.csv', 'r') as file:
        # read all rows from the log file
        rows = reader(file, delimiter=",")

        # make list of Log objects for each row
        logs: list[Log] = []
        for row in rows:
            logs.append(Log(*row))

        # print all unique logs and how many times they appear
        print("{:<16}\t{:<16}\t{:<16}".format("Source", "Destination", "Protocol"), "Count", end="\n\n")
        for log in set(logs):
            print(log, logs.count(log))
