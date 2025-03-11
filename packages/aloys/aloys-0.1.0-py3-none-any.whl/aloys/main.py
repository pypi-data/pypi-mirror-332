"""
Main module of the project.
"""
import os
import random
import pickle
import logging

import click
import pandas

from aloys.utils import say,add

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



# TODO : Say hello to more people
@click.command()
@click.option(
    "--name",
    prompt="Your name",
    help="The person to greet.",
)
def hello(name):
    """Say hello to NAME."""
    click.echo(f"Hello {name}!")
    logger.log(logging.INFO,"✅ Hello executed.")


if __name__ == "__main__":
    from loguru import logger
    
    logger.info("Running main.py as a script.")
    say("world")
    logger.info(f" {__name__=}")
    logger.debug("Pls Help ! ")
    logger.error(add(1, 1))
    
