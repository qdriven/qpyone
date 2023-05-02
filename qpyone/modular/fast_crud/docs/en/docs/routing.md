Automatic route generation is the meat and potatoes of CRUDRouter's features.  Detail below is how you can prefix, customize,
and disable any routes generated by the CRUDRouter.

## Default Routes
By default, the CRUDRouter will generate the six routes below for you. 

| Route        | Method   | Description
| ------------ | -------- | ----
| `/`          | `GET`    | Get all the resources 
| `/`          | `POST`   | Create a new resource 
| `/`          | `DELETE` | Delete all the resources
| `/{item_id}` | `GET`    | Get an existing resource matching the given `item_id`
| `/{item_id}` | `PUT`    | Update an existing resource matching the given `item_id`
| `/{item_id}` | `DELETE` | Delete an existing resource matching the given `item_id`

!!! note "Route URLs"
    Note that the route url is prefixed by the defined prefix.

    **Example:** If the CRUDRouter's prefix is set as *potato* and I want to update a specific potato the route I want to access is
    `/potato/my_potato_id` where *my_potato_id* is the ID of the potato.

## Prefixes
Depending on which CRUDRouter you are using, the CRUDRouter will try to automatically generate a suitable prefix for your
model.  By default, the [MemoryCRUDRouter](backends/memory.md) will use the pydantic model's name as the prefix.  However,
the [SQLAlchemyCRUDRouter](backends/sqlalchemy.md) will use the model's table name as the prefix.

!!! tip "Custom Prefixes"
    You are also able to set custom prefixes with the `prefix` kwarg when creating your CRUDRouter. This can be done like so:
    `router = CRUDRouter(model=mymodel, prefix='carrot')`

## Disabling Routes
Routes can be disabled from generating with a key word argument (kwarg) when creating your CRUDRouter. The valid kwargs 
are shown below.

| Argument         | Default | Description 
| ---------------- | ------  | ---
| get_all_route    | True    | Setting this to false will prevent the get all route from generating
| get_one_route    | True    | Setting this to false will prevent the get one route from generating
| delete_all_route | True    | Setting this to false will prevent the delete all route from generating
| delete_one_route | True    | Setting this to false will prevent the delete one route from generating
| create_route     | True    | Setting this to false will prevent the create route from generating
| update_route     | True    | Setting this to false will prevent the update route from generating

As an example, the *delete all* route can be disabled by doing the following:
```python
router = MemoryCRUDRouter(schema=MyModel, delete_all_route=False)
```

!!! tip "Custom Dependencies"
    Instead to passing a bool to the arguments listed about, you can also pass a sequence of custom dependencies to be 
    applied to each route. See the docs on [dependencies](dependencies.md) for more details.


## Overriding Routes
Should you need to add custom functionality to any of your routes any of the included routers allows you to do so. 
Should you wish to disable a route from being generated, it can be done [here](../routing/#disabling-routes).

Routes in the CRUDRouter can be overridden by using the standard fastapi route decorators. These include:

 -  `@router.get(path: str, *args, **kwargs)`
 -  `@router.post(path: str, *args, **kwargs)`
 -  `@router.put(path: str, *args, **kwargs)`
 -  `@router.delete(path: str, *args, **kwargs)`
 -  `@router.api_route(path: str, methods: List[str] = ['GET'], *args, **kwargs)`

!!! tip
    All of CRUDRouter's are a subclass of fastapi's [APIRouter](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter)
    meaning that they can be customized to your heart's content.

### Overriding Example
Below is an example where we are overriding the routes `/potato/{item_id}` and `/potato` while using the MemoryCRUDRouter.

```python
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

class Potato(BaseModel):
    id: int
    color: str
    mass: float

app = FastAPI()
router = CRUDRouter(schema=Potato)

@router.get('')
def overloaded_get_all():
    return 'My overloaded route that returns all the items'

@router.get('/{item_id}')
def overloaded_get_one():
    return 'My overloaded route that returns one item'

app.include_router(router)
```