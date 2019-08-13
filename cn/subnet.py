import re

ip = list(map(int, input().split('.')))

if ip[0] <= 126:
    ip_class = 'A'
    for_subnet = '.'.join(map(str, ip[:1]))
elif 128 <= ip[0] < 192:
    ip_class = 'B'
    for_subnet = '.'.join(map(str, ip[:2]))
elif 192 <= ip[0] < 224:
    ip_class = 'C'
    for_subnet = '.'.join(map(str, ip[:3]))
else:
    print('bye bye')
    exit(0)

print(
    'The class of ip address {} is {}'.format('.'.join(map(str, ip)), ip_class)
)

masks = {
    'A': ['255.', 24],
    'B': ['255.255.', 16],
    'C': ['255.255.255.', 8]
}

number_hosts = int(input("Enter number of hosts: ")) + 2
i = 1
while True:
    result = 2 ** i
    if number_hosts <= result:
        break
    i += 1

binary = ('0' * i).rjust(masks[ip_class][1], '1')

n = 2 ** (masks[ip_class][1] - i)

subnets = []
for k in range(n):
    start = re.sub('1+', str(bin(k)[2:]), binary).rjust(masks[ip_class][1], '0')
    end = start[:-i] + '1' * i
    subnets.append([start, end])

decimal_mask = []
for i in range(0, len(binary), 8):
    decimal_mask.append(str(int(binary[i:i + 8], 2)))
mask = masks[ip_class][0] + '.'.join(decimal_mask)
print(mask)

for i in subnets:
    decimal_mask = []
    for j in range(0, len(binary), 8):
        decimal_mask.append(str(int(i[0][j:j + 8], 2)))
    start_ip = for_subnet + '.' + '.'.join(decimal_mask)
    decimal_mask = []
    for j in range(0, len(binary), 8):
        decimal_mask.append(str(int(i[1][j:j + 8], 2)))
    end_ip = for_subnet + '.' + '.'.join(decimal_mask)
    print(start_ip, '-', end_ip)
