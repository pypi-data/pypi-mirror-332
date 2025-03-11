# DO NOT CHANGE CONFIG HERE, THESE ARE THE DEFAULTS
# If you want to change the configuration, make use
# the environment variables mapped below.
import os
import ast
from dotenv import load_dotenv
from loguru import logger

from dart_trec_learner.utils.parse import parse_env_to_dict, merge_template_with_env, parse_env_to_list

load_dotenv()

template_dict = {
    'learner_dnn_settings': {
        'model': 'huawei-noah/TinyBERT_General_4L_312D',
        'num_epochs': 5,
        'learning_rate': 1e-5,
        'early_stop': 3,
        'batch_size': 8,
        'batch_size_eval': 8,
        'base': 2,
        'weight_decay': 0.01,
        'warmup_steps': 0,
        'max_length': 512,
        'max_steps': 800,
        'dropout': 0.1,
        'strategy': 'epoch',
        'eval_metric': 'eval_Accuracy',
        'lsf': 0.0,
        'has_fp16': True,
        'use_balanced': True,
    },
}


# Parse the learner_dnn_settings dictionary from environment variables
learner_dnn_settings_env = parse_env_to_dict('LEARNER_DNN_SETTINGS')
learner_dnn_settings = merge_template_with_env(template_dict['learner_dnn_settings'], learner_dnn_settings_env)
langs = parse_env_to_list('LEARNER_LANGUAGES', default=['en'])

default_conf = {
    # Job Configs
    'job_frequency':
        int(os.getenv('JOB_FREQUENCY', 5)),

    # MINIO Configs
    "minio_host":
        os.getenv("MINIO_HOST"),
    "minio_access_key":
        os.getenv("MINIO_ACCESS_KEY"),
    "minio_secret_key":
        os.getenv("MINIO_SECRET_KEY"),
    "minio_recommender_bucket":
        os.getenv("MINIO_RECOMMENDER_BUCKET"),

    # MongoDB Configs
    'mongodb_uri':
        os.getenv('MONGODB_URI'),
    'mongodb_collection':
        os.getenv('MONGODB_COLLECTION', 'issue_document'),

    # Learner Configs
    'learner_days_interval':
        int(os.getenv('LEARNER_DAYS_INTERVAL', 180)),
    'learner_recommender_root_model_dir':
        os.getenv('LEARNER_ROOT_MODEL_DIR', 'tg_recomender_models'),
    'learner_recommender_model_dir':
        os.path.join(os.getenv('LEARNER_ROOT_MODEL_DIR', 'tg_recomender_models'),
                     os.getenv('LEARNER_MODEL_DIR', 'latest')),
    'learner_test_size':
        os.getenv("LEARNER_TEST_SIZE", 0.1),

    # Validator Params
    'validator_top_k': [1, 2, 3, 5, 10, 20],

    # Model Params
    'learner_label': 'tg_solver_id',
    'learner_textual_columns': ['title', 'description', 'steps_to_reproduce'],  # 'title_tags',
    'learner_categorical_columns': [
        'module_detail', 'module_name', 'reg_open_yn', 'reporter_department',
        'defect_type', 'test_item'
    ],
    'learner_dnn_settings': learner_dnn_settings,
    'langs': langs,
    'min_issues': int(os.getenv('MIN_ISSUES', 10)),
    'end_date': os.getenv('END_DATE', None),
    'start_date': os.getenv('START_DATE', None),
}


class Config():
    def __init__(self):
        self._config = default_conf

    @property
    def options(self):
        return self._config

    def get(self, prop, default=None):
        if prop not in self._config.keys():
            return default
        return self._config[prop]

    def print_config(self):
        for key, value in self._config.items():
            logger.debug(f"{key}: {value}")


config = Config()
config.print_config()

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
