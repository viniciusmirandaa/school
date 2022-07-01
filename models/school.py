from odoo import fields, models, api
from datetime import datetime, date, timedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from odoo.tools.translate import _


class SchoolProfile(models.Model):
    _name = "school"
    name = fields.Char(string="School Name", copy=False, default="Sunny Leone")
    email = fields.Char(string="Email", copy=False)
    phone = fields.Char("Phone", copy=False)
    is_virtual_class = fields.Boolean(string="Virtual Class Support?")
    school_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    estalish_date = fields.Date(string="Establish Date")
    open_date = fields.Datetime("Open Date")
    currency_id = fields.Many2one("res.currency", string="Currency")
    school_type = fields.Selection([('public', 'Public School'), ('private', 'Private School')],
                                   string="Type of School", )
    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File Name")
    school_image = fields.Image(string="Upload School Image", max_width=100, max_height=100)
    school_description = fields.Html(string="Description", copy=False)

