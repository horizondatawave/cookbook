# Sales AI-Assistant

**Sales AI-Assistant** is an AI Agent designed to help users streamline their sales and scheduling workflows. The assistant integrates with LinkedIn, Gmail, and Google Calendar, Google search enabling seamless profile searches, email management, and event scheduling.

## Features

- **LinkedIn Integration**: Search for profiles, companies, and job listings based on user queries.
- **Gmail Management**: Read, compose, and organize emails from your inbox.
- **Google Calendar Assistance**: Create, read, update, and delete events in your Google Calendar.
- **Google Search**: Perform web searches and retrieve relevant information via SerperDevtool API.
- **Intelligent Tool Selection**: Automatically selects the appropriate tool based on the user's query.
- **Personalized Assistance**: Responds to user inputs contextually and confirms critical details before executing actions.

---

## Setup Instructions

Follow the steps below to set up and run the project.

### Prerequisites

1. **Python 3.10+**
2. **Google Cloud Credentials**
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Gmail API and Google Calendar API for the project.
   - Download the `credentials.json` file from the API & Services > Credentials section.
3. **HorizonDataWave API Key**
   - Register at [HorizonDataWave](https://horizondatawave.ai).
   - Obtain your API key from the dashboard.
4. **SerperDevtool API Key**
    - Register at [SerperDev](https://serper.dev).
    - Obtain your API key from the dashboard.

---

### Environment Variables

Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY=<your_openai_api_key>
CHAINLIT_AUTH_SECRET=<your_chainlit_auth_secret>
LITERAL_API_KEY=<your_literal_api_key>
OAUTH_GOOGLE_CLIENT_ID=<your_google_client_id>
OAUTH_GOOGLE_CLIENT_SECRET=<your_google_client_secret>
CHAINLIT_PORT=8001
HDW_API_URL=https://api.horizondatawave.ai/api
HDW_API_KEY=<your_hdw_api_key>
SERPER_API_KEY=<your_serper_api_key>
```

Replace placeholders with actual values. You can obtain your HDW_API_KEY from [HorizonDataWave](https://horizondatawave.ai)

---

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/horizondatawave/cookbook.git
   cd sales-chat-assistant
   
2. **Create and activate a virtual environment:** 
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
3. **Install the dependencies:**
   ```bash
    pip install -r requirements.txt
    ```

4. **Place the credentials.json file in the root directory:**

 - Download your credentials.json from Google Cloud Console. 
 - The sure it is located in the root directory of the project.

5. **Generate Google API tokens:**

Run the following script to authenticate with Gmail and Google Calendar APIs:
   ```bash
    python get_token.py
   ```
Verify that the token.json file is created. This file will be used for subsequent API requests.

---

### Running the Application

   ```bash
   chainlit run app.py   
   ```

---

### Dependencies

**Key dependencies for this project include:**

 - Chainlit: Framework for building conversational UIs.
 - LlamaIndex: AI Agent Framework for building conversational AI agents.
 - Google APIs: Enables Gmail and Calendar functionalities.
 - OpenAI: Provides the AI model for conversational understanding.
 - HorizonDataWave: Provides AI-powered LinkedIn search capabilities.

---

## License

This project is licensed under the MIT License.