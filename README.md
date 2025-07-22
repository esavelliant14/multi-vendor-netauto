# multi-vendor-netauto
Network Automation

## NETMIKO

requirement

```bash
pip install netmiko
```

untuk dokumentasi lengkap netmiko bisa dilihat di https://github.com/ktbyers/netmiko

point penting dalam netmiko

- send_command => biasanya digunakan untuk show command
- send_config => biasanya digunakan untuk config, karena dengan command ini netmiko langsung melakukan configure terminal(jika di cisco) atau configure (jika di juniper)
- device_type => seri/merk perangkat yang digunakan, sudah ada format pengisiannya untuk tiap perangkat, list format tiap perangkat ada di https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md

