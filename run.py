# -*- coding: utf-8 -*-
import sys

# Core modules
from core.startup import run
from core.startup import create_app
from core.startup import load_config


if __name__ == '__main__':
    # Get the app according to the provided profile
    app = create_app(name=__name__, config=load_config(sys.argv[1]))
    
    # Spin up the development server
    run(app)
