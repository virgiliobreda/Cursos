import pymongo as pyM



client = pyM.MongoClient("mongodb+srv://mongo:L8XqWMeX58ZfitCA@cluster0.eknywcw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

collection = db.bank_collection
print(db.list_collection_names()) 

new_post = [{
    'nome': 'paula',
    'cpf': '111111111',
    'endereco': 'rua... numero... bairro... cidade... estado...',
    'tipo': 'corrente',
    'agencia': '0001',
    'num': '0001',
    'saldo': 309
},
{
    'nome': 'joao',
    'cpf': '222222222',
    'endereco': 'rua... numero... bairro... cidade... estado...',
    'tipo': 'poupanca',
    'agencia': '0001',
    'num': '0002',
    'saldo': 3900,
},
{
    'nome': 'dolly',
    'cpf': '333333333',
    'endereco': 'rua... numero... bairro... cidade... estado...',
    'tipo': 'poupanca',
    'agencia': '0001',
    'num': '0003',
    'saldo': 10000,
}
]
posts = db.posts
posts_id = posts.insert_many(new_post).inserted_ids