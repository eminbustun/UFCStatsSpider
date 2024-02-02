import scrapy
from ufcstat_scraper.items import FightItem 

class UfcstatScraper(scrapy.Spider):
    name = "ufcstat_scraper"
    start_urls = ["http://www.ufcstats.com/statistics/events/completed?page=all"]


    def parse(self, response):
        all_pages = response.css("tbody tr")
        list_of_all_events = all_pages.css("a.b-link_style_black::attr(href)").getall()
        for i in list_of_all_events:
            yield response.follow(i, callback=self.parse_event)
            
            

    def parse_event(self, response):
        fight_rows = response.css("tbody tr")
        for i in fight_rows:
            fight_item = FightItem()
            fight_item["event"] = response.css("span.b-content__title-highlight::text").get().strip()
            fight_item["date"] = response.css("ul.b-list__box-list li::text").getall()[1].strip()
            fight_item["location"] = response.css("ul.b-list__box-list li::text").getall()[3].strip()
            win_lose_or_draw = i.css("i.b-flag__text::text").get()
            fighterList = i.css("a.b-link_style_black::text").getall()
            fight_item["fighter1ID"] = i.css("a.b-link_style_black::attr(href)").getall()[0].split("/")[-1]
            fight_item["fighter2ID"] = i.css("a.b-link_style_black::attr(href)").getall()[1].split("/")[-1]

            fight_item["fighter1"] = fighterList[0].strip()
            fight_item["fighter2"] = fighterList[1].strip()

            
            if win_lose_or_draw == "win":     
                fight_item["win"] = fighterList[0].strip()
                fight_item["lose"] = fighterList[1].strip()

            
                
            elif win_lose_or_draw == "draw":
                fight_item["draw1"] = fighterList[0].strip()
                fight_item["draw2"] = fighterList[1].strip()
            
            
                
            elif win_lose_or_draw == "nc":
                fight_item["nc1"] = fighterList[0].strip()
                fight_item["nc2"] = fighterList[1].strip()
                
            
            fight_item["weight_class"] = i.css("p.b-fight-details__table-text::text").getall()[14].strip()
            method = i.css("p.b-fight-details__table-text::text").getall()[16].strip()
        
            if method == "U-DEC" or method == "S-DEC":
                fight_item["method"] = i.css("p.b-fight-details__table-text::text").getall()[16].strip()
                fight_item["endWith"] = "decision"
                fight_item["roundd"] = i.css("p.b-fight-details__table-text::text").getall()[18].strip()
                fight_item["time"] = i.css("p.b-fight-details__table-text::text").getall()[19].strip()

            elif i.css("p.b-fight-details__table-text::text").getall()[16].strip() == "SUB" or i.css("p.b-fight-details__table-text::text").getall()[16].strip() == "KO/TKO":
                fight_item["method"] = i.css("p.b-fight-details__table-text::text").getall()[16].strip()
                fight_item["endWith"] = i.css("p.b-fight-details__table-text::text").getall()[17].strip()
                fight_item["roundd"] = i.css("p.b-fight-details__table-text::text").getall()[18].strip()
                fight_item["time"] = i.css("p.b-fight-details__table-text::text").getall()[19].strip()

            elif i.css("p.b-fight-details__table-text::text").getall()[18].strip() == "CNC":
                fight_item["weight_class"] = i.css("p.b-fight-details__table-text::text").getall()[16].strip()
                fight_item["method"] = i.css("p.b-fight-details__table-text::text").getall()[18].strip()
                fight_item["endWith"] = "no contest"
                fight_item["roundd"] = i.css("p.b-fight-details__table-text::text").getall()[20].strip()
                fight_item["time"] = i.css("p.b-fight-details__table-text::text").getall()[21].strip()
                
            else:
                fight_item["method"] = i.css("p.b-fight-details__table-text::text").getall()[17].strip()
                fight_item["endWith"] = i.css("p.b-fight-details__table-text::text").getall()[18].strip()
                fight_item["roundd"] = i.css("p.b-fight-details__table-text::text").getall()[19].strip()
                try:
                    fight_item["time"] = i.css("p.b-fight-details__table-text::text").getall()[20].strip()
                except Exception:
                    fight_item["time"] = i.css("p.b-fight-details__table-text::text").getall()[19].strip()

                
            yield fight_item
        