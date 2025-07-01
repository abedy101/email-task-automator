

```markdown
# 📧 Email-to-Task Automator 🤖

An AI-powered tool that extracts actionable tasks from emails and automatically sends them to Trello and Slack.

## Preview

![App Screenshot](https://raw.githubusercontent.com/abedy101/email-task-automator/main/assets/screenshot.png)

## ✨ Features

- **Smart Email Parsing**:
  - Extracts task descriptions, deadlines, and priority levels (High/Medium/Low)
  - Handles multiple tasks from a single email
- **Seamless Integrations**:
  - Creates Trello cards automatically
  - Sends Slack notifications
- **User-Friendly Interface**:
  - Clean Streamlit UI for testing and experimentation
- **Time-Saving**:
  - Shows estimated time saved per processed email

## 📝 Example Workflow

### Input Email
```
Hi team,

Great work on wrapping up the June deliverables.

Looking ahead, here are a few important follow-ups:

* Please finalize and submit the Q3 marketing budget proposal to finance by Thursday noon.
* Someone needs to follow up with David (legal) about the updated NDA — make sure it's reviewed before we onboard the new partners next week.
* Jenna, kindly schedule a customer success meeting with the Top 5 enterprise clients. Ideally by Monday afternoon.
* Update the client onboarding SOP to reflect the new refund policy, and circulate to the CX team.
* Can someone double-check the CRM to ensure Acme Corp's billing info is accurate? We've had some issues with duplicate entries.
* Lastly, prepare the slides for next Wednesday's investor meeting — include growth metrics, churn reduction, and new market expansion plans.

Thanks,
Dave
```

### Extracted Tasks
```json
[
  {
    "task": "Finalize and submit the Q3 marketing budget proposal to finance",
    "due": "Thursday noon",
    "priority": "high"
  },
  {
    "task": "Follow up with David (legal) about the updated NDA",
    "due": "before onboarding next week",
    "priority": "high"
  },
  {
    "task": "Schedule a customer success meeting with the Top 5 enterprise clients",
    "due": "Monday afternoon",
    "priority": "high"
  },
  {
    "task": "Update the client onboarding SOP to reflect the new refund policy and circulate to CX team",
    "due": "not mentioned",
    "priority": "medium"
  },
  {
    "task": "Double-check the CRM to ensure Acme Corp's billing info is accurate",
    "due": "not mentioned",
    "priority": "medium"
  },
  {
    "task": "Prepare slides for next Wednesday's investor meeting",
    "due": "next Wednesday",
    "priority": "high"
  }
]
```

## 🛠️ Tech Stack

| Component       | Technology |
|-----------------|------------|
| Language Model  | OpenAI GPT-4 |
| Backend         | FastAPI    |
| Frontend        | Streamlit  |
| Integrations    | Trello API, Slack Webhooks |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key
- Trello credentials (optional)
- Slack webhook URL (optional)

### Installation
```bash
git clone https://github.com/abedy101/email-task-automator.git
cd email-task-automator
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Configuration
Create a `.env` file with your credentials:
```
OPENAI_API_KEY=your-key-here
TRELLO_KEY=your-key-here
TRELLO_TOKEN=your-token-here
TRELLO_BOARD_ID=your-board-id-here
SLACK_WEBHOOK_URL=your-webhook-url-here
```

### Running the Application
```bash
# Start the API server
uvicorn app.main:app --reload

# Start the frontend
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## 🔧 Customization Options

- **LLM Integration**: Swap OpenAI for Claude, Mistral, or other LLMs
- **Email Providers**: Connect with Gmail/Outlook via Zapier or Google Apps Script
- **Additional Integrations**: Add support for Notion, Monday.com, or MS Teams

## 📄 License

This project is open-source under the [MIT License](LICENSE).

## 💼 Professional Services

Need a customized version for your team? I can deliver:
- Full integration with your email system
- Custom CRM connections
- Team-specific configurations

**Delivery time**: Typically under 48 hours
```
