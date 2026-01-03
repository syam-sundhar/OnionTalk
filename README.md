# OnionTalk 🧅

**OnionTalk** is a minimal, terminal-based, peer-to-peer chat application built on **Tor Hidden Services**.
It allows two users to communicate directly **without any central server**, focusing on **privacy, decentralization, and learning system-level networking concepts**.

This project is designed to be **hackathon-ready**, **easy to demo**, and **easy to understand**, rather than feature-heavy.

---

## ✨ Key Features

* 🔐 **No central server** (true peer-to-peer)
* 🧅 **Tor Hidden Services (.onion)** for anonymity
* 💻 **Terminal-based** (works on Kali, Ubuntu, WSL)
* ⚡ **One-command installation** (Linux / WSL)
* 🧠 **Educational & transparent codebase**
* 🛑 **Single CTRL + C stops chat and Tor**

---

## 🏗️ Architecture Overview

```
User A (chat.py)
   │
   │  localhost:5555
   │
Tor Hidden Service (.onion)
   │
   │  Tor Network (routing only)
   │
User B (chat.py)
```

* Tor **only routes traffic** (no message storage)
* Chat happens **directly between the two devices**
* No cloud, no database, no login system

---

## 📦 Requirements

### Supported Platforms

| Platform         | Supported | Notes                    |
| ---------------- | --------- | ------------------------ |
| Kali Linux       | ✅         | Recommended              |
| Ubuntu           | ✅         | Recommended              |
| Windows + WSL    | ✅         | Recommended for Windows  |
| Android (Termux) | ⚠️        | Works with small changes |
| Windows (no WSL) | ❌         | Not officially supported |

---

## 🚀 Installation (Linux / WSL)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/syam-sundhar/OnionTalk.git
cd OnionTalk/oniontalk
```

### 2️⃣ Run the installer (ONE COMMAND)

```bash
chmod +x install.sh
./install.sh
```

This will:

* Install Tor and dependencies
* Configure a Tor hidden service
* Start Tor
* Display your `.onion` address

📌 **Save the `.onion` address** — you must share it with your friend **once**.

---

## 💬 Running the Chat

### Start chatting

```bash
python3 chat.py
```

Choose:

* `h` → Host (wait for connection)
* `c` → Connect (enter friend’s `.onion` address)

---

## 🛑 Stopping Everything

Press:

```
CTRL + C
```

This will:

* Stop the chat
* Stop Tor automatically
* Disable the `.onion` service

No background processes remain running.

---

## 🔐 Security Model

* Tor hides IP addresses and location
* `.onion` address does **not reveal identity**
* No messages are stored anywhere
* Only one peer connection is allowed
* Optional shared-secret authentication can be added

> ⚠️ If someone knows your `.onion`, they can attempt to connect — authentication prevents misuse.

---

## 🧠 Why OnionTalk?

Existing Tor-based tools already exist, but OnionTalk focuses on:

* **Simplicity over features**
* **Transparency over black-box design**
* **Learning and demonstration over mass adoption**

This makes it ideal for:

* Hackathons
* College projects
* Security demonstrations
* Learning decentralized networking

---

## ⚖️ Comparison with Existing Tools

| Aspect            | OnionTalk | Existing Tools |
| ----------------- | --------- | -------------- |
| Code simplicity   | ⭐⭐⭐⭐⭐     | ⭐⭐             |
| Educational value | ⭐⭐⭐⭐⭐     | ⭐⭐             |
| Deployment ease   | ⭐⭐⭐⭐⭐     | ⭐⭐⭐            |
| Features          | ⭐⭐        | ⭐⭐⭐⭐⭐          |
| Hackathon demo    | ⭐⭐⭐⭐⭐     | ⭐⭐⭐            |

---

## ⚠️ Limitations

* Single chat only (1-to-1)
* Terminal-based (no GUI)
* Not optimized for large-scale usage
* Tor network speed limitations

These are **intentional design choices**.

---

## 🔮 Future Enhancements

* Shared-secret authentication (password)
* End-to-end encryption (key exchange)
* File sharing
* Multi-user chat
* Cross-platform detection
* Simple TUI / GUI

---

## 📜 License

This project is released for **educational and demonstration purposes**.

---

## 🏁 Final Note

OnionTalk is **not trying to replace existing messengers**.
It demonstrates **how decentralized, serverless communication actually works at the system level**.

That understanding is the real value of this project.
