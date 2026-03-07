# Python Security Toolkit: Automated Auditing & Access Control

Project Overview
This repository contains a modular **Cybersecurity Toolkit** designed to automate routine security tasks. By integrating network auditing, credential analysis, and access management into a single suite, this project demonstrates the application of Python in **Defensive Security** and **Attack Surface Reduction**.

Key Modules

### 1. Bulk Password Auditor
A high-speed credential validator that audits password lists against a security matrix. It identifies "Critical" vulnerabilities (default passwords like `123456`) and evaluates "Strong" entropy based on a 14-character minimum and special symbol inclusion.

### 2. Digital Guard: Time-Based Access Control (TBAC)
A security gateway that enforces the **Principle of Least Privilege**. It restricts system access to authorized personnel and validates that login attempts occur only during defined "Business Hour" windows (09:00 - 17:00), mitigating off-hours unauthorized access.

### 3. Network Vulnerability Scanner
A specialized auditor that identifies "OPEN" status on critical server ports. It maps active ports to high-risk services such as **SSH (22)** and **FTP (21)**, providing immediate visibility into potentially exposed entry points.

Security Logic Matrix
| Module | Security Focus | Core Benefit |
| :--- | :--- | :--- |
| **Password Auditor** | Identity Management | Prevents the use of weak or leaked credentials. |
| **Digital Guard** | Access Control | Reduces the window of opportunity for attackers. |
| **Network Scanner** | Infrastructure Security | Flags unmanaged or unsafe open services. |

Technical Stack
* **Language:** Python 3.x
* **Security Domains
