# Python Multithreaded Port Scanner

A simple and ethical **TCP port scanner** written in Python.  

---

## Overview

This tool performs a **TCP connect scan** against a target IP address or domain using Python sockets.  
It uses **multithreading** to improve scanning speed and includes execution timing and clean interruption handling.

⚠️ **Important:**  
This tool is for **educational and authorized security testing only**.  
Scan only systems you own or have explicit permission to test.

---

## Features

- Multithreaded TCP port scanning using `ThreadPoolExecutor`
- User-defined target (IP address or domain)
- Scans common service ports
- Measures scan start time, end time, and total duration
- Graceful exit using `Ctrl + C`
- Proper socket cleanup to avoid resource leaks

---

## Technologies Used

- Python 3
- `socket` (network communication)
- `concurrent.futures.ThreadPoolExecutor` (multithreading)
- `time` (performance measurement)

---

## How It Works

1. The user enters a target IP address or domain.
2. A list of common ports is scanned using multiple threads.
3. Each thread attempts a TCP connection to a specific port.
4. Open ports are identified based on successful connections.
5. Scan duration is calculated and displayed.

---

