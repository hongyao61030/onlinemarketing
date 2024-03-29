import os
import sys
import django

module_path = os.path.abspath(os.getcwd() + '\\')

path_folder = os.path.abspath(os.getcwd() + '\\flashsale')
if path_folder in sys.path:
    sys.path.remove(path_folder)

if module_path not in sys.path:
    sys.path.append(module_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinemarket.settings')
django.setup()

from flashsale.kafka.kafka_service import consumer_2
from flashsale.models import FlashSale, FlashOrder
from flashsale.redis_service import remove_customer_to_limit, reverse_stock

print('customer for loop 2')
if __name__ == '__main__':
    for message in consumer_2:
        data = message.value
        customer_id = data['customer_id']
        flash_sale_id = data['flash_sale_id']
        try:
            flash_order = FlashOrder.objects.get(customer=customer_id, flash_sale=flash_sale_id, status__in=[0, 1])
            flash_sale = FlashSale.objects.get(id=flash_sale_id)
            print('available: ', flash_sale.available_qty)

            if flash_order.status != 1:
                flash_order.status = 2
                flash_sale.available_qty += 1
                flash_sale.locked_qty -= 1
                flash_order.save()
                flash_sale.save()
                try:
                    reverse_stock(flash_sale_id)
                except:
                    print('reverse is not successful')
                remove_customer_to_limit(customer_id, flash_sale_id)
                print('after available: ', flash_sale.available_qty)
            print('check_pay_status is consumed by message queue')
        except:
            print('No such flash order found')
   
