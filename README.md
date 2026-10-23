🔧 NeedSense Repair Advisor
AI-assisted repair tool recommendations for mobile phone repair technicians, powered by Amazon cloud technologies.
🔗 GitHub Repository: https://github.com/Josephine2016/NeedSense-Repair-Advisor
💡 About the Project
NeedSense Repair Advisor is an AI-assisted application designed to help mobile phone repair technicians identify potentially suitable repair tools based on their repair problem and available budget.
For this Amazon-focused hackathon, the project demonstrates how cloud-based AI and serverless services can support practical decision-making for repair businesses. Technicians describe the problem they are investigating, enter their budget, and receive product recommendations from a sample catalogue alongside AI-generated repair advice.
The solution is designed with a path toward Amazon Web Services integration, including Amazon Bedrock for foundation-model-powered repair guidance, Amazon DynamoDB for product and technician data, Amazon S3 for technical documents, and Amazon CloudWatch for monitoring.
The goal is to make repair-tool discovery easier, more practical, budget-conscious, and scalable for technicians and small repair businesses.
🚨 The Problem
Mobile phone repair technicians often face challenges when choosing the right tools for complex repairs.
Finding suitable diagnostic equipment can take time.
Specialised tools can be expensive.
Technicians may need help understanding which tools are relevant to a particular fault.
Choosing unsuitable equipment can waste money and delay repairs.
Small repair businesses may not have access to centralised technical knowledge or intelligent support tools.
💡 Our Solution
NeedSense combines catalogue-based product matching with AI-powered explanations to help technicians explore tools that may be appropriate for their repair task.
Rather than searching a long list of products manually, a technician can describe the problem, set a budget, and review suggested tools with supporting explanations.
The prototype currently uses OpenAI for AI-generated advice and a local sample catalogue. Its architecture is designed to evolve toward Amazon Web Services, where Amazon Bedrock could provide managed foundation-model access, DynamoDB could store catalogue and user data, and S3 could host repair manuals and reference documents.
☁️ Amazon Web Services Scope
NeedSense is positioned as a practical AWS-ready solution for the repair industry.
Potential AWS components include:
Amazon Bedrock: Generate repair guidance and explain why recommended tools may be relevant.
Amazon DynamoDB: Store repair-tool catalogue data, budgets, technician preferences, and recommendation history.
Amazon S3: Store repair manuals, product documentation, images, and other reference materials.
AWS Lambda: Run recommendation and AI-processing workflows without managing servers.
Amazon API Gateway: Provide secure APIs for the web application and future mobile or voice interfaces.
Amazon CloudWatch: Monitor application performance, errors, and AI-service usage.
AWS IAM and Secrets Manager: Protect credentials and control access to AWS resources.
Amazon Cognito: Support secure technician accounts in a future production version.
The current implementation is a working prototype, while these AWS services represent the intended cloud architecture and expansion path.
✨ Key Features
Repair problem input: Describe a repair task using natural language.
Product recommendations: Find potential matches in the repair-tool catalogue.
Budget-aware matching: Use a maximum budget to help filter recommendations.
AI repair advice: Generate explanations based on the repair request and matched products.
Simple interface: Use the application through a browser.
Technician-focused design: Support decision-making without replacing professional judgement.
AWS-ready architecture: Designed for future integration with Amazon Bedrock, DynamoDB, S3, Lambda, and related AWS services.
Alexa+ tool specification: The README documents the Alexa+ tool as a planned integration point for supported voice-assistant or agent interfaces; a live Alexa+ integration is not currently established.
🛠️ Technology Stack
Python
Streamlit
OpenAI API
python-dotenv
Amazon Web Services integration planned
Amazon Bedrock integration planned for managed AI inference
Amazon DynamoDB integration planned for catalogue and application data
Amazon S3 integration planned for repair documentation
AWS Lambda and API Gateway integration planned for a serverless deployment
Alexa+ tool integration planned for future development
⚙️ How It Works
Enter a mobile phone repair problem.
Specify your available budget in Nigerian naira.
The application searches the sample product catalogue.
The matched products are passed to the AI advice function.
OpenAI currently generates an explanation based on the repair request and matched products.
In the planned AWS architecture, Amazon Bedrock would provide the managed foundation-model inference layer.
Product data and repair references could be stored in DynamoDB and S3.
Review the suggestions and verify that the tools are suitable for the repair.
🚀 Getting Started
Requirements
Python 3.10 or later
An OpenAI API key with access to a supported model
An internet connection for AI requests
AWS account for future AWS service deployment
1. Clone the repository
git clone https://github.com/Josephine2016/NeedSense-Repair-Advisor.git
cd NeedSense-Repair-Advisor

