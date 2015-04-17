import web, os
from db import data_purchase

urls = (
    '/', 'Home')

web.config.debug = False
web.template.Template.globals['root_path'] = lambda p: web.ctx.homedomain + p

class Home:


    def GET(self):    
        render = web.template.render('statics')
        data = data_purchase.select_table()
        return render.home(data, 0)

        
    def POST(self):    
        render = web.template.render('statics')
        x = web.input(myfile={})
        cur_dir = os.path.abspath(os.path.dirname(__file__))
        data = []

        if 'myfile' in x: 

            filename = os.path.basename(x.myfile.filename)
            upload_dir = os.path.join(cur_dir,'upload_files',filename)
            fout = open(upload_dir,'wb')
            fout.write(x.myfile.file.read())
            fout.close()
            end_file =  open(upload_dir,'r').readlines()[1:]
            total = 0
            for line in end_file:
                list_purchase = {}
                f = line.split('\t')
                list_purchase["purchaser_name"] = f[0]
                list_purchase["item_desc"] = f[1]
                list_purchase["item_price"] = f[2]
                list_purchase["purchase_count"] = f[3]
                list_purchase["merchant_address"] = f[4]
                list_purchase["merchant_name"] = f[5].replace('\n','')
                data.append(list_purchase)
                total += float(list_purchase["item_price"])* float(list_purchase["purchase_count"])
            
            data_purchase.insert_table(data)
            data = data_purchase.select_table()
          
            
        return  render.home(data, total)

if __name__ == "__main__":  
    app = web.application(urls, globals())
    
    app.run()
    
