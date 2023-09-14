# -*- coding: utf-8 -*-
from odoo import http


class WebsiteDemo(http.Controller):
    @http.route('/website_demo/website_demo', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/website_demo/website_demo/objects', auth='public')
    def list(self, **kw):
        return http.request.render('website_demo.listing', {
            'root': '/website_demo/website_demo',
            'objects': http.request.env['website_demo.website_demo'].search([]),
        })

    @http.route('/website_demo/website_demo/objects/<model("website_demo.website_demo"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('website_demo.object', {
            'object': obj
        })
    

    @http.route(['/dynamic/employee/info'], auth="public")
    def sold_total(self):
       employee_details = http.request.env['employee.model'].search_read([],['employee_name'])
       return employee_details


  