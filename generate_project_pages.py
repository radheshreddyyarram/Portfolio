import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - Project by Radhesh Reddy Yarram">
    <title>{title} | Radhesh Reddy Yarram</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav id="navbar">
        <div class="nav-content">
            <a href="index.html" class="logo">RY<span>.</span></a>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="education.html">Education</a></li>
                <li><a href="skills.html">Skills</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
            <div class="hamburger">
                <div class="line"></div>
                <div class="line"></div>
                <div class="line"></div>
            </div>
        </div>
    </nav>

    <!-- Content Wrapper -->
    <div style="padding-top: var(--nav-height); min-height: calc(100vh - 80px);">
        <section class="section">
            <div class="container" style="max-width: 800px;">
                <a href="projects.html" style="display: inline-block; margin-bottom: 2rem; color: var(--accent); text-decoration: none; font-weight: 600;">&larr; Back to Projects</a>
                
                <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">{title}</h1>
                <div class="tags" style="margin-bottom: 2rem;">
                    {tags}
                </div>

                <div class="project-details" style="font-size: 1.1rem; color: var(--text-secondary); line-height: 1.8;">
                    {content}
                </div>

                {links}
            </div>
        </section>
    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Radhesh Reddy Yarram. Built with passion.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>"""

projects = [
    {
        "filename": "project-healthbot.html",
        "title": "AI Health Chat Bot",
        "tags": "<span>Python</span><span>AI Chatbot</span><span>SMS/WhatsApp API</span>",
        "content": """
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Project Overview</h3>
            <p>The AI Health Chat Bot is a specialized, multi-lingual conversational AI engineered specifically for communities residing in areas with low internet connectivity. By relying on low-bandwidth protocols like SMS and WhatsApp, it guarantees critical health information remains accessible to everyone, regardless of their network constraints.</p>
            
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Key Features</h3>
            <ul>
                <li><strong>Multi-Lingual Support:</strong> Breaks down language barriers by conversing with users in their native dialects.</li>
                <li><strong>Low-Bandwidth Accessibility:</strong> Operates fully over SMS and WhatsApp, bypassing the need for 4G/5G internet access.</li>
                <li><strong>Vaccination Scheduling:</strong> Automates reminders and helps users coordinate vital vaccination appointments seamlessly.</li>
                <li><strong>Emergency Assistance:</strong> Provides rapid, automated responses for urgent medical inquiries.</li>
                <li><strong>Voice & Text Capabilities:</strong> Accommodates various literacy levels by supporting both text-based and speech-based inputs.</li>
            </ul>

            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Technical Implementation</h3>
            <p>Developed entirely in Python, the system integrates advanced Natural Language Processing (NLP) to comprehend user intent. It seamlessly connects with Twilio and WhatsApp Business APIs to handle the routing of text and voice data, ensuring high uptime and reliable message delivery under constrained network scenarios.</p>
        """,
        "links": """<div style="margin-top: 3rem; display: flex; gap: 1rem; flex-wrap: wrap;"><a href="https://www.linkedin.com/posts/radhesh-reddy-yarram-a8b6a82b5_collaboration-ai-machinelearning-activity-7425496869755174913-ehyz?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEu-PgsBJpksfXyoGndBVsjvLFTtnCOIA8g" target="_blank" class="btn secondary-btn" style="background-color: #0A66C2; color: white; border-color: #0A66C2; display: inline-block;">View LinkedIn Post</a></div>"""
    },
    {
        "filename": "project-newsletter.html",
        "title": "AI-Powered Cybersecurity Newsletter",
        "tags": "<span>Python</span><span>Gemini LLM</span><span>RSS & SerpAPI</span>",
        "content": """
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Project Overview</h3>
            <p>Staying updated with the latest threats in cybersecurity is an overwhelming task due to the sheer volume of daily information. To solve this, I engineered an automated intelligence pipeline that acts as a personal cybersecurity analyst, curating, analyzing, and summarizing global security events into a digestible daily email newsletter.</p>
            
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Workflow Architecture</h3>
            <ul>
                <li><strong>Data Aggregation:</strong> Python scripts continuously monitor prominent cybersecurity RSS feeds and utilize SerpAPI to scrape real-time vulnerability reports and breach news.</li>
                <li><strong>LLM Processing:</strong> The raw data is passed into the Google Gemini LLM, which is prompted to extract key insights, assess threat levels, and summarize the findings into concise paragraphs.</li>
                <li><strong>Automated Delivery:</strong> The final formatted HTML newsletter is automatically distributed to a subscriber list via an SMTP email integration.</li>
            </ul>

            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Impact</h3>
            <p>This project showcases the powerful synergy between web scraping and Large Language Models. It completely automates the time-consuming process of OSINT (Open-Source Intelligence) gathering, providing actionable security updates with zero manual intervention.</p>
        """,
        "links": """<div style="margin-top: 3rem; display: flex; gap: 1rem; flex-wrap: wrap;"><a href="https://www.linkedin.com/posts/radhesh-reddy-yarram-a8b6a82b5_automation-ai-workflowautomation-activity-7428342922544271360-LyYQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEu-PgsBJpksfXyoGndBVsjvLFTtnCOIA8g" target="_blank" class="btn secondary-btn" style="background-color: #0A66C2; color: white; border-color: #0A66C2; display: inline-block;">View LinkedIn Post</a></div>"""
    },
    {
        "filename": "project-linkedin.html",
        "title": "Automated Content Publishing System",
        "tags": "<span>n8n</span><span>Groq AI</span><span>LinkedIn API</span>",
        "content": """
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Project Overview</h3>
            <p>Managing a professional brand requires consistent, high-quality content. This project is a resilient, end-to-end automation system that takes raw ideas from a spreadsheet and transforms them into engaging, published LinkedIn posts, all while maintaining a human-in-the-loop approval mechanism to ensure quality control.</p>
            
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">System Capabilities</h3>
            <ul>
                <li><strong>Idea Ingestion:</strong> Connects directly to Google Sheets, scanning for new content ideas or bullet points added by the user.</li>
                <li><strong>AI Drafting:</strong> Utilizes Groq AI's high-speed inference capabilities to expand the raw ideas into professional, engaging LinkedIn posts complete with formatting and relevant hashtags.</li>
                <li><strong>Approval Node:</strong> Pauses the workflow and sends an alert to the user. The post is only published once human approval is explicitly granted, ensuring the AI maintains the correct tone.</li>
                <li><strong>Automated Publishing:</strong> Interfaces directly with the LinkedIn Developer API to push the finalized content live on schedule.</li>
            </ul>

            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Technical Focus</h3>
            <p>The core of this system is built on <strong>n8n</strong>, showcasing an advanced understanding of workflow automation, API authentication (OAuth 2.0), error handling, and multi-step data transformation.</p>
        """,
        "links": """<div style="margin-top: 3rem; display: flex; gap: 1rem; flex-wrap: wrap;"><a href="https://www.linkedin.com/posts/radhesh-reddy-yarram-a8b6a82b5_automation-workflowdesign-systemthinking-activity-7428389494946693120-vGuv?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEu-PgsBJpksfXyoGndBVsjvLFTtnCOIA8g" target="_blank" class="btn secondary-btn" style="background-color: #0A66C2; color: white; border-color: #0A66C2; display: inline-block;">View LinkedIn Post</a></div>"""
    },
    {
        "filename": "project-ordertracking.html",
        "title": "Order Tracking Management System",
        "tags": "<span>C Programming</span><span>File Handling</span><span>CRUD Operations</span>",
        "content": """
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Project Overview</h3>
            <p>A foundational software engineering project that digitizes traditional order management. Built entirely in C, this terminal-based application demonstrates core computer science principles by implementing full CRUD (Create, Read, Update, Delete) operations without relying on high-level databases.</p>
            
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Technical Features</h3>
            <ul>
                <li><strong>Memory Management:</strong> Heavily utilizes C structures (`struct`) and arrays to handle complex relational data in memory efficiently.</li>
                <li><strong>Persistent Storage:</strong> Implements deep file-handling techniques (`fread`, `fwrite`) to ensure customer order records persist reliably across application restarts.</li>
                <li><strong>Interactive Menu:</strong> Provides a robust, user-friendly terminal interface for administrators to seamlessly add new orders, update shipping statuses, and generate tracking reports.</li>
            </ul>

            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Learning Outcomes</h3>
            <p>This project solidified my foundational understanding of memory allocation, pointer manipulation, and the mechanics of persistent data storage before transitioning to higher-level frameworks.</p>
        """,
        "links": """<div style="margin-top: 3rem; display: flex; gap: 1rem; flex-wrap: wrap;">
            <a href="https://github.com/radheshreddyyarram/Order-Tracking-Management-System" target="_blank" class="btn primary-btn" style="display: inline-block;">View Source on GitHub</a>
            <a href="https://www.linkedin.com/posts/radhesh-reddy-yarram-a8b6a82b5_github-radheshreddyyarramordertrackingmanagementsyste-activity-7428389494946693120-vGuv?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEu-PgsBJpksfXyoGndBVsjvLFTtnCOIA8g" target="_blank" class="btn secondary-btn" style="background-color: #0A66C2; color: white; border-color: #0A66C2; display: inline-block;">View LinkedIn Post</a>
        </div>"""
    },
    {
        "filename": "project-reportme.html",
        "title": "ReportMe (Smart Debugging Assistant)",
        "tags": "<span>TypeScript</span><span>n8n</span><span>Groq & Gemini</span>",
        "content": """
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Project Overview</h3>
            <p>Built during the "CODEDGE" Hackathon (BYOONDCAMPUZ), ReportMe is an intelligent debugging assistant engineered to help novice programmers understand cryptic error messages. Instead of simply presenting stack traces, ReportMe translates errors into plain, educational language.</p>
            
            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">How It Works</h3>
            <ul>
                <li><strong>Language Detection:</strong> Automatically identifies the programming language context of the submitted code snippet.</li>
                <li><strong>Log Fetching:</strong> Integrates with online compiler APIs to fetch real-world execution error logs.</li>
                <li><strong>Multi-Agent Analysis:</strong> Uses a chained AI workflow involving Groq (for fast preprocessing) and Google Gemini (for deep contextual explanation) to analyze the error and generate a beginner-friendly fix.</li>
            </ul>

            <h3 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">Achievements</h3>
            <p>As the Team Lead for this project, I architected the core n8n workflows and API integrations. The platform successfully demonstrated the potential of AI as a scalable, personalized tutor for computer science education.</p>
        """,
        "links": """<div style="margin-top: 3rem; display: flex; gap: 1rem; flex-wrap: wrap;">
            <a href="https://github.com/radheshreddyyarram/ReportMe" target="_blank" class="btn primary-btn" style="display: inline-block;">View Source on GitHub</a>
            <a href="https://www.linkedin.com/posts/radhesh-reddy-yarram-a8b6a82b5_hackathon-codedge-beyondcampuz-activity-7460851671229911040-5aig?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEu-PgsBJpksfXyoGndBVsjvLFTtnCOIA8g" target="_blank" class="btn secondary-btn" style="background-color: #0A66C2; color: white; border-color: #0A66C2; display: inline-block;">View LinkedIn Post</a>
        </div>"""
    }
]

for p in projects:
    with open(os.path.join(r"c:\Users\yarra\OneDrive\Desktop\Portfolio", p["filename"]), "w", encoding="utf-8") as f:
        f.write(template.format(title=p["title"], tags=p["tags"], content=p["content"], links=p["links"]))

print("Generated 5 project HTML files.")
