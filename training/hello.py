import os
import sys
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.workflow.parameters import ParameterInteger, ParameterString

# For Preprocess Step
from sagemaker.workflow.steps import ProcessingStep
from sagemaker.processing import Processor
from sagemaker.processing import ProcessingInput, ProcessingOutput

# For Train Step
from sagemaker.estimator import Estimator
from sagemaker.workflow.steps import TrainingStep
from sagemaker.inputs import TrainingInput

# For Model Step
from sagemaker.model import Model
from sagemaker.workflow.model_step import ModelStep

# For Pipeline
from sagemaker.workflow.pipeline import Pipeline

execution_role_arn = os.environ["EXECUTION_ROLE_ARN"]
print(execution_role_arn)
