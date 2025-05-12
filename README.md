# Agent Development Kit (ADK) - Setup and Usage

## Introduction to the Agent Development Kit (ADK)

The Agent Development Kit (ADK) is a powerful set of tools and libraries designed to streamline the development of intelligent agents.  An agent, in this context, is a software entity that can perceive its environment, reason about it, and take actions to achieve specific goals.

**Why is ADK valuable?**

* **Abstraction and Simplification:** ADK provides high-level abstractions, reducing the complexity of building agents from scratch.  It handles many of the common tasks, allowing developers to focus on the core logic of their agents.
* **Modularity and Reusability:** ADK promotes a modular design, making it easier to build, test, and maintain agent components.  These components can often be reused across different agent projects.
* **Integration with Powerful Tools:** ADK is designed to work seamlessly with powerful tools and services, such as Google Cloud's Vertex AI, enabling agents to leverage cutting-edge machine learning capabilities.
* **Rapid Development:** By providing pre-built components and utilities, ADK significantly speeds up the agent development process.
* **Focus on Logic:** ADK lets developers concentrate on defining the agent's behavior and decision-making processes, rather than dealing with low-level infrastructure.

In essence, ADK empowers developers to create sophisticated, intelligent agents more efficiently and effectively.

## Setting up Your Environment

Before you can start developing agents with this kit, you'll need to set up your development environment. This involves installing the necessary software and configuring environment variables.

### Prerequisites

* **Python:** Ensure you have Python 3.9 or later installed. You can check your Python version by running `python3 --version` or `python --version` in your terminal.
* **Google Cloud Account:** You'll need a Google Cloud account to access Vertex AI and other Google Cloud services. If you don't have one, sign up at [https://cloud.google.com/](https://cloud.google.com/).
* **Google Cloud SDK (gcloud):** The `gcloud` command-line tool is required to interact with Google Cloud services.  Follow the installation instructions for your operating system here: [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
* **Git:** Git is used for version control.  If you don't have it, install it from [https://git-scm.com/](https://git-scm.com/).

### Installation Steps

1.  **Clone the Repository (if applicable):** If you have a repository containing the ADK code, clone it to your local machine:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    Replace `<repository_url>` with the URL of your repository and `<repository_directory>` with the name of the directory where you want to clone it.

2.  **Create a Virtual Environment (Recommended):** It's best practice to create a virtual environment to isolate your project's dependencies.

    ```bash
    python3 -m venv venv  # Create a virtual environment named "venv"
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:** Install the required Python packages using `pip`.  A `requirements.txt` file is usually provided in the repository:

    ```bash
    pip install -r requirements.txt
    ```
    3.a. Install google-adk extensions
    ```bash
    pip install 'google-adk[extensions]'
    ```

## Setting Environment Variables

Environment variables provide a way to configure your application's behavior without hardcoding sensitive information or configuration values directly into your code.  The following environment variables are crucial for this project:

### 1.  `GOOGLE_GENAI_USE_VERTEXAI`

    * **Purpose:** This variable determines whether the agent will use Google Cloud's Vertex AI for its generative AI capabilities.
    * **Value:** Set this to `1` to enable Vertex AI.
    * **Setting the variable:**

        * **Linux/macOS:**
            ```bash
            export GOOGLE_GENAI_USE_VERTEXAI=1
            ```
        * **Windows (Command Prompt):**
            ```batch
            set GOOGLE_GENAI_USE_VERTEXAI=1
            ```
        * **Windows (PowerShell):**
             ```powershell
             $env:GOOGLE_GENAI_USE_VERTEXAI = 1
             ```

### 2.  `GOOGLE_CLOUD_PROJECT`

    * **Purpose:** Specifies the Google Cloud Project ID that you will be using.
    * **Value:** Replace `YOUR_GCP_PROJECT_ID` with your actual Google Cloud Project ID.  You can find your Project ID in the Google Cloud Console.
    * **Setting the variable:**

        * **Linux/macOS:**
            ```bash
            export GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
            ```
        * **Windows (Command Prompt):**
            ```batch
            set GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
            ```
         * **Windows (PowerShell):**
             ```powershell
             $env:GOOGLE_CLOUD_PROJECT = "YOUR_GCP_PROJECT_ID"
             ```

### 3.  `GOOGLE_CLOUD_LOCATION`

    * **Purpose:** Sets the Google Cloud location (region) where your Vertex AI resources are located.
    * **Value:** Replace `GCP_LOCATION` with the appropriate Google Cloud region (e.g., `us-central1`, `us-east1`).  Choose a location that supports the Vertex AI features you intend to use.
    * **Setting the variable:**

        * **Linux/macOS:**
            ```bash
            export GOOGLE_CLOUD_LOCATION=GCP_LOCATION
            ```
        * **Windows (Command Prompt):**
            ```batch
            set GOOGLE_CLOUD_LOCATION=GCP_LOCATION
            ```
        * **Windows (PowerShell):**
             ```powershell
             $env:GOOGLE_CLOUD_LOCATION = "GCP_LOCATION"
             ```

### 4.  `MODEL`

    * **Purpose:** Specifies the name of the generative AI model to use.
    * **Value:** The example provided is `gemini-2.0-flash-001`.  You might need to change this depending on the available models and your specific requirements.  Check the Vertex AI documentation for available models.
    * **Setting the variable:**

        * **Linux/macOS:**
            ```bash
            export MODEL="gemini-2.0-flash-001"
            ```
        * **Windows (Command Prompt):**
            ```batch
            set MODEL="gemini-2.0-flash-001"
            ```
        * **Windows (PowerShell):**
             ```powershell
             $env:MODEL = "gemini-2.0-flash-001"
             ```

## Login to Google Cloud Platform

Be sure you login to Google Cloud Platform.  When you run this command, a web browser will open up and guide you through the login process.

```bash 
    gcloud auth application-default login
```

## Next Steps

After completing these setup steps, you should be ready to start building and experimenting with agents using the Agent Development Kit.  Refer to the ADK documentation and examples for guidance on how to use the available tools and libraries.
