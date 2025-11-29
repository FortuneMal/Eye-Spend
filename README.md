💰 AI Expense Guardian: Real-time Receipt Audit and Risk PredictionProject OverviewThe AI Expense Guardian is a modern, responsive web application built with Streamlit and deployed using Docker and OpenShift. It demonstrates a powerful financial process automation workflow: leveraging a simulated AI model to perform Optical Character Recognition (OCR) on expense receipts, categorize the spending, and immediately assign a Risk Score based on predefined corporate policies and anomaly detection.This tool significantly accelerates the expense approval process by automatically flagging high-risk or policy-violating expenses, providing instant Auto-Approve or Auto-Reject recommendations. The application also features a Coaching section with aggregate analysis and budget forecasting.🚀 FeaturesReal-time Receipt Upload: Users can upload JPG or PNG receipt images.Simulated AI Analysis: Mocks OCR extraction (Vendor, Amount, Category) and calculates a dynamic Risk Score (0-100).Dynamic Risk Scoring: Implements business logic to flag expenses based on amount thresholds (e.g., > $1000) and suspicious vendor types.Styled Risk Summary: Visually distinct card displaying the final approval recommendation (Auto-Approve, Review, Auto-Reject).Coaching & Budget Forecasting: Provides an advanced tab with aggregated financial advice and predicted monthly spend based on historical analysis.OpenShift-Ready Containerization: Uses a non-root, secured Docker image and includes necessary configuration for deployment in restrictive environments like OpenShift.📦 Project Structure.
├── app.py                      # Main Streamlit application, UI, and business logic
├── .streamlit/                 # Directory containing Streamlit configuration files
│   └── config.toml             # Configuration for OpenShift (disables XSRF protection)
├── Dockerfile                  # Defines the non-root, production-ready container image
├── docker-compose.yml          # Local environment setup for quick development
├── k8s_deployment.yaml         # Kubernetes/OpenShift Deployment, Service, and Route
├── requirements.txt            # Python dependencies (Streamlit, pandas, pytest)
├── test_app.py                 # Unit tests for core business logic (risk flagging)
└── README.md                   # This file
⚙️ Local Development SetupThe easiest way to run the application locally is using Docker Compose.PrerequisitesDocker and Docker Compose installed.StepsClone the Repository:git clone [YOUR_REPO_URL]
cd ai-expense-guardian
Build and Run the Containers:docker-compose up --build
This command builds the Docker image defined in Dockerfile and starts the Streamlit server.Access the App:Open your web browser and navigate to:http://localhost:8501
☁️ OpenShift Deployment GuideThis application is configured for secure deployment on OpenShift, ensuring compliance with Security Context Constraints (SCCs) and proper handling of proxied requests.1. Image Build & PushEnsure your container image is built with the OpenShift-compliant Dockerfile (which uses a non-root user) and pushed to a registry accessible by your OpenShift cluster.# Build the image
docker build -t your-registry.io/your-namespace/expense-app:latest .

# Push to your registry
docker push your-registry.io/your-namespace/expense-app:latest
2. Configure API Key SecretThe application expects the API key to be provided via a Kubernetes/OpenShift Secret named app-secrets. This must be created before deployment.Use the following command to create the secret, replacing *** with your actual API key, and ensuring the namespace is correct (redkom-dev):kubectl create secret generic app-secrets \
  --from-literal=api-key=*** \
  --namespace=redkom-dev
3. Update and Apply Kubernetes ManifestThe k8s_deployment.yaml defines the Deployment, Service, and Route.⚠️ IMPORTANT: You must update the image: field in k8s_deployment.yaml with your actual registry image path before applying.# Inside k8s_deployment.yaml (Look for image: REPLACE_ME_IMAGE):
      containers:
      - name: expense-app
        image: your-registry.io/your-namespace/expense-app:latest 
        # ... rest of container config ...
Apply the configuration to your OpenShift cluster:oc apply -f k8s_deployment.yaml
The OpenShift Route will expose the application publicly, making the AI Expense Guardian accessible via the assigned public URL.🧪 TestingUnit tests for the core business logic (risk flagging and data structure) are located in test_app.py.Run tests locally using pytest:pip install -r requirements.txt
pytest
