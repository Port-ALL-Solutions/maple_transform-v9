# -*- coding: utf-8 -*-
from openerp import http

# class Mapletransform(http.Controller):
#     @http.route('/mapletransform/mapletransform/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mapletransform/mapletransform/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mapletransform.listing', {
#             'root': '/mapletransform/mapletransform',
#             'objects': http.request.env['mapletransform.mapletransform'].search([]),
#         })

#     @http.route('/mapletransform/mapletransform/objects/<model("mapletransform.mapletransform"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mapletransform.object', {
#             'object': obj
#         })