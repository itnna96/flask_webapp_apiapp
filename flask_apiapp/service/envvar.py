from dotenv import load_dotenv
import os


def ensure_envvar_DB_xx_defined(debug=False):
    """
    ensure envvar DB_xx defined in $AH/.env
    """
    if debug:
        print('Before')
        k='DB_USER'; v=os.environ.get(k); print(f'{k}={v}')
        k='DB_PASS'; v=os.environ.get(k); print(f'{k}={v}')
        k='DB_HOST'; v=os.environ.get(k); print(f'{k}={v}')
        k='DB_NAME'; v=os.environ.get(k); print(f'{k}={v}')

    load_dotenv(verbose=True)

    if debug:
        print('After')
        k='DB_USER'; v=os.environ.get(k); assert v, f'Envvar {k} is required'; print(f'{k}={v}')
        k='DB_PASS'; v=os.environ.get(k); assert v, f'Envvar {k} is required'; print(f'{k}={v}')
        k='DB_HOST'; v=os.environ.get(k); assert v, f'Envvar {k} is required'; print(f'{k}={v}')
        k='DB_NAME'; v=os.environ.get(k); assert v, f'Envvar {k} is required'; print(f'{k}={v}')
