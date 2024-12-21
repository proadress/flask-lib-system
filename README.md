<h1>Youtube展示影片</h1>
<a href="https://youtu.be/SPjJkuykPtg">https://youtu.be/SPjJkuykPtg</a>

# Library Access and Integration System

This project introduces a **one-time QR Code access system** for libraries, designed to enhance security and user convenience while minimizing operational costs. The system integrates core library functionalities into a centralized platform for better user experience and increased engagement.

---

## Features

### 1. One-Time QR Code Access System

- **User Side**:  
  Students can log in to the library's website and generate a time-sensitive, one-time QR Code.

  - The backend creates a random token linked to the user's identity (e.g., student ID).
  - The frontend displays the QR Code generated from the token.
  - The system updates the database with the token, request time, and usage status.

- **Administrator Side**:  
  Administrators scan the QR Code using any internet-connected device with a camera.
  - The backend validates the token, expiration time, and usage status.
  - If verified, a signal is sent to unlock the door.
  - Entry details are logged in the database.

This approach eliminates the need for students to carry physical ID cards while ensuring security.

### 2. Integrated Library System

- The platform combines library access with additional functionalities:
  - Browsing library information before login.
  - Accessing announcements highlighted with high-contrast colors for better visibility.

---

## System Overview

### User Workflow

1. Log in to the website.
2. Generate a one-time QR Code.
3. Present the QR Code at the library entrance.

### Admin Workflow

1. Scan the QR Code using a connected device.
2. Verify the code's validity and trigger the door unlock.
3. Log the user's entry details.

---

## Technical Details

### Prerequisites

- Python 3.10.11
- Virtual environment setup (e.g., `pyenv`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/library-access-system.git
   cd library-access-system
   ```
2. Run the installation script:
   ```bash
   bin/install
   ```
   - Creates a virtual environment.
   - Installs dependencies listed in `requirements.txt`.

### Running the Server

Start the server with Gunicorn:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt


bin/start

```

---

## Visual Demonstrations

### Access Flow

![QR Code Access Flow](https://example.com/path-to-image)

### User Interface

#### Before Login

- Library announcements and information are displayed.

#### After Login

- Access to personalized features, including QR Code generation and more.

---

## Future Potential

- **Cost-Effective Implementation**: Uses existing internet-enabled devices with cameras for administration.
- **Scalability**: Designed to support integration with other library services, increasing exposure and utility.

For questions or assistance, join our community on [Discord](https://discord.cyclic.sh).

Enjoy! 🚀
