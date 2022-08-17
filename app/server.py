#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fastapi import FastAPI, File

from loader import install_module as install_archived_module
from loader import load_plugins, registry, reload_plugins

app = FastAPI()

load_plugins()


@app.get("/")
async def list_modules():
    """List installed modules"""
    return {"modules": registry.modules()}


@app.get("/reload")
async def reload_modules():
    """Reload all installed modules"""
    reload_plugins()
    return {"modules": registry.modules()}


@app.post("/install")
async def install_module(file: bytes = File(...)):
    """Install module from a ZIP archive"""
    details = install_archived_module(file)
    return details


@app.post("/run/{module}/{action}")
async def execute_module_action(module: str, action: str):
    """Execute action from a specific package"""
    return registry.get_action(module_name=module, action=action)()
