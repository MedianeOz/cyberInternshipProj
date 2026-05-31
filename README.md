# 🔐 Cybersecurity Internship — XpertNurse

![Python](https://img.shields.io/badge/Python-3-blue)
![Cryptography](https://img.shields.io/badge/Cryptography-Fernet%20%7C%20RSA-green)
![Network Security](https://img.shields.io/badge/Network%20Security-Firewalls%20%7C%20HTTPS-orange)
![CIA Triad](https://img.shields.io/badge/CIA%20Triad-Confidentiality%20%7C%20Integrity%20%7C%20Availability-purple)
![Digital Signatures](https://img.shields.io/badge/Digital%20Signatures-RSA--PSS-red)

This repository contains the cybersecurity internship project completed by **Mediane Ozeir** at **XpertNurse**, a healthcare technology company. It is designed for beginner cybersecurity learners and covers foundational topics such as the CIA Triad, symmetric encryption, asymmetric encryption, digital signatures, and network security basics. The goal of the project was to build strong cybersecurity fundamentals through exported documentation from OneNote and practical Python demos that show how core security concepts work.

## 📁 Project Structure

```text
cyberInternshipProj/
├── docs/
│   └── CyberSecurity Project.pdf
├── scripts/
│   ├── symmetric_demo.py
│   ├── asymmetric_demo.py
│   ├── digital_signature_demo.py
│   └── port_ping_demo.py
└── README.md
```

| File | Description |
| --- | --- |
| `docs/CyberSecurity Project.pdf` | Exported OneNote documentation covering the internship topics, explanations, examples, and final report content. |
| `scripts/symmetric_demo.py` | Demonstrates symmetric encryption and decryption using Fernet from the `cryptography` library. |
| `scripts/asymmetric_demo.py` | Demonstrates RSA public-key encryption and private-key decryption using OAEP padding with SHA-256. |
| `scripts/digital_signature_demo.py` | Demonstrates RSA digital signing, verification, and tamper detection. |
| `scripts/port_ping_demo.py` | Checks selected localhost TCP ports using Python's built-in `socket` library. |
| `README.md` | Provides the project overview, setup instructions, script commands, topics covered, tech stack, and disclaimer. |

## ⚙️ Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/MedianeOz/cyberInternshipProj.git
```

2. Navigate into the project folder:

```bash
cd cyberInternshipProj
```

3. Install the required dependency for the cryptography demos:

```bash
pip install cryptography
```

4. Note: `port_ping_demo.py` uses Python's standard library only, so no extra installation is needed for that script.

## ▶️ How to Run the Python Scripts

Run the symmetric encryption demo:

```bash
python scripts/symmetric_demo.py
```

Expected output: the script prints the original message, encrypted ciphertext, and decrypted message.

Run the asymmetric encryption demo:

```bash
python scripts/asymmetric_demo.py
```

Expected output: the script prints the original message, RSA-encrypted ciphertext in base64, and the decrypted message.

Run the digital signature demo:

```bash
python scripts/digital_signature_demo.py
```

Expected output: the script prints a message, its signature in base64, a valid verification result, and a failed verification after tampering.

Run the localhost port checking demo:

```bash
python scripts/port_ping_demo.py
```

Expected output: the script checks selected ports on `127.0.0.1` and prints whether each port is open or closed.

## ✅ Topics Covered

- [x] CIA Triad
- [x] Symmetric Encryption
- [x] Asymmetric Encryption
- [x] Digital Signatures
- [x] Network Security Basics
- [x] Python demos for encryption, signing, verification, and localhost port checking

## 🛠 Tech Stack

| Tool/Library | Version | Purpose |
| --- | --- | --- |
| Python | Python 3 | Runs the cybersecurity demo scripts. |
| `cryptography` | Latest stable package from `pip` | Provides Fernet, RSA encryption, RSA signatures, padding, and hashing features. |
| `socket` | Python standard library | Performs basic localhost TCP port checks without external dependencies. |
| Markdown | GitHub-flavored Markdown | Formats the project README. |

## ⚠️ Disclaimer

All port scanning scripts in this project are for educational purposes only. Only run scanning tools or scripts on systems you own or have explicit permission to test.
