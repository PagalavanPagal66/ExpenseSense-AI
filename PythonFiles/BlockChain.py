import hashlib
import json
from typing import List, Any

class Block:
    def __init__(self, index: int, data: Any, previous_hash: str):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = json.dumps({
            'index': self.index,
            'data': self.data,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, data={self.data}, hash={self.hash[:10]}..., prev_hash={self.previous_hash[:10]}...)"


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data: Any):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(block)

    def verify_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Check if current block's hash is valid
            if current.hash != current.compute_hash():
                print(f"Block {i} has been tampered with: invalid hash!")
                return False

            # Check if previous_hash is correct
            if current.previous_hash != previous.hash:
                print(f"Block {i} has invalid previous hash link!")
                return False

        print("Blockchain is valid.")
        return True
