#!/usr/bin/env python
# -*- coding:utf-8 -*-

import typer

from spell.cli import spell_generator

app = typer.Typer(name="spell-codegen-cli")
app.add_typer(spell_generator.app, name="clients")

if __name__ == '__main__':
    app()
