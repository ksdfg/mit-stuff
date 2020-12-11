from csv import reader

if __name__ == "__main__":
    with open('logs.csv', 'r') as file:
        # read all the logs
        logs = reader(file, delimiter=",")

        format_string = "{:^12}\t{:^40}\t{:^20}\t{:^20}\t{:^18}\t{:^18}\t{:^8}"

        # print the headers
        print(
            format_string.format(
                'Frame Number', 'Frame Time', 'Source MAC', 'Destination MAC', 'Source IP', 'Destination IP', 'Protocol'
            ),
            end="\n\n",
        )

        # print the logs
        for log in logs:
            # replace protocol number with the name
            if log[-1] == "6":
                log[-1] = "TCP"
            elif log[-1] == "17":
                log[-1] = "UDP"
            elif log[-1] == "1":
                log[-1] = "ICMP"

            # print the logs
            print(format_string.format(*log))
