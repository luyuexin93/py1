import web

urls = (
    '/hello','Index')
app = web.application(urls,globals())
render = web.template.render('C:/Python27/workplace/myweb/gothonweb/templates/',base="layout")



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