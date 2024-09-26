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
    print(f'Added blog post with ID: {doc_ref[1].id}')
    return doc_ref[1].id

def Read_Blog_Post(post_id):
    doc_ref = db.collection('posts').document(post_id)
    doc = doc_ref.get()
    if doc.exists:
        print(f'Blog Post: {doc.to_dict()}')
    else:
        print('No such document!')


def Update_Blog_Posts(post_id, new_content):
    doc_ref = db.collection('posts').document(post_id)
    doc_ref.update({
        'content': new_content
    })
    print(f'Updated blog post with ID: {post_id}')

def Delete_Blog_Post(post_id):
    doc_ref = db.collection('posts').document(post_id)
    doc_ref.delete()
    print(f'Deleted blog post with ID: {post_id}')

def Main_Menu():
    user_input = None
    while user_input != 0:
        print('1. Create blog post')
        print('2. Read blog post')
        print('3. Update blog post')
        print('4. Delete blog post')
        print('0. Exit program')

        user_input = input('Please enter your selection: ')

        if user_input == 1:
            
            blog_title = input('Enter the title of your blog post: ')
            blog_author = input('Enter the author of your blog post: ')
            blog_content = input('Enter the content of your blog post: ')
            
            doc_id = Add_Blog_Post(blog_title, blog_author, blog_content)

            print(f'Your document was created with the ID: {doc_id}')
            Read_Blog_Post(doc_id)
        else:
            return


if __name__ == '__main__':
    Main_Menu()
