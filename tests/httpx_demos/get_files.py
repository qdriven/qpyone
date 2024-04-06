
import httpx
def test_get_html_files():

    url = "https://github.com/a16z-infra/llm-app-stack/edit/main/README.md"
    response = httpx.get(url=url)
    print(response.text)
