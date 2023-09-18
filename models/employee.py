from odoo import models, fields, api

class Employee(models.Model):
    _name = 'employee.model'
    _description = 'here we have data related employee'

    emp_name = fields.Char(string='Employee Name')
    phone_number = fields.Char(string='Phone Number')
    emp_img = fields.Binary(string = 'Employee Image')
    city = fields.Char(string='City')
    work_experience= fields.Char(string='Work Experience')



