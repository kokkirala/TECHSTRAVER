import hashlib
import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data):
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    @staticmethod
    def create_genesis_block():
        return Block(0, "0", datetime.datetime.now(), "Genesis Block", "0")

    @staticmethod
    def create_new_block(previous_block, data):
        index = previous_block.index + 1
        timestamp = datetime.datetime.now()
        previous_hash = previous_block.hash
        hash = Block.calculate_hash(index, previous_hash, timestamp, data)
        return Block(index, previous_hash, timestamp, data, hash)

class Blockchain:
    def __init__(self):
        self.chain = [Block.create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block.create_new_block(latest_block, data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != Block.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)
            print("\n")


supply_chain = Blockchain()


supply_chain.add_block("Step 1: Supplier sent the raw materials.")
supply_chain.add_block("Step 2: Manufacturing started with raw materials.")
supply_chain.add_block("Step 3: Quality check completed.")
supply_chain.add_block("Step 4: Product shipped to distributor.")
supply_chain.add_block("Step 5: Product received by retailer.")


supply_chain.display_chain()

print("Is blockchain valid?", supply_chain.is_chain_valid())