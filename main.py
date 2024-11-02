import requests
import json
import time
from datetime import datetime
import pandas as pd
import traceback

Total_items_name=[]
Item_sku=[]
Item_images=[]
Item_prices=[]
Item_prices_max=[]
Item_description=[]
item_url=[]

headers = {
    'Content-Type': 'application/json',
    'Cookie': ''
} 

payload = {
}



def Api_call(base_url,headers,payload):
    response = requests.get(base_url,headers=headers, json=payload)
    time.sleep(0.1)
    if response.status_code == 200:  
        results= response.json().get("response").get("results")        
        for items in results:
            Total_items_name.append(items.get("data").get("title"))
            Item_sku.append(items.get("data").get("leaderSku"))
            Item_images.append(items.get("data").get("image_url"))
            Item_prices.append(items.get("data").get("lowestPrice"))
            Item_prices_max.append(items.get("data").get("highestPrice"))
            Item_description.append(items.get("data").get("description"))
            item_url.append(items.get("data").get("url"))
                            
    
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    try:
        Run = 0  
        while Run != 188:
            item_offset = 20 * Run  
            base_url = f"https://ac.cnstrc.com/browse/group_id/all-living-room?c=ciojs-client-2.49.2&key=key_w3v8XC1kGR9REv46&i=7a92d14a-ad10-4bed-bc18-942ad01f5b8a&s=2&offset={item_offset}&num_results_per_page=20&sort_order=descending&fmt_options%5Bhidden_facets%5D=smartDeskFeatures&_dt=1730167263526" 
            Api_call(base_url, headers, payload)
            Run += 1  
            time.sleep(0.5)  
            print((Run)*20)
        
        data = {
                'SKU': Item_sku,
                'Item': Total_items_name,
                'Image url': Item_images,
                'Min Price': Item_prices,
                'Max Price': Item_prices_max,
                'Description': Item_description,                
                'URL': item_url,
            }
        df = pd.DataFrame(data)


        excel_file = 'E-Commerce.xlsx'
        df.to_excel(excel_file, index=False)
    except Exception as e:
        print(f"Error in request: {str(e)}")            
        traceback.print_exc()

