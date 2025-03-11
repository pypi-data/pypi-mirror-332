from benchflow.agents.bird_openai import BridAgent
from benchflow import load_benchmark
import os

bench = load_benchmark(benchmark_name="benchflow/Bird", bf_token=os.getenv("BF_TOKEN"))

your_agents = BridAgent()

run_ids = bench.run(
    task_ids=["all"],
    agents=your_agents,
    api={"provider": "openai", "model": "gpt-4o-mini", "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")},
    requirements_txt="bird_requirements.txt",
    args={}
)

results = bench.get_results(run_ids)
