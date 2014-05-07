#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import web
from controller import SinaController
render = web.template.render('templates/')
# render_without_layout = web.template.render('templates/')
urls = (
    '/api/sina',SinaController.app,
    '/chart/', 'chart'
)

class chart:
    def GET(self):
        return render.charts()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()