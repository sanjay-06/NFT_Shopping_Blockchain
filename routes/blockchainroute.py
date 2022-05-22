from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from blockchain import Blockchain

block=APIRouter()
blockchain = Blockchain()

@block.get('/mine_block/{id}')
def mine_block(id: str):
	previous_block = blockchain.print_previous_block()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	block = blockchain.create_block(proof, previous_hash, id, owner= "name")
	
	response = {'message': 'A block is MINED',
				'index': block['index'],
				'timestamp': block['timestamp'],
				'proof': block['proof'],
                'owner': block['owner'],
				'z_image': block['image'],
				'previous_hash': block['previous_hash']}
	
	return response

@block.get('/get_chain')
def display_chain():
	response = {'chain': blockchain.chain,
				'length': len(blockchain.chain)}
	return response

@block.get('/valid')
def valid():
	valid = blockchain.chain_valid(blockchain.chain)
	
	if valid:
		response = {'message': 'The Blockchain is valid.'}
	else:
		response = {'message': 'The Blockchain is not valid.'}
	return response
