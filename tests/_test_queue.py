from simple_gpu_queue.simple_gpu_queue import GPUQueueClient
queue = GPUQueueClient(git_commit_id="most_recent")

# Send commands as a list of (command, stdout_file) tuples. Stdoutfile can be "" for no saving of stdout logging.
commands = [
    ("python -c 'import time; import jax.numpy as jnp; a=jnp.ones(5); time.sleep(1); print(\"I SLEPT HAPPY 1\")'", "testlogs/v1.txt"),
    ("python -c 'import time; import jax.numpy as jnp; a=jnp.ones(5); time.sleep(2); print(\"I SLEPT HAPPY 2\")'", ""),
    ("python -c 'import time; import jax.numpy as jnp; a=jnp.ones(5); time.sleep(3); print(\"I SLEPT HAPPY 3\")'", "testlogs/v3.txt"),
]

if queue.git_repo.is_dirty():
    user_input = input("Repo has uncommitted changes: continue? [Y/n] ").strip().lower()
    if user_input == 'n':
        raise ValueError("Aborting due to uncommitted changes in the repository.") 

queue.send_command_list(commands)