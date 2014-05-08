#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import web
from controller import SinaController
render = web.template.render('templates/',base='layout')
# render_without_layout = web.template.render('templates/')
urls = (
    '/sina',SinaController.app,
    '/friends/', 'friend',
    '/userinfo/','userinfo',
    '/','home'
)

class friend:
    def GET(self):
        return render.friends()

class home:
	def GET(self):
		return render.home()

class userinfo:
    def GET(self):
        return render.userinfo()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()