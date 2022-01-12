import datetime
import json
import hashlib
from flask import Flask , jsonify
from flask.helpers import make_response
class Blockchain:
    def __init__(self):
        #เก็บกลุ่มของ Block
        self.chain = [] #list ที่่เก็บ block
        #genesis block
        self.create_block(nonce=1,previous_hash="0")
        self.create_block(nonce=10,previous_hash="00")
        self.create_block(nonce=20,previous_hash="000")


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

    #ให้บริการเกี่ยวกับ Block ก่อนหน้า
    def get_previous_block(self):
        return self.chain[-1]

    #เข้ารหัส Block
    def hash(self,block):
        #แปลง python object (dict) => json object
        encode_block = json.dumps(block,sort_keys=True).encode()
        #sha-256
        return hashlib.sha256(encode_block).hexdigest()

    def proof_of_work(self,previous_nonce):
        #อยากได้ค่า nonce = ? ที่ส่งผลให้ได้ target hash => 4 หลักแรก => 0000xxxxxxxxxxxx
        new_nonce = 1 #ค่า nonce ที่ต้องการ
        check_proof = False #ตัวแปรที่เช็คค่า nonce ให้ได้ตาม target ที่กำหนด

        #แก้โจทย์ทางคณิตศาสตร์
        while check_proof is False:
            #เลขฐาน 16 มา 1 ชุด
            hashoperation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hashoperation[:4] == "0000":
                check_proof = True
            else:
                new_nonce+=1
        return new_nonce

#web server
app = Flask(__name__)

#routing
@app.route('/')
def hello():
    return "<p>Hello Blockchain</p>"

@app.route('/get_chain',methods=["GET"])
def get_chain():
    response = make_response(
        jsonify(
            {"chain":blockchain.chain, "length":len(blockchain.chain)}
        ),200
    )
    response.headers["Content-Type"] = "application/json"
    return response

#run server
if __name__ == "__main__":
    app.run()

#ใช้งาน Blockchain
blockchain = Blockchain()
