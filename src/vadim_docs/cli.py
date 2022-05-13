#!/usr/bin/env python
import click
from dataclasses import dataclass
from typing import Tuple, Optional
from google.oauth2.credentials import Credentials
from simple_settings import LazySettings

from vadim_docs import services

settings = LazySettings('vadim_docs.settings')


@dataclass
class Config:
    creds: Optional[Credentials]


@click.group()
@click.pass_context
def cli(ctx: click.Context):
    ctx.obj = Config
    ctx.obj.creds = services.get_creds()


@cli.command()
@click.pass_context
@click.argument('presentations-ids', nargs=-1)
def get_presentation_details(ctx: click.Context, presentations_ids: Tuple[str]):
    for presentation_id in presentations_ids:
        services.get_presentation_details(presentation_id, ctx.obj.creds)


if __name__ == '__main__':
    cli()
