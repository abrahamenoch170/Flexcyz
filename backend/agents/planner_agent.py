from worker_agent import run_worker
from memory.memory_store import save, load

def plan_task(task: str):
    # naive split by periods for multi-step demonstration
    subtasks = [s.strip() for s in task.split(".") if s.strip()]
    results = []

    for i, subtask in enumerate(subtasks):
        result = run_worker(subtask)
        results.append(result)
        save(f"subtask_{i}", result)

    return results
