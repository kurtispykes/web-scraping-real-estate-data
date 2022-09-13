import json 

import scrapy 
from bradvisors.items import BradvisorsItem

class BradvisorsSpider(scrapy.Spider): 
    name = "bradvisors"
    start_urls = ["https://bradvisors.com/listings/"] 

    headers = {
    'authority': 'buildout.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://buildout.com',
    'pragma': 'no-cache',
    'referer': 'https://buildout.com/plugins/5339d012fdb9c122b1ab2f0ed59a55ac0327fd5f/bradvisors.com/inventory/?pluginId=0&iframe=true&embedded=true&cacheSearch=true&=undefined',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-newrelic-id': 'Vg4GU1RRGwIJUVJUAwY=',
    'x-requested-with': 'XMLHttpRequest'
    }
    
    def parse(self, response):
        url = "https://buildout.com/plugins/5339d012fdb9c122b1ab2f0ed59a55ac0327fd5f/inventory"
        
        for i in range(5):

            payload = f"utf8=%E2%9C%93&polygon_geojson=&lat_min=&lat_max=&lng_min=&lng_max=&mobile_lat_min=\
        &mobile_lat_max=&mobile_lng_min=&mobile_lng_max=&page={str(i)}&map_display_limit=500&map_type=roadmap\
            &custom_map_marker_url=%2F%2Fs3.amazonaws.com%2Fbuildout-production%2Fbrandings%2F7242%2Fprofile_photo\
                %2Fsmall.png%3F1607371909&use_marker_clusterer=true&placesAutoComplete=&q%5Btype_use_offset_eq_any%5D%5B%5D=\
                    &q%5Bsale_or_lease_eq%5D=&q%5Bbuilding_size_sf_gteq%5D=&q%5Bbuilding_size_sf_lteq%5D=&q%5B\
                        listings_data_max_space_available_on_market_gteq%5D=&q%5Blistings_data_min_space_available_on_market_lteq\
                            %5D=&q%5Bproperty_research_property_year_built_gteq%5D=&q%5Bproperty_research_property_year_built_lteq\
                                %5D=&q%5Bproperty_use_id_eq_any%5D%5B%5D=&q%5Bcompany_office_id_eq_any%5D%5B%5D=&q%5Bs%5D%5B%5D="
            
            yield scrapy.Request(method="POST", body=payload, url=url, headers=self.headers, callback=self.parse_api)

    def parse_api(self, response):
        data = json.loads(response.body)

        item = BradvisorsItem()

        for listing in data["inventory"]:
            item["address"] = listing["address_one_line"]
            item["city"] = listing["city"]
            item["city_state"] = listing["city_state"]
            item["zip"] = listing["zip"]
            item["description"] = listing["description"]
            item["size_summary"] = listing["size_summary"]
            item["item_url"] = listing["show_link"]
            item["property_sub_type_name"] = listing["property_sub_type_name"]
            item["sale"] = listing["sale"]
            item["sublease"] = listing["sublease"]
            yield item
