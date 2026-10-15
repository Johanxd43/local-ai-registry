# New recipe for RTX 4060 Ti 16 GB
{
    "hardware_id": "rtx-4060-ti-16gb",
    "model": "Qwen3.8-27B",
    "engine": "vllm",
    "docker_image": "ghcr.io/0xsero/vllm-openai@sha256:d9743fccd4a9b8dd7f8fa18945ce6e5026f00dcab50b0727edd51690b88d4f32",
    "docker_command": [
        "--model", "Qwen3.8-27B",
        "--tensor-parallel-size", "1",
        "--max-num-batched-tokens", "128000",
        "--max-num-seqs", "128",
        "--max-model-len", "128000",
        "--gpu-memory-utilization", "0.95"
    ],
    "validation_checks": [
        {
            "name": "loads",
            "command": ["curl", "-X", "GET", "localhost:8000/v1/models"],
            "expected_output": "Qwen3.8-27B"
        },
        {
            "name": "answers",
            "command": ["curl", "-X", "POST", "localhost:8000/v1/chat/completions", "-d", "{\"messages\": [{\"role\": \"user\", \"content\": \"What is the capital of France?\"}]}"],
            "expected_output": "Paris"
        },
        {
            "name": "thinks",
            "command": ["curl", "-X", "POST", "localhost:8000/v1/chat/completions", "-d", "{\"messages\": [{\"role\": \"user\", \"content\": \"Explain the theory of relativity.\"}]}"],
            "expected_output": "exist"
        },
        {
            "name": "calls a tool",
            "command": ["curl", "-X", "POST", "localhost:8000/v1/chat/completions", "-d", "{\"messages\": [{\"role\": \"user\", \"content\": \"Calculate 2+2.\"}]}"],
            "expected_output": "4"
        },
        {
            "name": "recalls at a nearly full window",
            "command": ["curl", "-X", "POST", "localhost:8000/v1/chat/completions", "-d", "{\"messages\": [{\"role\": \"user\", \"content\": \"Recall the first paragraph of this conversation.\"}]}"],
            "expected_output": "exist"
        },
        {
            "name": "15 tok/s or more",
            "command": ["curl", "-X", "POST", "localhost:8000/v1/chat/completions", "-d", "{\"messages\": [{\"role\": \"user\", \"content\": \"Generate a random paragraph.\"}], \"temperature\": 1}"],
            "expected_output": "exist",
            "expectation": "tok/s >= 15"
        }
    ]
}