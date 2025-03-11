import os

from benchflow import load_benchmark
from benchflow.agents.webcanvas_openai import WebcanvasAgent


def test_webcanvas_benchmark():
    bench = load_benchmark(benchmark_name="benchflow/Webcanvas", bf_token=os.getenv("BF_TOKEN"))

    your_agents = WebcanvasAgent()

    args = {
    "BROWSERBASE_API_KEY": os.environ.get("BROWSERBASE_API_KEY"),
    "GRAPHQL_USERNAME": os.environ.get("GRAPHQL_USERNAME"), 
    "GRAPHQL_PASSWORD": os.environ.get("GRAPHQL_PASSWORD"),
    "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY")
    }

    run_ids = bench.run(
        task_ids=[1],
        agents=your_agents,
        requirements_txt = "webcanvas_requirements.txt",
        api={"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")},
        args=args
    )

    results = bench.get_results(run_ids)

    assert results is not None

if __name__ == "__main__":
    test_webcanvas_benchmark()
