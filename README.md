# Automate-JIRA-Creation-on-a-Github-Event-using-Python

## Flask App for Creating JIRA Tickets via GitHub Issue Comments

This Flask app integrates with GitHub's webhook to create JIRA tickets when the comment `/jira` is added to a GitHub issue. This allows you to automate ticket creation in JIRA whenever an issue comment is made and verified as genuine.

## How It Works

- **GitHub Webhook**: GitHub will trigger a webhook when an issue comment is made.
- **Issue Comment**: The app listens for comments that include `/jira` in the body of the comment.
- **JIRA Ticket Creation**: When `/jira` is detected, the app triggers the creation of a new JIRA ticket via the JIRA API.
- **Verification**: Ensure that the issue and comment are genuine before typing `/jira`.

## Requirements

- **AWS EC2 Instance**: You need an EC2 instance to deploy the Flask app.
- **JIRA API Token**: You need a JIRA API token for authentication.
- **GitHub Webhook**: Set up a webhook in GitHub to trigger the Flask app when an issue comment is made.
- **Security Group Rule**: Open **port 5000** in your EC2 instance’s security group to allow inbound traffic.

## Steps to Deploy

### 1. Launch an EC2 Instance
- Create a new EC2 instance on AWS using an **Amazon Linux** or **Ubuntu** image.
- Configure the security group to allow **inbound traffic on port 5000**.
- SSH into the EC2 instance.

### 2. Install Dependencies
SSH into your EC2 instance and run the following commands to install Python, pip, and Flask:

```bash
# Update package manager
sudo apt update

# Install Python, pip, and Flask
sudo apt install python3 python3-pip
pip3 install flask requests
3. Add Your Flask App Code
Create a new Python file (e.g., app.py) and paste your Flask app code. Replace the JIRA API token and email in your code with your actual credentials.

4. Run the Flask App
Start your Flask app by running the following command:

bash
Copy
Edit
python3 app.py
The app will start running on port 5000 by default.

5. Set Up GitHub Webhook
In your GitHub repository, go to Settings → Webhooks → Add webhook.

Set the payload URL to point to the EC2 instance's public IP on port 5000:

bash
Copy
Edit
http://<your-ec2-ip>:5000/createJIRA
Set the content type to application/json.

Select Let me select individual events and choose Issue comment.

Save the webhook.

6. Test the Integration
To trigger the JIRA ticket creation, comment /jira on a GitHub issue.

The Flask app will receive the webhook, detect the comment, and create a JIRA ticket.

Example Request from GitHub Webhook
Endpoint:
bash
Copy
Edit
POST http://<your-ec2-ip>:5000/createJIRA
Request Body:
json
Copy
Edit
{
  "action": "created",
  "issue": {
    "url": "https://api.github.com/repos/<username>/<repo>/issues/1",
    "title": "Example Issue",
    "body": "This is a test issue"
  },
  "comment": {
    "body": "/jira"
  }
}
Response:
json
Copy
Edit
{
  "id": "XXXX",
  "key": "ADG-1",
  "self": "https://aadeshdinkargupta2003.atlassian.net/rest/api/3/issue/XXXX"
}
Notes
Security: Ensure your EC2 instance is properly secured, and only trusted sources can access the Flask app.

Cost: Running the app on EC2 incurs AWS charges, so monitor your costs.

JIRA API: Make sure your JIRA account has API access and your API token is valid.

GitHub Webhook: Ensure the webhook is properly configured to send data to the Flask app.

This app allows for a seamless integration between GitHub and JIRA by automating ticket creation via issue comments.