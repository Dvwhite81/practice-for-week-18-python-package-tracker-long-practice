from flask import Blueprint, redirect, render_template, url_for
from app.forms.shipping_form import ShippingForm

bp = Blueprint('packages', __name__, url_prefix='')


@bp.route('/')
def index():
    return 'Package Tracker'



@bp.route('/new-package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))

    return render_template('shipping_request.html', form=form)
