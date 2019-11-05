import re

# index 0 - part of the subnet mask that won't change
# index 1 - no. of host bits
masks = {
    'A': ['255.', 24],
    'B': ['255.255.', 16],
    'C': ['255.255.255.', 8]
}


# converting the binary part of ip address to decimals seperated by bytes
def convert(binary):
    decimal = []
    for i in range(0, len(binary), 8):
        decimal.append(str(int(binary[i:i + 8], 2)))
    return '.'.join(decimal)


ip = list(map(int, input('Enter ip : ').split('.')))
for_subnet = ''
ip_class = ''

# for_subnet is basically what will bytes will stay same when you make subnets
if ip[0] <= 126:
    ip_class = 'A'
    for_subnet = '.'.join(map(str, ip[:1])) + '.'
elif 128 <= ip[0] < 192:
    ip_class = 'B'
    for_subnet = '.'.join(map(str, ip[:2])) + '.'
elif 192 <= ip[0] < 224:
    ip_class = 'C'
    for_subnet = '.'.join(map(str, ip[:3])) + '.'
else:
    print('bye bye')
    exit(0)

print(
    '\nThe class of ip address {} is {}\n'.format('.'.join(map(str, ip)), ip_class)
)

ip_range = int(input("Enter number of hosts: ")) + 2  # +2 cuz first and last address not available
i = 1  # 2**i will be the closest to ip_range
while True:
    result = 2 ** i
    if ip_range <= result:
        break
    i += 1

mask = ('0' * i).rjust(masks[ip_class][1], '1')  # part of the subnet mask after the part included in masks

n = 2 ** (masks[ip_class][1] - i)  # number of ip addresses in each subnet

subnets = []
for k in range(n):
    start = re.sub('1+', str(bin(k)[2:]), mask).rjust(masks[ip_class][1], '0')  # basically replace 111... with a no.
    end = start[:-i] + '1' * i  # replace all the 0s of the subnet mask with 1s to get the last address
    subnets.append([start, end])

print('the subnet mask is', masks[ip_class][0] + convert(mask), '\n')

print('subnets :')
for i in subnets:
    print(for_subnet + convert(i[0]), '-', for_subnet + convert(i[1]))
