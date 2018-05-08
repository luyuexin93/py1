import web
from gothonweb import map

urls = (
    '/hello','Index')
app = web.application(urls,globals())
render = web.template.render('C:/Python27/workplace/myweb/gothonweb/templates/',base="layout")


# little hack so that debug mode works with sessions
if web.config.get('_session')is None:
    store=web.session.DiskStore('sessions')
    store=web.session.DBStore()
    session=web.session.Session(app,store)




class Index(object):
    def GET(self):
        return render.hello_form()
    
    
    def POST(self):
        form = web.input(name="Nobody",greet="Hello")
        #if form.greet:
        greeting = " %s,%s" % (form.greet,form.name)
        return render.index(greeting = greeting)
        #else:
        #return "ERROR:greet is required."


if __name__ == "__main__" :
    app.run() 