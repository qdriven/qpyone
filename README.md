# qqyone: Python All-in-One lib for Software QA
<a href="https://github.com/qdriven/qpyone/actions"><img alt="Actions Status" src="https://github.com/qdriven/qpyone/workflows/build/badge.svg"></a>

[![Build status](https://github.com/qdriven/qpyone/workflows/build/badge.svg?branch=main&event=push)](https://github.com/qdriven/qpyone/actions?query=workflow%3Abuild)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
![coverage](./assets/images/coverage.svg)

***qpyone*** stands, one python lib for QA.
This lib integrates most useful libs for QA Daily tasks.

## Modules
1. **builtin**
   - [] dicttool

## Rethink Python base libs as composer

fluentqa-composer include:

1. base cmd 
2. injector: injector 
3. config: base configuration


## plugin model

- register into main app
- service register into main app
- expose as service or methods

- main engine
1. register service
2. init service, service,methods and args
3. dispatch any inbound request 
4. any dispatch method could be executed in an async worker or event bus to get response

## Logger

- [loguru](https://github.com/Delgan/loguru)
## DI
- [kink](https://github.com/kodemore/kink)
- [python-dependency-injector](https://github.com/ets-labs/python-dependency-injector.git)
- 
## database module
- [database]
- [sqlarchmey]
- [sqlmode]

## data model

- [dataclass-wizard](https://github.com/rnag/dataclass-wizard.git)

## utils:
-  https://github.com/twocucao/hutoolpy.git
- 
## Demos
- [todo](https://github.com/GArmane/python-fastapi-hex-todo.git)

### Django Demo
- [yadrta](https://github.com/SerhatTeker/yadrta.git)

## proxy

- [proxy.py](https://github.com/abhinavsingh/proxy.py.git)
- [proxypool](https://github.com/Python3WebSpider/ProxyPool.git)


## DDD


## To Do

- [] DI Implementation
- [] plugin pattern
- [] workflow/pipeline pattern
- [] more enhanced 

## Integrations

- [X][atlassian-python-api]( https://github.com/atlassian-api/atlassian-python-api.git)
