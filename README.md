# -GNS3-Corporate-Network-Simulation-with-Cisco-ASA-Firewall

# 🔥 GNS3: Corporate Network Simulation with Cisco ASA Firewall

This project simulates a realistic corporate network topology using Cisco routers, MikroTik, and ASA firewall. It includes NAT configuration, internal VLAN segmentation, and Internet emulation using a separate router.

---

## 📡 Topology Overview

[PC]---[Cisco R1]---[MikroTik]---[ASA Firewall]---[Cisco INTERNET Router]
| |
VLAN 10 IP: 192.168.100.2
192.168.10.x |
Loopback 8.8.8.8 (Fake Internet)

- **ASA Firewall** acts as the border between internal and external networks.
- **Cisco INTERNET Router** simulates the public Internet via a loopback address (8.8.8.8).
- **MikroTik Router** handles VLANs and internal routing.
- **PCs** obtain IP addresses within VLAN 10 and route through ASA to reach the outside world.
