import importlib
import logger

def load_outputs(output_data):
    outputs = {}
    for o_key, o_data in output_data.items():
        if o_data.get('enabled', True) is False:
            continue
        try:
            module = importlib.import_module(f"outputs.{o_key}")
        except ModuleNotFoundError:
            logger.warn(f"Invalid output type \'{o_key}\'.")
            continue

        try:
            outputs[o_key] = module.Output(o_data)
        except:
            logger.fatal(f"Invalid format in config for output \'{o_key}\'.")
    return outputs