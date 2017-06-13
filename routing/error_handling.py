@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.errorhandler(403)
def forbidden(error):
    return 'This content is forbidden', 403

@app.errorhandler(400)
def bad_request(error)
    return 'Bad request', 400
