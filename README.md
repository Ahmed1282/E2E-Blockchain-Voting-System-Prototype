# E2E Blockchain Voting System Prototype

## Overview
This project is an End-to-End Blockchain Voting System Prototype, designed to provide a secure, transparent, and reliable platform for conducting electronic voting. It leverages blockchain technology to ensure the integrity and anonymity of votes.

## Features
- **Blockchain Integration**: Implements blockchain for recording votes, ensuring security and transparency.
- **User-Friendly Interface**: The client-side interface allows users to cast votes easily.
- **Real-Time Vote Tally**: The server-side interface displays the current voting results in real-time.
- **Blockchain Visualization**: Users can view the blockchain containing the voting records.
- **Secure Voting Process**: Ensures the confidentiality and integrity of the voting process.

## Technology Stack
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Backend**: Python (Flask framework for server-side operations)
- **Blockchain Framework**: Custom blockchain implementation in Python
- **Template Engine**: Jinja2 for dynamic rendering of HTML pages
- **Additional Libraries/Tools**: JavaScript for frontend scripting

## Installation and Setup

Follow these steps to set up and run the E2E Blockchain Voting System Prototype:

1. **Clone the Repository**
   - Clone this repository to your local machine using:
     ```
     git clone https://github.com/Ahmed1282/E2E-Blockchain-Voting-System-Prototype.git
     ```
   - Navigate to the project directory:
     ```
     cd E2E-Blockchain-Voting-System-Prototype
     ```

2. **Install Dependencies**
   - Ensure you have Python installed on your machine. This project requires Python 3.x.
   - Install the required Python packages:
     ```
     pip install flask
     ```

3. **Start the Server**
   - Run the server application:
     ```
     python server.py
     ```

4. **Launch the Client**
   - Open another terminal window.
   - Run the client application:
     ```
     python client.py
     ```

5. **Access the Application**
   - Open your web browser and navigate to `http://localhost:5000` to interact with the client interface.
   - The server interface can be viewed at `http://localhost:5000/server` (or the appropriate URL based on your server configuration).

Note: This is a basic setup guide. You might need to adjust the steps based on your system configuration and the specifics of your project.


