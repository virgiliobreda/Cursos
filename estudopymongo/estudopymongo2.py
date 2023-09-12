import pymongo as pyM
import pprint

client = pyM.MongoClient("mongodb+srv://mongo:L8XqWMeX58ZfitCA@cluster0.eknywcw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

collection = db.bank_collection
posts = db.posts

# Recuperando documento por nome
print('\nRecuperando documento por nome')
pprint.pprint(db.posts.find_one({'nome':'paula'}))

# Recuperando documentos por agência
print('\nRecuperando documentos por agência')
for conta in posts.find({'agencia': '0001'}):
    print(conta)


# Contagem de documentos
print('\nContagem de documentos no banco de dados')
print(posts.count_documents({}))