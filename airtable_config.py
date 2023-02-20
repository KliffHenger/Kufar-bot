from pyairtable import Table, Api


api_key = 'key64C9CvHlRvTZnd'
base_id = 'appgqujCtrKkaE1ze'
# table_name = 'tblThveQNAe8wfrHb' # table - основная таблица
table_name = 'tblV8GlP0Kcm6vdCn' # table copy - тестовая таблица


table = Table(api_key, base_id, table_name)


