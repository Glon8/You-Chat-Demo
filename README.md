# Messenger Demo

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

### Client

The current client is written in Python and uses socket-based communication.

The Python client can potentially run in multiple environments:

* Console
* Termux on Android devices
* Windows Shell
* Linux terminals

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
