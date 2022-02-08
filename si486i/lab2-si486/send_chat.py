from blockchain_utilities import http_get, http_post, build_block
if __name__ == "__main__":
    url = 'http://cat:5000'

    # Get user message
    message = input("message: ")

    # Get the head blocks hash
    request_url = url+'/head'
    head_hash = http_get(request_url).content

    # Build a new block and send it to the blockchain
    json_encoded_block = build_block(head_hash.decode(),{'chat' : message},0)
    push_data = {'block' : json_encoded_block}
    post = http_post(url+'/push',push_data)
    print(post.status_code)
