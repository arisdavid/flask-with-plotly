from flask import (Blueprint,
                   redirect,
                   url_for)


page = Blueprint('pages', __name__, template_folder='templates')


@page.route("/")
def index():
    """
    Index / Main page
    :return: html
    """

    return redirect(url_for('charts.bar_chart'))
