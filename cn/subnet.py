ip = list(map(int, input().split('.')))

if ip[0] <= 126:
    ip_class = 'A'
elif 128 <= ip[0] < 192:
    ip_class = 'B'
elif 192 <= ip[0] < 224:
    ip_class = 'C'
elif 224 <= ip[0] < 240:
    ip_class = 'D'
else:
    ip_class = 'E'
    print('class E ip, this shizz useless :(')
    exit(1)

print(
    'The class of ip address {} is {}'.format('.'.join(map(str, ip)), ip_class)
)

default_masks = {
    'A': '255.0.0.0',
    'B': '255.255.0.0',
    'C': '255.255.255.0',
    'D': '255.255.255.255'
}

number_hosts = int(input("Enter number of hosts: "))
i = 1
while True:
    result = 2 ** i
    if number_hosts <= result:
        break
    i += 1
