import docker
import logger
from datetime import datetime, timedelta
from config import load_config
from outputs import load_outputs


if __name__ == '__main__':
    config = load_config()

    if config is None:
        logger.fatal("Config file not found. Please add a config.yml file to the root of the project.")

    if 'events' not in config or 'outputs' not in config:
        logger.fatal("Invalid format for config file. Please see the README for more information.")

    options = config.get('options', {}) or {}
    events = config.get('events', {}) or {}
    output_data = config.get('outputs', {}) or {}

    outputs = load_outputs(output_data)

    exclude = options.get('exclude', [])
    include = options.get('include', [])

    if len(outputs) == 0:
        logger.warn(
            "No outputs configured. Please see the README for more information.")
    
    client = docker.from_env()

    delta = timedelta(seconds = 2)
    since = datetime.utcnow()
    until = datetime.utcnow() + delta

    while True:
        for event in client.events(since=since, until=until, decode=True):
            event_type = event.get('Type', None)
            event_action = event.get('Action', None)
            if event_type in events and event_action in events[event_type]:
                event_from = event.get('from', None)

                if (len(include) > 0 and event_from not in include) or event_from in exclude:
                    continue

                for output in outputs.values():
                    output.fire_event(event)
        since = until
        until = datetime.utcnow() + delta