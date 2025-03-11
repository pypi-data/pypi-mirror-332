A flexible SDK for interacting with various model types including BERT, Inkman, and BiasTPV.

Installation
pip install modelsdk

Features
Unified interface for different model types
Easily extensible to support new models

Usage
Basic Usage
from modelsdk import ModelSDK

# Create an Inkman model instance
inkman = ModelSDK("inkman")

# Get model run id
run_id = inkman.get_run_id()

# Get features
features = inkman.get_features()

# Get factors
factors = inkman.get_factors()

# Get model users data (requires a pid)
pid = datetime.now().strftime("%Y%m%dT%H%M%S")
source_data = inkman.get_users_df(pid=pid)

Available Models
 - inkman

Environment Variables
The SDK uses these environment variables:
GOOGLE_CLOUD_PROJECT
MLFLOW_TRACKING_URI
MLFLOW_TRACKING_USERNAME
MLFLOW_TRACKING_PASSWORD

License