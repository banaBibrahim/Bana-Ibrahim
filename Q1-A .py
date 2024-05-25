L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]

d = {key: value for key, value in zip(L1, L2)}
print(d)



