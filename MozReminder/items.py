from scrapy.item import Item, Field

class MozreminderItem(Item):

    tarea = Field()
    link_tarea = Field()
    limite = Field()
    responsable = Field()
    link_user = Field()
    mail = Field()
