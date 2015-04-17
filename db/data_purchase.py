import sqlite3


def select_table():
    conn = sqlite3.connect('db\desafio.s3db')
    c = conn.cursor()  
         
    sql = ('''select * from tb_purchase''')
      
    c.execute(sql)
    rs = c.fetchall()
    

    conn.commit()
        
    conn.close()   
    
    return rs
    
    


def insert_table( data ):
    conn = sqlite3.connect('db\desafio.s3db')
    c = conn.cursor()  
    for item in data:
        
        sql = ('''INSERT INTO tb_purchase''' \
        '''(purchaser_name,item_desc,item_price,purchase_count,merchant_address,merchant_name)'''\
        '''VALUES ("%s","%s",%s,%s,"%s","%s")''')\
        %(item["purchaser_name"],item["item_desc"],item["item_price"], \
          item["purchase_count"],item["merchant_address"],item["merchant_name"])
        rs = c.execute(sql)
   
        conn.commit()
        
    conn.close()           
            