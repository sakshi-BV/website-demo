from odoo import models, fields, api

class Employee(models.Model):
    _name = 'employee.model'
    _description = 'here we have data related employee'

    emp_name = fields.Char(string='Employee Name')
    phone_number = fields.Integer(string='Phone Number')
    emp_img = fields.Boolean(string = 'Employee Image')
    city = fields.Char(string='City')
    work_experience= fields.Integer(string='Work Experience')



