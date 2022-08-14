#!/usr/bin/env python
# -*- coding:utf-8 -*-
import typer

from spell.generator.client_codes import generate_service, generate_model

app = typer.Typer(name="client")


@app.command(name="service", help="generate service codes")
def generate_rpc_code(service_name: str = typer.Option(..., "--service", "-s", help="service name"),
                      product: str = typer.Option("pcf", "--product", "-p", help="product name,"),
                      idl_file: str = typer.Option(None, "--idl_file", "-i", help="NCP protocol IDL file"),
                      option: str = typer.Option("SERVICE", "--option", "-o",
                                                 help="code gen options: SERVICE,TEST,BOTH")):
    generate_service(service_name, product, idl_file, option)


@app.command(name="model", help="generate model code")
def generate_model_code(service_name: str = typer.Option(..., "--service", "-s", help="service name"),
                        product: str = typer.Option("pcf", "--product", "-p", help="product name,")):
    generate_model(service_name=service_name, product_name=product)