2. Install dependencies
python -m pip install -r requirements.txt

3. Configure your API key
Create a .env file in the project directory and add:
OPENAI_API_KEY=your_openai_api_key_here

Replace the placeholder with your own API key.
For a future AWS deployment, credentials should be managed using IAM roles, AWS Secrets Manager, or another secure AWS credential-management approach rather than hard-coding secrets.
Never publish your actual API key or AWS credentials. Ensure .env is listed in .gitignore so it is not committed to GitHub.
4. Run the application
python -m streamlit run app.py

Open the local address displayed in your terminal, usually http://localhost:8501.
🧪 Example Scenario
Repair problem: Diagnose a phone motherboard that draws excessive current.
Budget: ₦100,000.
NeedSense searches the sample catalogue for potentially relevant equipment, such as a digital multimeter or DC power supply, when supported by the matching logic. Its AI advice function then explains how the matched tools may help with the investigation.
In a future AWS deployment, the application could retrieve product and technical-reference data from DynamoDB and S3, then use Amazon Bedrock to generate grounded repair guidance.
The technician must verify tool suitability and follow appropriate electrical safety procedures.
⚠️ Current Limitations
NeedSense is an early-stage prototype.
Product matching depends on the current catalogue and matching logic.
Catalogue prices are demonstration values and are not verified live market prices.
Live stock availability is not connected.
AI-generated advice may be incomplete or inaccurate.
Amazon Bedrock integration is planned and is not currently active in the prototype.
AWS data storage, authentication, monitoring, and serverless deployment are planned rather than fully implemented.
The application does not replace professional repair expertise.
A live Alexa+ integration has not been established.
🌍 Potential Impact
NeedSense aims to help repair technicians spend less time searching for tools, make more informed equipment choices, and consider their budgets when planning repairs.
By using Amazon Web Services, the project could scale from a local prototype into a cloud-based platform supporting repair businesses, shared product catalogues, technical documentation, secure user accounts, and AI-assisted workflows.
The project explores how Amazon cloud technologies and generative AI can make specialised repair resources easier to navigate and understand, particularly for small businesses and technicians with limited access to formal technical support.
🗺️ Future Improvements
Replace or complement the current OpenAI integration with Amazon Bedrock.
Store product catalogue and recommendation data in Amazon DynamoDB.
Store repair manuals and technical references in Amazon S3.
Deploy recommendation workflows using AWS Lambda and API Gateway.
Add secure technician accounts with Amazon Cognito.
Add monitoring and usage tracking with Amazon CloudWatch.
More accurate AI-assisted repair classification.
Improved matching between symptoms and diagnostic equipment.
Verified technical documentation and repair references.
Live inventory and pricing integration.
Technician feedback and recommendation evaluation.
Integration with the Alexa+ tool and other supported voice-assistant or agent interfaces.
👩‍💻 Project Information
Project: NeedSense Repair Advisor
 Audience: Mobile phone repair technicians and repair businesses
 Hackathon Scope: Amazon Web Services-ready AI solution for repair-tool discovery
 Status: Working prototype with catalogue-based matching and OpenAI integration
 AWS Direction: Amazon Bedrock, DynamoDB, S3, Lambda, API Gateway, CloudWatch, and Cognito
 Repository: https://github.com/Josephine2016/NeedSense-Repair-Advisor
