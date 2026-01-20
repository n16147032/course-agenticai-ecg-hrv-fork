# ECG-Pomodoro: A Pomodoro Timer with ECG-based Stress and Focus Detection

An AI agent system for managing work and rest cycles with real-time physiological feedback.

**Group:** 2026-Chen-Chen-Liu
**Authors:** Chen, Chen, Liu
**License:** Apache-2.0

## Badges

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
[![Coverage Status](https://coveralls.io/repos/github/joemccann/dillinger/badge.svg?branch=master)](https://coveralls.io/github/joemccann/dillinger?branch=master)

## Navigation

- [Description](#description)
- [Requirements](#requirements)
- [API Keys](#api-keys)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Testing](#testing)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Style Guide](#style-guide)
- [License](#license)
- [Disclaimer](#disclaimer)

## Description

This project, `ecg-pomodoro`, is a web application that integrates the Pomodoro Technique with mock electrocardiogram (ECG) analysis. The goal is to provide a tool that helps users manage their productivity through timed work and break intervals, while simulating the monitoring of physiological markers for stress and focus.

The application is architected as a set of microservices:
1.  A **React frontend** that provides the user interface for the Pomodoro timer and displays the analysis results.
2.  An **ECG service** (Python/FastAPI) that simulates receiving raw ECG data and processing it to extract features like R-peaks and heart rate variability (HRV) metrics.
3.  An **AI service** (Python/FastAPI) that takes the features from the ECG service and provides a mock "prediction" of the user's state (e.g., "focus" or "stress").

**Note:** The backend services are currently stubs that generate random data, as the focus of this implementation is on the system's architecture and inter-service communication.

## Requirements

- Node.js v14+ and npm
- Python 3.9+ and pip
- `uvicorn` for running the Python services

## API Keys

No API keys are required to run this project.

## Installation

### Install Dependencies

1.  **Frontend**

    ```bash
    # Navigate to the frontend directory
    cd frontend

    # Install npm packages
    npm install
    ```

2.  **Backend**

    The backend consists of two services. It is recommended to create a virtual environment for them.

    ```bash
    # From the project root directory
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install dependencies for both services
    pip install -r ecg-service/requirements.txt
    pip install -r ai-service/requirements.txt
    ```

## Usage

All three services must be running concurrently for the application to function.

1.  **Start the Frontend**

    ```bash
    # In the frontend/ directory
    npm start
    ```
    The application will be available at `http://localhost:3000`.

2.  **Start the Backend Services**

    Open two separate terminals to run the backend services.

    ```bash
    # In the first terminal, start the ECG service
    # (from the ecg-pomodoro/ directory)
    cd ecg-service
    uvicorn main:app --reload --port 8001

    # In the second terminal, start the AI service
    # (from the ecg-pomodoro/ directory)
    cd ai-service
    uvicorn main:app --reload --port 8002
    ```
    The ECG service will run at `http://localhost:8001`, and the AI service will run at `http://localhost:8002`.

Once all services are running, you can open a web browser to `http://localhost:3000` to use the Pomodoro timer and see the mock analysis results.

## Architecture

The system uses a microservices architecture:

```
┌───────────────────┐       ┌────────────────┐       ┌──────────────┐
│  React Frontend   │──────>│  ECG Service   │──────>│  AI Service  │
│ (localhost:3000)  │       │ (localhost:8001) │       │(localhost:8002)│
└───────────────────┘       └────────────────┘       └──────────────┘
```

-   **Frontend**: A standard `create-react-app` application for the user interface.
-   **ECG Service**: A FastAPI server that exposes a `/ecg/` endpoint. It receives mock ECG data and returns a set of calculated features.
-   **AI Service**: A FastAPI server that exposes an `/ai/` endpoint. It receives features from the ECG service and returns a mock prediction.

This decoupled design allows each component to be developed, deployed, and scaled independently.

### Project Structure

```
ecg-pomodoro/
├── .env.example           # Example environment variables
├── .gitignore             # Git ignore file
├── CODE_OF_CONDUCT.md     # Code of Conduct
├── LICENSE                # Apache-2.0 License
├── README.md              # This file
├── ai-service/            # Python FastAPI AI service
│   ├── main.py            # Service entry point
│   └── requirements.txt
├── ecg-service/           # Python FastAPI ECG service
│   ├── main.py            # Service entry point
│   └── requirements.txt
├── frontend/              # React frontend application
│   ├── public/            # Public assets
│   ├── src/               # Frontend source code
│   └── package.json
└── ...
```

## Testing

The frontend includes a standard set of React tests.

```bash
# In the frontend/ directory
npm test
```

No automated tests have been set up for the backend services at this time.

## Known Issues

-   **Stubbed Services:** The `ecg-service` and `ai-service` do not perform real analysis. They return pre-defined or randomly generated data for demonstration purposes.
-   **Missing Top-Level `requirements.txt`**: The course requirements suggest a single `requirements.txt`. However, due to the microservices architecture, each service has its own dependency file.

## Demo

[Link to a live demo of the project]

## Meta

-   **Author:** Chen-Chen-Liu
-   **Email:** (email to be added)
-   **Website:** (website to be added)
-   **Repository:** (repository to be added)

## Release History

-   **0.1.0**
    -   The first release of the project.
    -   This release includes the basic functionality of the Pomodoro timer and the ECG analysis.
-   **0.0.1**
    -   Work in progress

## Roadmap

-   **Q1 2026:**
    -   [ ] Launch of the beta version
    -   [ ] Integration with a real ECG device
-   **Q2 2026:**
    -   [ ] Launch of the stable version
    -   [ ] Integration with a real AI model
-   **Q3 2026:**
    -   [ ] Launch of the mobile app
    -   [ ] Integration with a database
-   **Q4 2026:**
    -   [ ] Launch of the web app
    -   [ ] Integration with a CI/CD pipeline

## FAQ

**Q: Is this project free to use?**
**A:** Yes, this project is licensed under the Apache-2.0 License, which means it is free to use, modify, and distribute.

**Q: Can I contribute to this project?**
**A:** Yes, we welcome contributions! Please see the [Contributing](#contributing) section for more information.

**Q: Where can I get help with this project?**
**A:** Please see the [Support](#support) section for more information.

## Support

If you need help with the project, you can:

-   Open an issue in the repository
-   Join our Discord server (link to be added)
-   Email us at (email to be added)

## Acknowledgments

-   [Contributor Covenant](https://www.contributor-covenant.org/)
-   [Img Shields](https://shields.io/)
-   [Choose an Open Source License](https://choosealicense.com/)

## Technology Stack

-   **Frontend:** React, JavaScript, CSS
-   **Backend:** Python, FastAPI
-   **Database:** None
-   **Testing:** Jest, React Testing Library
-   **Deployment:** None

## Screenshots

[Add screenshots of the application here]

## To-Do

-   [ ] Implement real ECG analysis in the `ecg-service`
-   [ ] Implement a real AI model in the `ai-service`
-   [ ] Add a database to store user data and analysis results
-   [ ] Add user authentication
-   [ ] Set up a CI/CD pipeline for automated testing and deployment

## Disclaimer

This project is for educational purposes only and is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

## Style Guide

-   **Python:** We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.
-   **JavaScript/React:** We follow the [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript) for JavaScript and React code.

We use `black` to format our Python code and `prettier` to format our JavaScript/React code. Please make sure to run these tools before submitting a pull request.

## Contributing

We welcome contributions to the `ecg-pomodoro` project! If you'd like to contribute, please follow these guidelines:

1.  **Reporting Bugs:** If you find a bug, please open an issue in the repository. Be sure to include a clear and concise description of the bug, as well as steps to reproduce it.
2.  **Suggesting Features:** If you have an idea for a new feature, please open an issue to discuss it. This will allow us to give you feedback and ensure that the feature is a good fit for the project.
3.  **Submitting Pull Requests:** We welcome pull requests for bug fixes, feature implementations, and documentation improvements. When submitting a pull request, please make sure that your code is well-tested and that it follows the project's coding style.

Thank you for your interest in contributing to the `ecg-pomodoro` project!

## Code of Conduct

We have adopted a Code of Conduct that we expect project participants to adhere to. Please read [the full text](CODE_OF_CONDUCT.md) so that you can understand what actions will and will not be tolerated.
