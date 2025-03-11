# Ad-Hoc API
An [Archytas](https://github.com/jataware/archytas) tool that uses LLMs to interact with APIs given documentation. The user explains what they want in plain english, and then the agent (using the APIs docs for context) writes python code to complete the task.

## Installation
```bash
pip install adhoc-api
```

## Minimal Example

Here is a complete example of grabbing the HTML content of an API documentation page, converting it to markdown, and then having the adhoc-api tool interact with the API using the generated markdown documentation (see [examples/jokes.py](examples/jokes.py) for reference):

```python
from archytas.react import ReActAgent, FailedTaskError
from archytas.tools import PythonTool
from easyrepl import REPL
from adhoc_api.tool import AdhocApi, APISpec

from bs4 import BeautifulSoup
import requests
from markdownify import markdownify


def main():    
    # set up the API spec for the JokeAPI
    gdc_api: APISpec = {
        'name': "JokesAPI",
        'description': 'JokeAPI is a REST API that serves uniformly and well formatted jokes.',
        'documentation': get_joke_api_documentation(),
    }

    # set up the tools and agent
    adhoc_api = AdhocApi(
        apis=[gdc_api],
        drafter_config={'provider': 'anthropic', 'model': 'claude-3-5-sonnet-latest'},
    )
    python = PythonTool()
    agent = ReActAgent(model='gpt-4o', tools=[adhoc_api, python], verbose=True)

    # REPL to interact with agent
    for query in REPL(history_file='.chat'):
        try:
            answer = agent.react(query)
            print(answer)
        except FailedTaskError as e:
            print(f"Error: {e}")


def get_joke_api_documentation() -> str:
    """Download the HTML of the joke API documentation page with soup and convert it to markdown."""
    url = 'https://sv443.net/jokeapi/v2/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    markdown = markdownify(str(soup))
    
    return markdown


if __name__ == "__main__":
    main()
```

Then you can run the script and interact with the agent in the REPL:

```
$ python example.py

>>> Can you tell me what apis are available?
The available API is JokesAPI, which is a REST API that serves uniformly and well formatted jokes.

>>> Can you fetch a safe joke?
Here is a safe joke from the JokesAPI:

Category: Pun
Type: Two-part
Setup: What kind of doctor is Dr. Pepper?
Delivery: He's a fizzician.
```

## Library Interface

### AdhocApi
Instances of this tool are created via the `AdhocApi` class

```python
from adhoc_api.tool import AdhocApi

tool = AdhocApi(
    apis =           # list[APISpec]: list of the APIs this tool can access
    drafter_config = # DrafterConfig | list[DrafterConfig]: LLM model(s) to use
    logger =         # (optional) Logger: logger instance
)
```

> Note: If multiple `DrafterConfig`'s are provided in a list, the tool selects (per each API) the first model with a large enough context window.

### DrafterConfig
Specify which LLM model to use for drafting code. The config is simply a dictionary with the following fields:

```python
from adhoc_api.tool import DrafterConfig, GeminiConfig, GPTConfig, ClaudeConfig

# DrafterConfig is just an alias for GeminiConfig | GPTConfig | ClaudeConfig
drafter_config: DrafterConfig = {
    'provider': # 'openai' | 'google' | 'anthropic'
    'model':    # str: name of the model
    'api_key':  # (optional) str: manually set the API key here
}
```


Currently support the following providers and models:
- openai
    - gpt-4o
    - gpt-4o-mini
    - o1
    - o1-preview
    - o1-mini
    - gpt-4
    - gpt-4-turbo
- google
    - gemini-1.5-flash-001
    - gemini-1.5-pro-001
- anthropic
    - claude-3-5-sonnet-latest
    - claude-3-5-haiku-latest

Additionally depending on the provider, there might be extra fields supported in the `DrafterConfig`. For example gemini models support `ttl_seconds` for specifying how long content is cached for. See the full type definitions of `GeminiConfig`, `GPTConfig`, and `ClaudeConfig` in [adhoc_api/tool.py](adhoc_api/tool.py)

Some examples of commonly used configs:
```
{'provider': 'openai', 'model': 'gpt-4o'}
{'provider': 'anthropic', 'model': 'claude-3-5-sonnet-latest'}
{'provider': 'google', 'model': 'gemini-1.5-pro-001'}
{'provider': 'google', 'model': 'gemini-1.5-flash-001', 'ttl_seconds': 1800},
```

### APISpec
Dictionary interface for representing an API

```python
from adhoc_api.tool import APISpec

spec: APISpec = {
    'name':           # str: Name of the API. This should be unique
    'description':    # str: A Description of the API
    'documentation':  # str: arbitrary documentation describing how to use the API
    'cache_key':      # (optional) str: (if possible) enable caching for this API
    'model_override': # (optional) DrafterConfig: explicit model to use for this API
}
```

> Note: `description` is only seen by the archytas agent, not the drafter. Any content meant for the drafter should be provided in `documentation`.

### Automatically Selecting the Best model for each API
Ad-Hoc API supports automatically selecting the best model to use with a given API. At the moment this only looks at the length of the API documentation in tokens compared to the model context window size.

To use automatic selection, simply provide multiple `DrafterConfig`'s in a list when instantiating `AdhocApi`. For each API, the first suitable model in the list will be selected. If no models are suitable, an error will be raised (at `AdhocApi` instantiation time).

```python
from adhoc_api.tool import AdhocApi

tool = AdhocApi(apis = [...],
    drafter_config = [
        # better model but with smaller context window
        {'provider': 'anthropic', 'model': 'claude-3-5-sonnet-latest'},
        # worse model but supports largest context window
        {'provider': 'google', 'model': 'gemini-1.5-pro-001'}
    ]
)
```

### Using different models per API
In an `APISpec` you can explicitly indicate which model to use by specifying a `model_override`. This will ignore any model(s) specified when the `AdhocApi` instance was created.

```python
from adhoc_api.tool import APISpec, AdhocApi

# Only use GPT-4o for this API. Ignore any other models specified
gpt_spec: APISpec = {'name': ..., 'description': ..., 'documentation': ...,
    'model_override': {'openai', 'gpt-4o'}
}

# a bunch of other APIs that will use gemini as default
other_specs: list[APISpec] = [...]

tool = AdhocApi(
    apis=[gpt_spec, *other_specs],
    drafter_config={'provider': 'google', 'model': 'gemini-1.5-pro-001'}
)
```

### Loading APIs from YAML
For convenience, Ad-Hoc API supports loading `APISpec` dictionaries directly from yaml files. To use, your yaml file must include all required fields from the `APISpec` type definition, namely `name`, `description`, and `documentation`. You may include the optional fields as well i.e. `cache_key`, and `model_override`.

```yaml
name: "Name of this API"
description: "Description of this API"
documentation: |
    all of the documentation 
    for this API, contained
    in a single string
# [optional fields]
# cache_key: ...
# model_override:
#    provider: ...
#    model: ...
```

yaml `APISpec`'s may be loaded via the following convenience function

```python
from adhoc_api.loader import load_yaml_api
from pathlib import Path

yaml_path = Path('location/of/the/api.yaml')
spec = load_yaml_api(yaml_path)
```

For convenience the yaml loader supports loading text content from arbitrary files via the `!load` tag, and string interpolation from fields in the yaml via `{name_of_field}` syntax.

```yaml
name: Name of this API
description: This is {name}. It allows you to ...
documentation: |
    # API Documentation
    {raw_documentation}


    # Usage Instructions
    some instructions on how to use this API
    etc.
    etc.

    ## Facets
    when using this API, ensure any enums/values are drawn from this list of facets:
    {facets}


    # Usage Examples
    {examples}
raw_documentation: !load documentation.md
facets: !load facets.txt
examples: !load examples.md
```

> Note: any extra fields not in `APISpec` are ignored, and are purely for convenience of constructing and pulling content into the yaml.

### Setting API Keys
The preferred method of using API keys is to set them as an environment variable:
- OPENAI_API_KEY
- ANTHROPIC_API_KEY
- GEMINI_API_KEY

Alternatively you can pass the key in as part of the `DrafterConfig` via the `api_key` field as seen above.

### Caching
At present, prompt caching is supported by Gemini and Claude. Caching is done on a per API basis (because each API has different content that gets cached). To use caching, you must specify in the `APISpec` dict a unique `cache_key` (unique per all APIs in the system).

By default, gemini content is cached for 30 minutes after which the cache will be recreated if more messages are sent to the agent. You can override this amount by specifying an integer for `ttl_seconds` in the `DrafterConfig`.

Claude caches content for 5 minutes and content is refreshed every time it is used. Currently there is no option for caching for longer--Instead Claude's caching is largely handled under the hood when Anthropic determines caching is possible

OpenAI models currently do not support caching in this library.
