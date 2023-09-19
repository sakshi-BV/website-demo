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
    
    # @http.route('/employee/data', auth='public', type='json', method=['POST'])
    # def form_data(self, **kw):
    #     user = http.request.env.user
    #     if user and user.id != http.request.website.user_id.id:
    #         http.request.env['employee.model'].create([kw])
    #         return {'success': True}
    #     else:
    #         return {'error': 'You must be logged in to submit the data'}