from dotenv import load_dotenv
import os


def ensure_envvar_DB_xx_defined():
    """
    ensure envvar DB_xx defined in $AH/.env
    """
    load_dotenv()
    assert os.environ.get('DB_USER')
    assert os.environ.get('DB_PASS')
    assert os.environ.get('DB_HOST')
    assert os.environ.get('DB_NAME')
