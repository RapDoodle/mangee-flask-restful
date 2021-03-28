# -*- coding: utf-8 -*-
import sys

# Core modules
from core.startup import run
from core.startup import create_app
from core.startup import load_config
from core.startup import init_core_modules
from core.startup import load_resources


if __name__ == '__main__':
    # Get the app according to the provided profile
    app = create_app(name=__name__, config=load_config(sys.argv[1]))

    # Initialize core modules
    init_core_modules(app)

    # Dynamically load all resources
    load_resources(app)
    
    # Spin up the server
    run(app)
