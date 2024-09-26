import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\thoma\Desktop\Fall 2024\CSE-310\learning-model-443a0-firebase-adminsdk-4u4u2-729aa673f9.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def Add_Blog_Post(title, author, content):
    doc_ref = db.collection('posts').add({
        'title': title,
        'author': author,
        'content': content
    })
    print(f'Added blog post with ID: {doc_ref.id}')

if __name__ == '__main__':
    Add_Blog_Post('Dogs','Thomas','Dogs are cool!')
