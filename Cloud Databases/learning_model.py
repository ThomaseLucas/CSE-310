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

def Read_Blog_Post(post_id):
    doc_ref = db.collection('posts').document(post_id)
    doc = doc_ref.get()
    if doc.exists:
        print(f'Blog post: {doc.to_doc()}')
    else:
        print('No such document')

def Update_Blog_Posts(post_id, new_content){
    doc_ref = db.collection('posts').document(post_id)
    doc_ref.update({
        'content': new_content
    })
    print(f'Updated blog post with ID: {post_id}')
}
if __name__ == '__main__':
    Add_Blog_Post('Dogs','Thomas','Dogs are cool!')
