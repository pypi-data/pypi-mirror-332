# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

import logging
import sys

from dotenv import load_dotenv
from errorhandler import ErrorHandler

from edfi_google_classroom_extractor.helpers import arg_parser
from edfi_google_classroom_extractor import facade


def _load_configuration() -> arg_parser.MainArguments:
    load_dotenv()
    return arg_parser.parse_main_arguments(sys.argv[1:])


def _configure_logging(arguments: arg_parser.MainArguments):
    logging.basicConfig(
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        level=arguments.log_level,
    )


def _main(arguments):
    error_tracker = ErrorHandler()

    facade.run(arguments)

    if error_tracker.fired:
        print(
            "A fatal error occurred, please review the log output for more information.",
            file=sys.stderr,
        )
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    arguments = _load_configuration()
    _configure_logging(arguments)
    _main(arguments)
