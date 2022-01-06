import datetime
class Blockchain:
    def __init__(self):
        #เก็บกลุ่มของ Block
        self.chain = [] #list ที่่เก็บ block
        #genesis block
        self.create_block(nonce=1,previous_hash="0")

    #สร้าง Block ขึ้นมาในระบบ Blockchain
    def create_block(self,nonce,previous_hash):
        #เก็บส่วนประกอบของ Block แต่ละ Block
        block = {
            "index":len(self.chain)+1,
            "timestamp":str(datetime.datetime.now()),
            "nonce":nonce,
            "previous_hash":previous_hash
        }
        self.chain.append(block)
        return block

#ใช้งาน Blockchain
blockchain = Blockchain()
print(blockchain.chain)