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
    print('Class E IP, this shizz useless :(')
    exit(1)

print(
    'The class of ip address {} is {}'.format('.'.join(map(str, ip)), ip_class)
)
