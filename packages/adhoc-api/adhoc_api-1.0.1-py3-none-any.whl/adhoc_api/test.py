from .uaii import ClaudeAgent, OpenAIAgent, UAII
from .tool import AdhocApi, APISpec, DrafterConfig


from easyrepl import REPL
test_api: APISpec = {
    'name': 'test',
    'description': 'test',
    'documentation': '',
}


def instantiate_apis():
    drafter_config: DrafterConfig = {'provider': 'anthropic', 'model': 'claude-3-7-sonnet-latest'}
    drafter_config: DrafterConfig = {'provider': 'openai', 'model': 'o3-mini'}
    drafter_config: DrafterConfig = {'provider': 'openai', 'model': 'o1-mini'}
    drafter_config: DrafterConfig = {'provider': 'openai', 'model': 'o1'}

    api = AdhocApi(apis=[test_api], drafter_config=drafter_config)


def test_claude_37():
    agent = ClaudeAgent(model='claude-3-7-sonnet-latest', system_prompt='You are a helpful assistant.')
    repl_loop(agent)


def test_openai():
    agent = OpenAIAgent(model='gpt-4o', system_prompt=None)
    repl_loop(agent)


def repl_loop(agent:UAII):
    for query in REPL(history_file='.chat'):
        res = agent.message(query, stream=True)
        for i in res:
            print(i, end='', flush=True)
        print()


if __name__ == '__main__':
    # test_claude_37()
    test_openai()
    # instantiate_apis()