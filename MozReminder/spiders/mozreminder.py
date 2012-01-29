from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from MozReminder.items import MozreminderItem

class TareaSpider(BaseSpider):
  name = "tareas"
  allowed_domains = ["mozilla-hispano.org"]
  start_url = [
	"https://www.mozilla-hispano.org/documentacion/Tareas"
  ]

  def parse(self, response):
	hxs = HtmlXPathSelector(response)
        sites = hxs.select('//table/tr')
        for site in sites:
                item = MozreminderItem()
                item['tarea'] = site.select('td/a/text()').extract()
                item['link_tarea'] = site.select('td/a/@href').extract()
                item['limite'] = site.select('td[6]').extract()
                items.append(item)
        return items

