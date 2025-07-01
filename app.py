import streamlit as st
from utils.task_extractor import extract_tasks
from utils.trello_client import create_trello_card
from utils.slack_client import notify_slack

st.set_page_config(page_title="Email to Task Automator", layout="centered")
st.title("📬 Email to Task Automator")

st.markdown("""
### How It Works
1. Paste any email that includes to-dos or follow-ups.
2. Click "Extract Tasks".
3. Tasks auto-push to Trello and Slack, if configured.
""")

# Preset sample email
preset_email = """Hi team,

Great work on wrapping up the June deliverables.

Looking ahead, here are a few important follow-ups:

- Please finalize and submit the Q3 marketing budget proposal to finance by Thursday noon.  
- Someone needs to follow up with David (legal) about the updated NDA — make sure it's reviewed before we onboard the new partners next week.  
- Jenna, kindly schedule a customer success meeting with the Top 5 enterprise clients. Ideally by Monday afternoon.  
- Update the client onboarding SOP to reflect the new refund policy, and circulate to the CX team.  
- Can someone double-check the CRM to ensure Acme Corp’s billing info is accurate? We’ve had some issues with duplicate entries.  
- Lastly, prepare the slides for next Wednesday's investor meeting — include growth metrics, churn reduction, and new market expansion plans.

Let me know if anything is unclear. Appreciate the hustle!

Thanks,  
Dave
"""

# Session state logic (safe default)
if "email_input" not in st.session_state:
    st.session_state.email_input = preset_email
if "cleared_once" not in st.session_state:
    st.session_state.cleared_once = False

# Render input field
st.text_area("Paste email content here:", key="email_input", height=200)

# If cleared manually
if not st.session_state.email_input.strip() and not st.session_state.cleared_once:
    st.session_state.cleared_once = True

if st.button("Extract Tasks"):
    email = st.session_state.email_input
    if not email.strip():
        st.warning("Please paste an email to extract tasks.")
    else:
        with st.spinner("⏳ Extracting tasks using GPT..."):
            tasks = extract_tasks(email)

        if not tasks:
            st.error("❌ No actionable tasks found.")
        else:
            st.success(f"✅ {len(tasks)} tasks found")
            for task in tasks:
                st.markdown(f"**Task:** {task['task']}")
                st.markdown(f"- Due: {task.get('due')}")
                st.markdown(f"- Priority: {task.get('priority')}")
                trello_status = create_trello_card(task)
                slack_status = notify_slack(task)
                st.markdown(f"- 🔗 Trello: {'✅' if trello_status else '❌'} | Slack: {'✅' if slack_status else '❌'}")
                st.divider()

            task_count = len(tasks)
            estimated_hours_saved = round(task_count * 0.2, 1)
            st.info(f"🧾 {task_count} tasks processed — estimated {estimated_hours_saved} hours saved.")

            st.caption("Want this deployed to your Gmail, Trello, or Slack? I can deliver a custom setup in 2 days.")
