"""
This Module contains routes for error redirects.

Functions
    page_not_found: Redirects to a 404 Page Not Found.
    bad_request: Redirects to a 400 Bad Request.
"""

from . import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(error):
    """Function to render a 404 error page."""
    return render_template('./exceptions/404_not_found.html', error=error), 404


@app.errorhandler(400)
def bad_request(error):
    """Function to render a 400 error page."""
    return render_template('./exceptions/400_bad_request.html', error=error), 400
