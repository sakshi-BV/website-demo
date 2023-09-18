from odoo import http

class FormController(http.Controller):
    @http.route('/employee/form', auth='public', website = True)
    def index(self):
        return http.request.render('website_demo.employee_template')
  
    @http.route('/employee/data', auth='user', type='json',method=['POST'])
    def form_data(self, **kw):
        print(kw)
        http.request.env['employee.model'].create([kw])
        return True