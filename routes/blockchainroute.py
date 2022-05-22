from zipfile import ZipFile
from fastapi import APIRouter, Form
from fastapi.templating import Jinja2Templates
from blockchain import Blockchain
import shutil
from fastapi.responses import FileResponse

block=APIRouter()
blockchain = Blockchain()

@block.post('/create_block/{id}')
def create(id:str, name:str=Form(...)):
	previous_block = blockchain.print_previous_block()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	block = blockchain.create_block(proof, previous_hash, id, owner=name)
	
	response = {'message': 'A block is MINED',
				'index': block['index'],
				'timestamp': block['timestamp'],
				'proof': block['proof'],
                'owner': block['owner'],
				'key': block['image'],
				'imagename': block['imageurl'],
				'previous_hash': block['previous_hash']}
	
	shutil.move('./html/images/'+id,'./bought/boughtimages/'+id)

	f=open('./bought/key/block.txt','w')
	f.write(str(response))
	f=open('./bought/key/filekey.txt','w')
	f.write(block['image'])

	zipObj = ZipFile('image.zip', 'w')
	zipObj.write('./bought/boughtimages/'+id)
	# zipObj.write('./bought/key/filekey.txt')
	zipObj.write('./bought/key/block.txt')

	# zipObj.write('test_2.log')

	return FileResponse('image.zip', media_type='application/octet-stream', filename='image.zip')

@block.get('/get_chain')
def display_chain():
	response = {'chain': blockchain.chain,
				'length': len(blockchain.chain)}
	
	f = open('chains/chain.txt','w')
	f.write(str(response))
	
	f = open('chains/chaincopy1.txt','w')
	f.write(str(response))

	f = open('chains/chaincopy2.txt','w')
	f.write(str(response))

	f = open('chains/chaincopy3.txt','w')
	f.write(str(response))

	return response

@block.get('/valid')
def valid():
	valid = blockchain.chain_valid(blockchain.chain)
	
	if valid:
		response = {'message': 'The Blockchain is valid.'}
	else:
		response = {'message': 'The Blockchain is not valid.'}
	return response
