from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from MozReminder.items import MozreminderItem

items = []

class TareaSpider(BaseSpider):
  name = "tareas"
  allowed_domains = ["mozilla-hispano.org"]
  start_urls = [
	"https://www.mozilla-hispano.org/documentacion/Tareas"
  ]

  def parse(self, response):
      hxs = HtmlXPathSelector(response)
      sites = hxs.select('//table/tr')
      for site in sites:
          item = MozreminderItem()
          item['tarea'] = site.select('td/a/text()').extract()
          link_tarea = site.select('td/a/@href').extract()
          item['limite'] = site.select('td[6]/text()').extract()
	  items.append(item)
      for url in link_tarea:
	  yield Request("https://www.mozilla-hispano.org"+url, callback=self.parse_links)
  def parse_links(self, response):
      hxs = HtmlXPathSelector(response)
      links = hxs.select('//div[@id="bodyContent"]/ul/li/a')
      for link in links:
	  item = MozreminderItem()
	  item['responsable'] = link.select('text()').extract()
	  link_user = link.select('@href').extract()
	  items.append(item)
      for url in link_user:
	  yield Request("https://www.mozilla-hispano.org"+url, callback=self.parse_user)
  def parse_user(self, response):
      hxs = HtmlXPathSelector(response)
      users = hxs.select('//table/tr[10]/td[2]')
      for user in users:
	  item = MozreminderItem()
	  item['mail'] = user.select('text()').extract()
	  items.append(item)
      return items
