import hashlib

class dataBlock:

    def __init__(self, previous_block_hash, transaction_list):
        
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = " | ".join(transaction_list) + " | " + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t_list1 = "Dan send 1 BTC to Ped"
t_list2 = "Ped send 10 BTC to Film"
t_list3 = "Elon send 100 BTC to Wan"
t_list4 = "Wan send 1 USDT to Elon"

first_block = dataBlock("First Block",[t_list1,t_list2])
second_block = dataBlock(first_block.block_hash,[t_list3,t_list4])
third_block = dataBlock(second_block.block_hash,[t_list3,t_list4])

print(third_block.block_data)
print(third_block.block_hash)

#print(hashlib.sha256('1234'.encode()).hexdigest())