# Messager Demo

This project is a **demo and prototype** for a future messaging product based on a new approach to communication.

## Core Concept

The main goal of this prototype is to experiment with a messaging infrastructure built around **open and custom relays** that follow a shared set of rules.

The concept gives users more control over both the **frontend and backend**, allowing them to create, configure, and operate their own relay infrastructure.

The long-term goal is to minimize or completely remove the need for relay servers whenever possible by prioritizing **direct peer-to-peer communication**, with **IPv6 connections** as the preferred connection method.

The ideal architecture would allow users to communicate directly without relying on a centralized middleman.

## Current Prototype

The current version is focused on testing the infrastructure and validating whether the proposed communication model is technically practical.

### Backend

The backend may use:

* Node.js
* Express
* WebSockets
* CORS
* JavaScript

## Relay / Server Installation

#### 1. Install dependencies

Make sure **Node.js** and **npm** are installed on your system.

#### 2. Enter the backend directory

From the project root, navigate to the `backend` folder using a console or your preferred editor:

```bash
cd backend
```

#### 3. Install the required packages

Install the backend dependencies using npm:

```bash
npm i
```

#### 4. Start the relay/server

Start the server using:

```bash
npm start
```

If everything is configured correctly, the console should display:

```text
> backend@1.0.0 start
> node server.js

Server started at port: 5000
```

### Client

The current client is written in **Python 3** and uses socket-based communication.

The Python client can potentially run in multiple environments:

* Console
* Termux on Android devices
* Windows Shell
* Linux terminals

#### Dependencies

The client currently requires:

* **Python 3**
* [`websocket-client`](https://pypi.org/project/websocket-client/) — WebSocket communication
* [`requests`](https://pypi.org/project/requests/) — HTTP requests

## Client Installation

#### 1. Install dependencies

Make sure **Python 3** is installed, then install the required Python packages:

```bash
pip install websocket-client requests
```

#### 2. Enter the client directory

From the project root, enter the `frontend` folder:

```bash
cd frontend
```

#### 3. Start the client

Run the client using Python 3:

```bash
python3 You-Chat-DEMO.py
```

On first launch, the client may create three JSON files:

* **`chats.json`** — Stores all chats, including trashed chats and self-notes.
* **`contacts.json`** — Stores the user's contacts and their associated metadata.
* **`config.json`** — Stores essential client state and configuration.

## Basic Usage

The simplest way to get started is:

1. Use `cnn` to add a link to a relay, if one is not already configured.
2. Use `rcv` to add a receiver.
3. Use `snd` to send a message.
4. Use `vmsg` to view existing and incoming messages.

> **Note:** If the connection to the relay is lost, you currently need to reconnect manually using `rec`.

While using `vmsg`, the client is currently unable to send messages. This limitation may be removed in a future.

### Relay Link Format

When using `cnn`, provide **only the relay namespace/address**. Do not include the protocol (`http://` or `https://`) or any other URL prefix.

**Examples:**

```text
https://chatgpt.com/          ❌ Wrong
chatgpt.com                   ✅ Correct

11.12.13.14                  ❌ Wrong
http://11.12.13.14           ❌ Wrong
http://11.12.13.14:0000      ❌ Wrong
11.12.13.14:0000             ✅ Correct
```

The link should contain only the **host/namespace and, when required, the port**.

## Testing Goals

The current demo is intended to test:

* Direct peer-to-peer communication
* IPv6 connectivity
* Open and custom relay infrastructure
* Shared relay rules
* User-controlled relay configuration
* Communication between custom relay implementations
* The overall feasibility of the proposed messaging architecture

## Future Product

This prototype is not intended to represent the final product. Its purpose is to experiment with the infrastructure and concept before developing the full application.

The architecture may change significantly as testing reveals technical limitations, security concerns, or better approaches to achieving direct communication.

## Project Status

🚧 **Prototype / Demo**
