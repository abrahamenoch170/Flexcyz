# Simple in-memory storage for agent context
MEMORY = {}

def save(key, value):
    MEMORY[key] = value

def load(key):
    return MEMORY.get(key, None)
