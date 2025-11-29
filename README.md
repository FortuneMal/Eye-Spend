AI Expense Guardian: Real-time Receipt Audit and Risk PredictionProject OverviewThe AI Expense Guardian is a modern, responsive web application built with Streamlit and deployed via Docker and OpenShift. It demonstrates a powerful business process automation workflow: leveraging an AI model (simulated in this demo, typically Gemini Vision or similar) to perform Optical Character Recognition (OCR) on expense receipts, categorize the spending, and immediately assign a Risk Score based on predefined corporate policies and anomaly detection.This tool accelerates the approval process by automatically flagging high-risk or policy-violating expenses, providing instant Auto-Approve or Auto-Reject recommendations. FeaturesReal-time Receipt Upload: Users can upload JPG or PNG receipt images.Simulated AI Analysis: Mocks OCR extraction (Vendor, Amount, Category) and calculates a dynamic Risk Score (0-100).Dynamic Risk Scoring: Implements business logic to flag expenses based on amount thresholds (e.g., > $1000) and suspicious vendor names.Styled Risk Summary: Visually distinct card displaying the final approval recommendation (Auto-Approve, Review, Auto-Reject).Coaching & Budget Forecasting: Provides an advanced tab with aggregated financial advice and predicted monthly spend based on historical analysis.Containerized Deployment: Includes Docker and Kubernetes/OpenShift configuration for secure, scalable deployment.
Project Structure.
├── app.py                      # Main Streamlit application and UI logic
├── Dockerfile                  # Defines the non-root, production-ready container image
├── docker-compose.yml          # Local environment setup for quick development
├── k8s_deployment.yaml         # Kubernetes/OpenShift Deployment, Service, and Route
├── requirements.txt            # Python dependencies (Streamlit, pandas, pytest)
├── test_app.py                 # Unit tests for core business logic (risk flagging)
└── README.md                   # This file
Local Development SetupThe easiest way to run the application locally is using Docker Compose.PrerequisitesDocker and Docker Compose installed.Python 3.9+ (Optional, for running outside Docker).StepsClone the Repository:git clone [YOUR_REPO_URL]
cd ai-expense-guardian
Build and Run the Containers:docker-compose up --build
This command builds the Docker image defined in Dockerfile and starts the application. OpenShift DeploymentThis application is configured for deployment on OpenShift, prioritizing security and stability through a non-root user and explicit configurations for proxy environments.
1. Image Build & PushEnsure your container image is built and pushed to a registry accessible by your OpenShift cluster (e.g., Quay, GitLab Registry).docker build -t your-registry.io/your-namespace/expense-app:latest .
docker push your-registry.io/your-namespace/expense-app:latest
2. Update and Apply Kubernetes ManifestThe k8s_deployment.yaml contains the Deployment, Service, and Route definitions. 
IMPORTANT: Before applying, you must update the image: placeholder in k8s_deployment.yaml with your actual registry image path.# Inside k8s_deployment.yaml:
      containers:
      - name: expense-app
        # REPLACE THIS LINE:
        image: your-registry.io/your-namespace/expense-app:latest 
Apply the configuration to your OpenShift cluster:oc apply -f k8s_deployment.yaml
The OpenShift Route will expose the application publicly, making the AI Expense Guardian accessible via a URL provided by the platform.🛠️ TestingUnit tests for the business logic (risk flagging and data structure) are located in test_app.py.Run tests locally using pytest:pip install -r requirements.txt
pytest
DependenciesAll Python dependencies are listed in requirements.txt:streamlitpandaspytestpytest-mock
