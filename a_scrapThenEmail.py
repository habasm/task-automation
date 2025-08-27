import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def fetch_hn_top_stories(limit=10):
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    stories = []
    for item in soup.select('tr.athing')[:limit]:
        story = {}
        title_tag = item.select_one('a.storylink')
        if title_tag:
            story['title'] = title_tag.get_text(strip=True)
            story['link'] = title_tag.get('href')
        else:
            continue

        detail_row = item.find_next_sibling('tr')
        score_tag = detail_row.select_one('span.score')
        story['score'] = score_tag.get_text(strip=True) if score_tag else '0 points'

        time_tag = detail_row.select_one('span.age')
        story['submitted'] = time_tag.get_text(strip=True) if time_tag else 'N/A'

        stories.append(story)
    return stories

def compose_email(stories):
    today = datetime.now().strftime("%d-%m-%Y")
    subject = f"Top News Stories HN [Automated Email] {today}"

    # Create HTML body
    body = "<b>HN Top Stories:</b><br>--------------------------------------------------<br><br>"
    for idx, s in enumerate(stories, start=1):
        body += f"<b>{idx}. {s['title']}</b><br>"
        body += f"Score: {s['score']} — Submitted: {s['submitted']}<br>"
        body += f"<a href='{s['link']}'>{s['link']}</a><br><br>------<br><br>"
    body += "<br>End of Message"

    return subject, body

def send_email(sender, recipient, subject, body, smtp_server, smtp_port, login, password):
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(login, password)
        server.sendmail(sender, recipient, msg.as_string())

if __name__ == "__main__":
    stories = fetch_hn_top_stories(limit=10)
    subject, body = compose_email(stories)

    # Print email preview
    print("Extracting Hacker News Stories...")
    print("Composing Email...")
    print(subject)
    print(body)

    # Uncomment below if you want to actually send email
    # send_email(
    #     sender="your_email@gmail.com",
    #     recipient="receiver_email@example.com",
    #     subject=subject,
    #     body=body,
    #     smtp_server="smtp.gmail.com",
    #     smtp_port=465,
    #     login="your_email@gmail.com",
    #     password="your_app_password"
    # )
