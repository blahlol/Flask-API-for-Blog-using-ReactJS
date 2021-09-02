from flask import Blueprint, request
from flask import jsonify

blog_bp = Blueprint('blog', __name__, url_prefix = '/blogs')

blogs = [{
    'id': 1,
    'title': 'Breaking Bad',
    'author': 'Walter White',
    'body': 'Walter White, a chemistry teacher, discovers that he has cancer and decides to get into the meth-making business to repay his medical debts. His priorities begin to change when he partners with Jesse.' 
}]

@blog_bp.route('/')
def get_blogs():
    return jsonify(blogs)

@blog_bp.route('/', methods = ['POST'])
def create_blog():
    request_data = request.get_json()
    new_blog = {'id' : len(blogs) + 1, 'title': request_data['title'], 'author': request_data['author'], 'body': request_data['body']}
    blogs.append(new_blog)
    return new_blog
    
@blog_bp.route('/<int:id>')
def get_blog(id):
    for blog in blogs:
        if blog['id'] == id:
            return blog
    return 'Not found'

@blog_bp.route('/<int:id>', methods = ['DELETE'])
def delete_blog(id):
    for blog in blogs:
        if blog['id'] == id:
            blogs.remove(blog)
    return {'message': f'Deleted blog with ID {id}'}