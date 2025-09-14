import os
import pickle


def export_artifact(obj, path: str):
    try:
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Serializar el objeto
        with open(path, 'wb') as f:
            pickle.dump(obj, f)
    except (OSError, IOError) as e:
        print(f"Error writing artifact to {path}: {e}")
    except pickle.PickleError as e:
        print(f"Pickle error while exporting artifact: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def load_artifact(path: str):
    try:
        with open(path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except pickle.UnpicklingError:
        print(f"Error unpickling file: {path}")
    except Exception as e:
        print(f"Unexpected error while loading artifact: {e}")
