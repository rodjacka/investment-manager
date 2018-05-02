from datamanager.admin import SecurityResource
import tablib
security_resource = SecurityResource()
data = tablib.Dataset().load(open('datamanager/data/securities.csv').read())
result = security_resource.import_data(data, dry_run=True)